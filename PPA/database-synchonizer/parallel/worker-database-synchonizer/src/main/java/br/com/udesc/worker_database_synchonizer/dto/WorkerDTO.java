package br.com.udesc.worker_database_synchonizer.dto;

public class WorkerDTO {

    private String host;

    public WorkerDTO() {}

    public WorkerDTO(String host) {
        this.host = host;
    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }
}