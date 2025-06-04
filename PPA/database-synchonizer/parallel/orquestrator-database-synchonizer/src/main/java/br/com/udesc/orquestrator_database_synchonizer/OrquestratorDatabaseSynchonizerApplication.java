package br.com.udesc.orquestrator_database_synchonizer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class OrquestratorDatabaseSynchonizerApplication {

	public static void main(String[] args) {
		SpringApplication.run(OrquestratorDatabaseSynchonizerApplication.class, args);
	}

}
