package br.com.roselabs.lbot_datagen_backend.services;

import br.com.roselabs.lbot_datagen_backend.entities.Execution;
import br.com.roselabs.lbot_datagen_backend.entities.Session;
import br.com.roselabs.lbot_datagen_backend.repositories.ExecutionRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
@RequiredArgsConstructor
@Transactional
public class ExecutionService {

    private final ExecutionRepository executionRepository;
    private final SessionService sessionService;

    public Execution createExecution(UUID sessionId, String prompt, String output, Integer grade, String observation) {
        Optional<Session> sessionOpt = sessionService.findById(sessionId);
        if (sessionOpt.isEmpty()) {
            throw new RuntimeException("Session not found with id: " + sessionId);
        }

        Session session = sessionOpt.get();
        Execution execution = Execution.builder()
                .prompt(prompt)
                .output(output)
                .grade(grade)
                .observation(observation)
                .session(session)
                .build();

        Execution savedExecution = executionRepository.save(execution);
        session.addExecution(savedExecution);

        return savedExecution;
    }

    public Execution createExecution(Execution execution, UUID sessionId) {
        Optional<Session> sessionOpt = sessionService.findById(sessionId);
        if (sessionOpt.isEmpty()) {
            throw new RuntimeException("Session not found with id: " + sessionId);
        }

        execution.setSession(sessionOpt.get());
        return executionRepository.save(execution);
    }

    @Transactional(readOnly = true)
    public Optional<Execution> findById(UUID id) {
        return executionRepository.findById(id);
    }

    @Transactional(readOnly = true)
    public List<Execution> findAll() {
        return executionRepository.findAll();
    }

    @Transactional(readOnly = true)
    public List<Execution> findBySessionId(UUID sessionId) {
        return executionRepository.findBySessionIdOrderById(sessionId);
    }

    @Transactional(readOnly = true)
    public List<Execution> findByGrade(Integer grade) {
        return executionRepository.findByGrade(grade);
    }

    @Transactional(readOnly = true)
    public List<Execution> findByGradeRange(Integer minGrade, Integer maxGrade) {
        return executionRepository.findByGradeBetween(minGrade, maxGrade);
    }

    @Transactional(readOnly = true)
    public Double getAverageGradeBySession(UUID sessionId) {
        return executionRepository.getAverageGradeBySessionId(sessionId);
    }

    public Execution updateExecution(Execution execution) {
        return executionRepository.save(execution);
    }

    public void deleteExecution(UUID id) {
        executionRepository.deleteById(id);
    }

    public boolean existsById(UUID id) {
        return executionRepository.existsById(id);
    }
}