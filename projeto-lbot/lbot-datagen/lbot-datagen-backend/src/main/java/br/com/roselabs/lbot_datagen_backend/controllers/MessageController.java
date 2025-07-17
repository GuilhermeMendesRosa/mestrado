package br.com.roselabs.lbot_datagen_backend.controllers;

import br.com.roselabs.lbot_datagen_backend.entities.Message;
import br.com.roselabs.lbot_datagen_backend.services.MessageService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/api/messages")
@RequiredArgsConstructor
public class MessageController {

    private final MessageService messageService;

    @PostMapping
    public ResponseEntity<Message> createMessage(@RequestBody Message message, @RequestParam UUID chatId) {
        try {
            Message createdMessage = messageService.createMessage(message, chatId);
            return ResponseEntity.status(HttpStatus.CREATED).body(createdMessage);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().build();
        }
    }

    @GetMapping("/{id}")
    public ResponseEntity<Message> getMessage(@PathVariable UUID id) {
        Optional<Message> Message = messageService.findById(id);
        return Message.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping
    public ResponseEntity<List<Message>> getAllMessages() {
        List<Message> messages = messageService.findAll();
        return ResponseEntity.ok(messages);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Message> updateMessage(@PathVariable UUID id, @RequestBody Message message) {
        if (!messageService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        message.setId(id);
        Message updatedMessage = messageService.updateMessage(message);
        return ResponseEntity.ok(updatedMessage);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteMessage(@PathVariable UUID id) {
        if (!messageService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        messageService.deleteMessage(id);
        return ResponseEntity.noContent().build();
    }
}