package br.com.roselabs.monitoramente_nivel_agua_backend.water_level;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/water-level")
public class WaterLevelController {

    private WaterLevel waterLevel = new WaterLevel();

    @PostMapping()
    public void setWaterLevel(@RequestBody WaterLevel waterLevel) {
        this.waterLevel = waterLevel;
    }

    @GetMapping()
    public ResponseEntity<WaterLevel> getWaterLevel() {
        return ResponseEntity.ok(waterLevel);
    }

    public void toggleWaterLevel() {
        this.waterLevel.toggleWaterLevel();
    }
}