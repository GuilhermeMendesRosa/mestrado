package br.com.udesc.sequential_database_synchonizer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class SequentialDatabaseSynchonizerApplication {

	public static void main(String[] args) {
		SpringApplication.run(SequentialDatabaseSynchonizerApplication.class, args);
	}

}
