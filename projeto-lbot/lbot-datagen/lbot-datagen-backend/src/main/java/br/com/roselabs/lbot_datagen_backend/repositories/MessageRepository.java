package br.com.roselabs.lbot_datagen_backend.repositories;

import br.com.roselabs.lbot_datagen_backend.entities.Message;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface MessageRepository extends JpaRepository<Message, UUID> {

    List<Message> findByChatId(UUID chatId);

    List<Message> findByGrade(Integer grade);

    List<Message> findByGradeBetween(Integer minGrade, Integer maxGrade);

    @Query("SELECT e FROM Message e WHERE e.chat.id = :chatId ORDER BY e.id")
    List<Message> findByChatIdOrderById(UUID chatId);

    @Query("SELECT AVG(e.grade) FROM Message e WHERE e.chat.id = :chatId")
    Double getAverageGradeByChatId(UUID chatId);
}