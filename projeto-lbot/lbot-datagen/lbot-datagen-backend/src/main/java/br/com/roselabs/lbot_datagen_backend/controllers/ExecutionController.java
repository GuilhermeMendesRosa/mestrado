package br.com.roselabs.lbot_datagen_backend.controllers;

import br.com.roselabs.lbot_datagen_backend.entities.Execution;
import br.com.roselabs.lbot_datagen_backend.services.ExecutionService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/api/executions")
@RequiredArgsConstructor
public class ExecutionController {

    private final ExecutionService executionService;

    @PostMapping
    public ResponseEntity<Execution> createExecution(@RequestBody Execution execution, @RequestParam UUID sessionId) {
        try {
            Execution createdExecution = executionService.createExecution(execution, sessionId);
            return ResponseEntity.status(HttpStatus.CREATED).body(createdExecution);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().build();
        }
    }

    @GetMapping("/{id}")
    public ResponseEntity<Execution> getExecution(@PathVariable UUID id) {
        Optional<Execution> execution = executionService.findById(id);
        return execution.map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping
    public ResponseEntity<List<Execution>> getAllExecutions() {
        List<Execution> executions = executionService.findAll();
        return ResponseEntity.ok(executions);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Execution> updateExecution(@PathVariable UUID id, @RequestBody Execution execution) {
        if (!executionService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        execution.setId(id);
        Execution updatedExecution = executionService.updateExecution(execution);
        return ResponseEntity.ok(updatedExecution);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteExecution(@PathVariable UUID id) {
        if (!executionService.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        executionService.deleteExecution(id);
        return ResponseEntity.noContent().build();
    }
}