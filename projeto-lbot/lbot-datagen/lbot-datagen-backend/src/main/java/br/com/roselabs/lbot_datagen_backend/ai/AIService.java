package br.com.roselabs.lbot_datagen_backend.ai;

import org.springframework.stereotype.Service;

@Service
public class AIService {


    public String convertToLML(String prompt) {
        String standardizedPrompt = standardizesPromptImCm(prompt);
        return convert(standardizedPrompt);
    }

    private String convert(String prompt) {
        return "resultado";
    }

    private String standardizesPromptImCm(String prompt) {
        return prompt;
    }
}
