package br.com.roselabs.lbot_datagen_backend.repositories;

import br.com.roselabs.lbot_datagen_backend.entities.Session;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface SessionRepository extends JpaRepository<Session, UUID> {

    List<Session> findByCreatedAtBetween(LocalDateTime start, LocalDateTime end);

    @Query("SELECT s FROM Session s LEFT JOIN FETCH s.executions WHERE s.id = :id")
    Optional<Session> findByIdWithExecutions(UUID id);

    @Query("SELECT s FROM Session s ORDER BY s.createdAt DESC")
    List<Session> findAllOrderByCreatedAtDesc();
}