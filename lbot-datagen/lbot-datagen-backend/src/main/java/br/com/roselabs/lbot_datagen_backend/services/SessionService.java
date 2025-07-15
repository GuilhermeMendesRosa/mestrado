package br.com.roselabs.lbot_datagen_backend.services;

import br.com.roselabs.lbot_datagen_backend.entities.Session;
import br.com.roselabs.lbot_datagen_backend.repositories.SessionRepository;
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
public class SessionService {

    private final SessionRepository sessionRepository;

    public Session createSession() {
        Session session = Session.builder()
                .createdAt(LocalDateTime.now())
                .build();
        return sessionRepository.save(session);
    }

    public Session createSession(LocalDateTime createdAt) {
        Session session = Session.builder()
                .createdAt(createdAt)
                .build();
        return sessionRepository.save(session);
    }

    @Transactional(readOnly = true)
    public Optional<Session> findById(UUID id) {
        return sessionRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public Optional<Session> findByIdWithExecutions(UUID id) {
        return sessionRepository.findByIdWithExecutions(id);
    }

    @Transactional(readOnly = true)
    public List<Session> findAll() {
        return sessionRepository.findAllOrderByCreatedAtDesc();
    }

    @Transactional(readOnly = true)
    public List<Session> findByDateRange(LocalDateTime start, LocalDateTime end) {
        return sessionRepository.findByCreatedAtBetween(start, end);
    }

    public Session updateSession(Session session) {
        return sessionRepository.save(session);
    }

    public void deleteSession(UUID id) {
        sessionRepository.deleteById(id);
    }

    public boolean existsById(UUID id) {
        return sessionRepository.existsById(id);
    }
}