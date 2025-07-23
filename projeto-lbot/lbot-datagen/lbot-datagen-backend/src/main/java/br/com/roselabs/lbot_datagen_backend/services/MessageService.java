package br.com.roselabs.lbot_datagen_backend.services;

import br.com.roselabs.lbot_datagen_backend.ai.AIService;
import br.com.roselabs.lbot_datagen_backend.dtos.EvaluateMessageDto;
import br.com.roselabs.lbot_datagen_backend.dtos.SendMessageDto;
import br.com.roselabs.lbot_datagen_backend.entities.Chat;
import br.com.roselabs.lbot_datagen_backend.entities.Message;
import br.com.roselabs.lbot_datagen_backend.repositories.MessageRepository;
import jakarta.persistence.EntityNotFoundException;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.UUID;

@Service
@RequiredArgsConstructor
@Transactional
public class MessageService {

    private final ChatService chatService;
    private final AIService aiService;
    private final MessageRepository messageRepository;

    public Message sendMessage(SendMessageDto sendMessageDto) {
        UUID chatId = sendMessageDto.getChatId();
        Chat chat = chatService.findById(chatId)
                .orElseThrow(() -> new EntityNotFoundException("Chat not found with id: " + chatId));

        String prompt = sendMessageDto.getPrompt();
        String output = aiService.convertToLML(prompt);

        Message message = Message.builder()
                .prompt(prompt)
                .chat(chat)
                .output(output)
                .build();

        return messageRepository.save(message);
    }

    public Message evaluateMessage(EvaluateMessageDto evaluateMessageDto) {
        UUID messageId = evaluateMessageDto.getMessageId();
        Message message = messageRepository.findById(messageId)
                .orElseThrow(() -> new EntityNotFoundException("Message not found with id: " + messageId));

        message.setGrade(evaluateMessageDto.getGrade());
        return messageRepository.save(message);
    }
}