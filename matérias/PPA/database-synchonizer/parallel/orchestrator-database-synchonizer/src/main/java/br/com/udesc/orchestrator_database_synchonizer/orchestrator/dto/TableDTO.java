package br.com.udesc.orchestrator_database_synchonizer.orchestrator.dto;

public class TableDTO {
    private String name;
    private Boolean isFinished;

    public TableDTO() {
    }

    public TableDTO(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Boolean getFinished() {
        return isFinished;
    }

    public void setFinished(Boolean finished) {
        isFinished = finished;
    }
}
