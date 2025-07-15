package br.com.roselabs.lbot_datagen_backend.repositories;

import br.com.roselabs.lbot_datagen_backend.entities.Execution;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface ExecutionRepository extends JpaRepository<Execution, UUID> {

    List<Execution> findBySessionId(UUID sessionId);

    List<Execution> findByGrade(Integer grade);

    List<Execution> findByGradeBetween(Integer minGrade, Integer maxGrade);

    @Query("SELECT e FROM Execution e WHERE e.session.id = :sessionId ORDER BY e.id")
    List<Execution> findBySessionIdOrderById(UUID sessionId);

    @Query("SELECT AVG(e.grade) FROM Execution e WHERE e.session.id = :sessionId")
    Double getAverageGradeBySessionId(UUID sessionId);
}