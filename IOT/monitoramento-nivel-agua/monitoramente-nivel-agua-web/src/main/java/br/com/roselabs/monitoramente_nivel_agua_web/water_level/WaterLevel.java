package br.com.roselabs.monitoramente_nivel_agua_web.water_level;

public class WaterLevel {
    private Boolean lowLevel = true;

    public Boolean getLowLevel() {
        return lowLevel;
    }

    public void setLowLevel(Boolean lowLevel) {
        this.lowLevel = lowLevel;
    }

    public void toggleWaterLevel() {
        this.lowLevel = !lowLevel;
    }

}
