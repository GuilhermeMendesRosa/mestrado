// lbot-chat.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface Message {
  text: string;
  type: 'user' | 'bot' | 'error';
}

@Component({
  selector: 'app-lbot-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './lbot-chat.html',
  styleUrls: ['./lbot-chat.css']
})
export class LbotChat {
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

  // Variáveis para o popup de observação (ao finalizar)
  showObservation = false;
  observation = '';

  // Array para armazenar todas as avaliações
  ratings: number[] = [];

  sendMessage() {
    const command = this.messageInput.trim();
    if (!command || this.isLoading || this.isWaitingForRating) return;

    // Adicionar mensagem do usuário
    this.messages.push({ text: command, type: 'user' });
    this.messageInput = '';
    this.isLoading = true;

    // Simular processamento
    setTimeout(() => {
      this.messages.push({
        text: `🤖 Comando processado: ${command}`,
        type: 'bot'
      });
      this.isLoading = false;
      this.scrollToBottom();

      // Iniciar período de espera de 5 segundos
      this.startWaitingPeriod();
    }, 1000);
  }

  startWaitingPeriod() {
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

  showRatingPopup() {
    this.showRating = true;
    this.selectedRating = 0;
    this.hoverRating = 0;
  }

  closeRatingPopup() {
    this.showRating = false;
    this.selectedRating = 0;
    this.hoverRating = 0;
  }

  selectRating(rating: number) {
    this.selectedRating = rating;
  }

  submitRating() {
    if (this.selectedRating > 0) {
      // Armazenar a avaliação
      this.ratings.push(this.selectedRating);
      console.log('Avaliação da mensagem:', this.selectedRating);
      console.log('Todas as avaliações:', this.ratings);

      this.closeRatingPopup();
    }
  }

  showObservationPopup() {
    if (this.isWaitingForRating) return; // Não permite finalizar durante a espera

    this.showObservation = true;
    this.observation = '';
  }

  closeObservationPopup() {
    this.showObservation = false;
    this.observation = '';
  }

  submitObservation() {
    // Calcular média das avaliações
    const averageRating = this.ratings.length > 0
      ? (this.ratings.reduce((sum, rating) => sum + rating, 0) / this.ratings.length).toFixed(1)
      : 'N/A';

    // Dados finais para envio
    const finalFeedback = {
      individualRatings: this.ratings,
      averageRating: averageRating,
      totalMessages: this.ratings.length,
      observation: this.observation.trim()
    };

    console.log('Feedback final:', finalFeedback);

    // Mostrar mensagem de agradecimento
    let thankYouMessage = `Obrigado pelo feedback! `;

    if (this.ratings.length > 0) {
      thankYouMessage += `Média das avaliações: ${averageRating} estrelas. `;
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

  onKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter' && !this.isWaitingForRating) {
      this.sendMessage();
    }
  }

  private scrollToBottom() {
    setTimeout(() => {
      const messagesContainer = document.querySelector('.chat-messages');
      if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
      }
    }, 100);
  }

  ngOnDestroy() {
    // Limpar interval se o componente for destruído
    if (this.countdownInterval) {
      clearInterval(this.countdownInterval);
    }
  }
}
