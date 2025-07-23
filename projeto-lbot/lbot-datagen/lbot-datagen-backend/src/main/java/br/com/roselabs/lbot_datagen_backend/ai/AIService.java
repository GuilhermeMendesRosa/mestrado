package br.com.roselabs.lbot_datagen_backend.ai;

import org.springframework.stereotype.Service;

@Service
public class AIService {

    public String convertToLML(String prompt) {
        String standardizedPrompt = standardizesPromptImCm(prompt);
        return convert(standardizedPrompt);
    }

    //TODO
    private String convert(String prompt) {
        return "resultado";
    }

    //TODO
    private String standardizesPromptImCm(String prompt) {
        return "prompt in cm";
    }
}
