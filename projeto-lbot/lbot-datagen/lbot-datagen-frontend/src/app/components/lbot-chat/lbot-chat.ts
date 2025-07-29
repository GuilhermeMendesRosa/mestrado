// lbot-chat.component.ts
import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatDto, EvaluateResponse, MessageDto, MessagesService } from '../../services/messages-service';

interface Message {
  text: string;
  type: 'user' | 'bot' | 'error';
  messageId?: string;
  normalizedPrompt?: string;
  output?: string;
}

@Component({
  selector: 'app-lbot-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './lbot-chat.html',
  styleUrls: ['./lbot-chat.css']
})
export class LbotChat implements OnInit, OnDestroy {
  messages: Message[] = [
    { text: 'Olá! Digite um comando em português e eu traduzo para LBot.', type: 'bot' }
  ];
  messageInput = '';
  isLoading = false;

  // Variáveis para controlar o período de espera
  isWaitingForRating = false;
  countdown = 5;
  countdownInterval: any;

  // Variáveis para o popup de avaliação (após cada mensagem)
  showRating = false;
  selectedRating = 0;
  hoverRating = 0;
  currentMessageId = '';

  // Variáveis para o popup de observação (ao finalizar)
  showObservation = false;
  observation = '';

  // Array para armazenar todas as avaliações
  ratings: number[] = [];

  // ID do chat atual
  chatId = '';

  constructor(private messagesService: MessagesService) {}

  ngOnInit(): void {
    this.initializeChat();
  }

  initializeChat(): void {
    this.messagesService.startChat().subscribe({
      next: (response: ChatDto) => {
        this.chatId = response.id;
        console.log('Chat iniciado:', response);
        console.log('Chat ID:', this.chatId);
        console.log('Data de criação:', response.createdAt);
      },
      error: (error: any) => {
        console.error('Erro ao iniciar chat:', error);
        this.messages.push({
          text: 'Erro ao iniciar o chat. Tente novamente.',
          type: 'error'
        });
      }
    });
  }

  sendMessage(): void {
    const command = this.messageInput.trim();
    if (!command || this.isLoading || this.isWaitingForRating || !this.chatId) return;

    // Adicionar mensagem do usuário
    this.messages.push({ text: command, type: 'user' });
    this.messageInput = '';
    this.isLoading = true;
    this.scrollToBottom();

    // Enviar mensagem para a API
    this.messagesService.sendMessage({
      prompt: command,
      chatId: this.chatId
    }).subscribe({
      next: (response: MessageDto) => {
        console.log('Resposta da API:', response);

        // Criar mensagem formatada com as informações da resposta
        let botMessage = '';

        if (response.normalizedPrompt) {
          botMessage += `📝 Comando normalizado: ${response.normalizedPrompt}\n\n`;
        }

        if (response.output) {
          botMessage += `🤖 Código LBot: ${response.output}`;
        }

        if (!botMessage) {
          botMessage = 'Comando processado com sucesso!';
        }

        // Adicionar resposta do bot
        this.messages.push({
          text: botMessage,
          type: 'bot',
          messageId: response.id,
          normalizedPrompt: response.normalizedPrompt,
          output: response.output
        });

        this.isLoading = false;
        this.scrollToBottom();

        // Armazenar o ID da mensagem para avaliação
        this.currentMessageId = response.id;

        // Iniciar período de espera de 5 segundos
        this.startWaitingPeriod();
      },
      error: (error: any) => {
        console.error('Erro ao enviar mensagem:', error);
        this.messages.push({
          text: 'Erro ao processar sua mensagem. Tente novamente.',
          type: 'error'
        });
        this.isLoading = false;
        this.scrollToBottom();
      }
    });
  }

  startWaitingPeriod(): void {
    this.isWaitingForRating = true;
    this.countdown = 5;
    this.scrollToBottom();

    this.countdownInterval = setInterval(() => {
      this.countdown--;

      if (this.countdown <= 0) {
        clearInterval(this.countdownInterval);
        this.isWaitingForRating = false;
        this.showRatingPopup();
      }
    }, 1000);
  }

  showRatingPopup(): void {
    this.showRating = true;
    this.selectedRating = 0;
    this.hoverRating = 0;
  }

  closeRatingPopup(): void {
    this.showRating = false;
    this.selectedRating = 0;
    this.hoverRating = 0;
    this.currentMessageId = '';
  }

  selectRating(rating: number): void {
    this.selectedRating = rating;
  }

  submitRating(): void {
    if (this.selectedRating > 0 && this.currentMessageId) {
      // Enviar avaliação para a API
      this.messagesService.evaluateMessage({
        messageId: this.currentMessageId,
        grade: this.selectedRating
      }).subscribe({
        next: (response: EvaluateResponse) => {
          console.log('Avaliação enviada com sucesso:', response);
          console.log(`Mensagem ${this.currentMessageId} avaliada com nota ${this.selectedRating}`);

          // Armazenar a avaliação localmente
          this.ratings.push(this.selectedRating);
          console.log('Todas as avaliações:', this.ratings);

          this.closeRatingPopup();
        },
        error: (error: any) => {
          console.error('Erro ao enviar avaliação:', error);
          // Mesmo com erro, armazenar localmente
          this.ratings.push(this.selectedRating);
          this.closeRatingPopup();

          // Mostrar mensagem de erro (opcional)
          this.messages.push({
            text: 'Avaliação registrada localmente (erro na conexão).',
            type: 'error'
          });
          this.scrollToBottom();
        }
      });
    }
  }

  showObservationPopup(): void {
    if (this.isWaitingForRating) return;

    this.showObservation = true;
    this.observation = '';
  }

  closeObservationPopup(): void {
    this.showObservation = false;
    this.observation = '';
  }

  submitObservation(): void {
    // Calcular média das avaliações
    const averageRating = this.ratings.length > 0
      ? (this.ratings.reduce((sum, rating) => sum + rating, 0) / this.ratings.length).toFixed(1)
      : 'N/A';

    // Dados finais para envio
    const finalFeedback = {
      chatId: this.chatId,
      individualRatings: this.ratings,
      averageRating: averageRating,
      totalMessages: this.ratings.length,
      observation: this.observation.trim()
    };

    console.log('Feedback final do chat:', finalFeedback);

    // Mostrar mensagem de agradecimento
    let thankYouMessage = `Obrigado pelo feedback! `;

    if (this.ratings.length > 0) {
      thankYouMessage += `Média das avaliações: ${averageRating} estrelas (${this.ratings.length} mensagem${this.ratings.length > 1 ? 's' : ''} avaliada${this.ratings.length > 1 ? 's' : ''}). `;
    }

    if (this.observation.trim()) {
      thankYouMessage += 'Suas observações foram registradas.';
    }

    this.messages.push({
      text: thankYouMessage,
      type: 'bot'
    });

    this.closeObservationPopup();
    this.scrollToBottom();

    // Finalizar o chat
    setTimeout(() => {
      this.messages.push({
        text: 'Chat finalizado. Até a próxima! 👋',
        type: 'bot'
      });
      this.scrollToBottom();
    }, 2000);
  }

  onKeyPress(event: KeyboardEvent): void {
    if (event.key === 'Enter' && !this.isWaitingForRating) {
      this.sendMessage();
    }
  }

  private scrollToBottom(): void {
    setTimeout(() => {
      const messagesContainer = document.querySelector('.chat-messages');
      if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    }, 100);
  }

  ngOnDestroy(): void {
    // Limpar interval se o componente for destruído
    if (this.countdownInterval) {
      clearInterval(this.countdownInterval);
    }
  }
}
