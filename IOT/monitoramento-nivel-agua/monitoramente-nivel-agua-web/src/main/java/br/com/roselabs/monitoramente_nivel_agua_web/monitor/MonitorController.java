package br.com.roselabs.monitoramente_nivel_agua_web.monitor;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/monitor")
public class MonitorController {

    @GetMapping()
    public String home() {
        return "forward:/index.html";
    }
}