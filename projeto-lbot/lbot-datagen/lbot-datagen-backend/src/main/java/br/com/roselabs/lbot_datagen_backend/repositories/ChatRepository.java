package br.com.roselabs.lbot_datagen_backend.repositories;

import br.com.roselabs.lbot_datagen_backend.entities.Chat;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface ChatRepository extends JpaRepository<Chat, UUID> {

    List<Chat> findByCreatedAtBetween(LocalDateTime start, LocalDateTime end);

    @Query("SELECT s FROM Chat s LEFT JOIN FETCH s.messages WHERE s.id = :id")
    Optional<Chat> findByIdWithExecutions(UUID id);

    @Query("SELECT s FROM Chat s ORDER BY s.createdAt DESC")
    List<Chat> findAllOrderByCreatedAtDesc();
}