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

    public Message createMessage(UUID sessionId, String prompt, String output, Integer grade, String observation) {
        Optional<Chat> sessionOpt = chatService.findById(sessionId);
        if (sessionOpt.isEmpty()) {
            throw new RuntimeException("Chat not found with id: " + sessionId);
        }

        Chat chat = sessionOpt.get();
        Message message = Message.builder()
                .prompt(prompt)
                .output(output)
                .grade(grade)
                .observation(observation)
                .chat(chat)
                .build();

        Message savedMessage = messageRepository.save(message);
        chat.addMessage(savedMessage);

        return savedMessage;
    }

    public Message createMessage(Message message, UUID chatId) {
        Optional<Chat> sessionOpt = chatService.findById(chatId);
        if (sessionOpt.isEmpty()) {
            throw new RuntimeException("Chat not found with id: " + chatId);
        }

        message.setChat(sessionOpt.get());
        return messageRepository.save(message);
    }

    @Transactional(readOnly = true)
    public Optional<Message> findById(UUID id) {
        return messageRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public List<Message> findAll() {
        return messageRepository.findAll();
    }

    @Transactional(readOnly = true)
    public List<Message> findByChatId(UUID chatId) {
        return messageRepository.findByChatIdOrderById(chatId);
    }

    @Transactional(readOnly = true)
    public List<Message> findByGrade(Integer grade) {
        return messageRepository.findByGrade(grade);
    }

    @Transactional(readOnly = true)
    public List<Message> findByGradeRange(Integer minGrade, Integer maxGrade) {
        return messageRepository.findByGradeBetween(minGrade, maxGrade);
    }

    @Transactional(readOnly = true)
    public Double getAverageGradeByChat(UUID chatId) {
        return messageRepository.getAverageGradeByChatId(chatId);
    }

    public Message updateMessage(Message message) {
        return messageRepository.save(message);
    }

    public void deleteMessage(UUID id) {
        messageRepository.deleteById(id);
    }

    public boolean existsById(UUID id) {
        return messageRepository.existsById(id);
    }
}