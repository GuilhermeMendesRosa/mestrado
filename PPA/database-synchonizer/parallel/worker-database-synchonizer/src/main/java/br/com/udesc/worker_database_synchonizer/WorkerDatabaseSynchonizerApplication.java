package br.com.udesc.worker_database_synchonizer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class WorkerDatabaseSynchonizerApplication {

	public static void main(String[] args) {
		SpringApplication.run(WorkerDatabaseSynchonizerApplication.class, args);
	}

}
