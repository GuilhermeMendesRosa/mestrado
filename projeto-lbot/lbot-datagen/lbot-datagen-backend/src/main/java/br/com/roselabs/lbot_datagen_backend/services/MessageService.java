package br.com.roselabs.lbot_datagen_backend.services;

import br.com.roselabs.lbot_datagen_backend.entities.Message;
import br.com.roselabs.lbot_datagen_backend.entities.Chat;
import br.com.roselabs.lbot_datagen_backend.repositories.MessageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
@RequiredArgsConstructor
@Transactional
public class MessageService {

    private final MessageRepository messageRepository;
    private final ChatService chatService;

    public Message createMessage(Message message, UUID chatId) {
        Optional<Chat> sessionOpt = chatService.findById(chatId);
        if (sessionOpt.isEmpty()) {
            throw new RuntimeException("Chat not found with id: " + chatId);
        }

        message.setChat(sessionOpt.get());
        return messageRepository.save(message);
    }

}