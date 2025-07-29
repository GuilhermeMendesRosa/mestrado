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
