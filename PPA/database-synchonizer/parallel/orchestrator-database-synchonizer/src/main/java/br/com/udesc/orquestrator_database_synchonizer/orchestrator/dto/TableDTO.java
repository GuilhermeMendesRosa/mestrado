package br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto;

public class TableDTO {
    public String name;
    public Boolean isFinished;

    public TableDTO() {
    }

    public TableDTO(String name) {
        this.name = name;
    }
}
