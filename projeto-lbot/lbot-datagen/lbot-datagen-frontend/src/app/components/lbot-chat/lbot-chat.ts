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

  // Variáveis para o popup de avaliação
  showRating = false;
  selectedRating = 0;
  hoverRating = 0;
  observation = '';

  sendMessage() {
    const command = this.messageInput.trim();
    if (!command || this.isLoading) return;

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
    }, 1000);
  }

  showRatingPopup() {
    this.showRating = true;
    this.selectedRating = 0;
    this.hoverRating = 0;
    this.observation = '';
  }

  closeRatingPopup() {
    this.showRating = false;
    this.selectedRating = 0;
    this.hoverRating = 0;
    this.observation = '';
  }

  selectRating(rating: number) {
    this.selectedRating = rating;
  }

  submitRating() {
    if (this.selectedRating > 0) {
      // Aqui você pode enviar a avaliação para um servidor
      const feedback = {
        rating: this.selectedRating,
        observation: this.observation.trim()
      };

      console.log('Avaliação enviada:', feedback);

      // Mostrar mensagem de agradecimento
      let thankYouMessage = `Obrigado pela sua avaliação de ${this.selectedRating} estrela${this.selectedRating > 1 ? 's' : ''}! 🌟`;

      if (this.observation.trim()) {
        thankYouMessage += ' Suas observações foram registradas.';
      }

      this.messages.push({
        text: thankYouMessage,
        type: 'bot'
      });

      this.closeRatingPopup();
      this.scrollToBottom();

      // Opcional: finalizar o chat após alguns segundos
      setTimeout(() => {
        this.messages.push({
          text: 'Chat finalizado. Até a próxima!',
          type: 'bot'
        });
        this.scrollToBottom();
      }, 2000);
    }
  }

  onKeyPress(event: KeyboardEvent) {
    if (event.key === 'Enter') {
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
}
