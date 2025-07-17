package br.com.roselabs.lbot_datagen_backend.controllers;

import br.com.roselabs.lbot_datagen_backend.entities.Chat;
import br.com.roselabs.lbot_datagen_backend.services.ChatService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/api/chats")
@RequiredArgsConstructor
public class ChatController {

    private final ChatService chatService;

    @PostMapping
    public ResponseEntity<Chat> createChat(@RequestBody Chat chat) {
        Chat createdChat = chatService.createChat();
        return ResponseEntity.status(HttpStatus.CREATED).body(createdChat);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Chat> getChat(@PathVariable UUID id) {
        Optional<Chat> Chat = chatService.findById(id);
        return Chat.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping
    public ResponseEntity<List<Chat>> getAllChats() {
        List<Chat> chats = chatService.findAll();
        return ResponseEntity.ok(chats);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Chat> updateChat(@PathVariable UUID id, @RequestBody Chat chat) {
        if (!chatService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        chat.setId(id);
        Chat updatedChat = chatService.updateChat(chat);
        return ResponseEntity.ok(updatedChat);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteChat(@PathVariable UUID id) {
        if (!chatService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        chatService.deleteChat(id);
        return ResponseEntity.noContent().build();
    }
}