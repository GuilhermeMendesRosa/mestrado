// lbot-chat.component.ts
import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { interval, Subscription } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';

interface Message {
  text: string;
  type: 'user' | 'bot' | 'error';
}

interface TranslateResponse {
  result: string;
}

@Component({
  selector: 'app-lbot-chat',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './lbot-chat.html',
  styleUrls: ['./lbot-chat.css']
})
export class LbotChat implements OnInit, OnDestroy {
  API_URL = 'http://ec2-15-228-173-198.sa-east-1.compute.amazonaws.com:8000';
  messages: Message[] = [
    { text: 'Olá! Digite um comando em português e eu traduzo para LBot.', type: 'bot' }
  ];
  messageInput = '';
  isLoading = false;
  isOnline = false;
  statusText = 'Verificando...';
  private statusCheckSubscription?: Subscription;

  constructor(private http: HttpClient) {}

  ngOnInit() {
    // this.checkStatus();
    // // Verificar status a cada 30 segundos
    // this.statusCheckSubscription = interval(30000).subscribe(() => {
    //   this.checkStatus();
    // });
  }

  ngOnDestroy() {
    if (this.statusCheckSubscription) {
      this.statusCheckSubscription.unsubscribe();
    }
  }

  checkStatus() {
    this.http.get(this.API_URL)
      .pipe(
        catchError(() => of(null))
      )
      .subscribe(response => {
        if (response !== null) {
          this.isOnline = true;
          this.statusText = '🟢 Online';
        } else {
          this.isOnline = false;
          this.statusText = '🔴 Offline';
        }
      });
  }

  async sendMessage() {
    const command = this.messageInput.trim();
    if (!command || this.isLoading) return;

    // Adicionar mensagem do usuário
    this.messages.push({ text: command, type: 'user' });
    this.messageInput = '';
    this.isLoading = true;

    try {
      const response = await this.http.post<TranslateResponse>(
        `${this.API_URL}/translate`,
        { command }
      ).toPromise();

      if (response?.result) {
        this.messages.push({ text: `🤖 ${response.result}`, type: 'bot' });
      } else {
        throw new Error('Resposta inválida');
      }
    } catch (error) {
      this.messages.push({
        text: '❌ Erro na tradução. Verifique se a API está rodando.',
        type: 'error'
      });
    } finally {
      this.isLoading = false;
      this.scrollToBottom();
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
