package br.com.roselabs.lbot_datagen_backend.controllers;

import br.com.roselabs.lbot_datagen_backend.entities.Session;
import br.com.roselabs.lbot_datagen_backend.services.SessionService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/api/sessions")
@RequiredArgsConstructor
public class SessionController {

    private final SessionService sessionService;

    @PostMapping
    public ResponseEntity<Session> createSession(@RequestBody Session session) {
        Session createdSession = sessionService.createSession();
        return ResponseEntity.status(HttpStatus.CREATED).body(createdSession);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Session> getSession(@PathVariable UUID id) {
        Optional<Session> session = sessionService.findById(id);
        return session.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping
    public ResponseEntity<List<Session>> getAllSessions() {
        List<Session> sessions = sessionService.findAll();
        return ResponseEntity.ok(sessions);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Session> updateSession(@PathVariable UUID id, @RequestBody Session session) {
        if (!sessionService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        session.setId(id);
        Session updatedSession = sessionService.updateSession(session);
        return ResponseEntity.ok(updatedSession);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteSession(@PathVariable UUID id) {
        if (!sessionService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        sessionService.deleteSession(id);
        return ResponseEntity.noContent().build();
    }
}