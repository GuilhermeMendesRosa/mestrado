package br.com.roselabs.lbot_datagen_backend.controllers;

import br.com.roselabs.lbot_datagen_backend.dtos.EvaluateMessageDto;
import br.com.roselabs.lbot_datagen_backend.dtos.SendMessageDto;
import br.com.roselabs.lbot_datagen_backend.entities.Message;
import br.com.roselabs.lbot_datagen_backend.services.MessageService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("messages")
@RequiredArgsConstructor
public class MessageController {

    private final MessageService messageService;

    @PostMapping
    public ResponseEntity<Message> sendMessage(@RequestBody SendMessageDto sendMessageDto) {
        try {
            Message createdMessage = messageService.sendMessage(sendMessageDto);
            return ResponseEntity.status(HttpStatus.CREATED).body(createdMessage);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().build();
        }
    }

    @PostMapping("evaluate")
    public ResponseEntity<Message> evaluateMessage(@RequestBody EvaluateMessageDto evaluateMessageDto) {
        try {
            Message createdMessage = messageService.evaluateMessage(evaluateMessageDto);
            return ResponseEntity.status(HttpStatus.ACCEPTED).body(createdMessage);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().build();
        }
    }

}