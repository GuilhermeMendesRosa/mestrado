package br.com.udesc.orchestrator_database_synchonizer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class OrchestratorDatabaseSynchonizerApplication {

	public static void main(String[] args) {
		SpringApplication.run(OrchestratorDatabaseSynchonizerApplication.class, args);
	}

}
