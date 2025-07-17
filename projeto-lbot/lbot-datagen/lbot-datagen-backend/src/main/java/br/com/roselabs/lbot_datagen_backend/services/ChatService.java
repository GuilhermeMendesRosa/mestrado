package br.com.roselabs.lbot_datagen_backend.services;

import br.com.roselabs.lbot_datagen_backend.entities.Chat;
import br.com.roselabs.lbot_datagen_backend.repositories.ChatRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
@RequiredArgsConstructor
@Transactional
public class ChatService {

    private final ChatRepository chatRepository;

    public Chat createChat() {
        Chat chat = Chat.builder()
                .createdAt(LocalDateTime.now())
                .build();
        return chatRepository.save(chat);
    }

    public Chat createChat(LocalDateTime createdAt) {
        Chat chat = Chat.builder()
                .createdAt(createdAt)
                .build();
        return chatRepository.save(chat);
    }

    @Transactional(readOnly = true)
    public Optional<Chat> findById(UUID id) {
        return chatRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public Optional<Chat> findByIdWithExecutions(UUID id) {
        return chatRepository.findByIdWithExecutions(id);
    }

    @Transactional(readOnly = true)
    public List<Chat> findAll() {
        return chatRepository.findAllOrderByCreatedAtDesc();
    }

    @Transactional(readOnly = true)
    public List<Chat> findByDateRange(LocalDateTime start, LocalDateTime end) {
        return chatRepository.findByCreatedAtBetween(start, end);
    }

    public Chat updateChat(Chat chat) {
        return chatRepository.save(chat);
    }

    public void deleteChat(UUID id) {
        chatRepository.deleteById(id);
    }

    public boolean existsById(UUID id) {
        return chatRepository.existsById(id);
    }
}