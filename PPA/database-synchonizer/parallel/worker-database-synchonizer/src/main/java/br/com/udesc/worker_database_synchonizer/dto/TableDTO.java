package br.com.udesc.worker_database_synchonizer.dto;

public class TableDTO {
    public String name;
    public Boolean isFinished;

    public TableDTO() {
    }

    public TableDTO(String name) {
        this.name = name;
    }
}
