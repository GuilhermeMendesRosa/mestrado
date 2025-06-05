package br.com.udesc.orquestrator_database_synchonizer.orquestrator.dto;

public class TableDTO {
    public String name;
    public Boolean isFinished;

    public TableDTO() {
    }

    public TableDTO(String name) {
        this.name = name;
    }
}
