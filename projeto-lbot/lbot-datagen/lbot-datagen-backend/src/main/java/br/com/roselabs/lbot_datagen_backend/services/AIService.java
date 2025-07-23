package br.com.roselabs.lbot_datagen_backend.services;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;


@Service
@RequiredArgsConstructor
public class AIService {

    public String convertToLML(String prompt) {
        String standardizedPrompt = standardizesPromptImCm(prompt);
        return convert(standardizedPrompt);
    }

    //TODO
    private String standardizesPromptImCm(String prompt) {
        return "prompt in cm";
    }

    //TODO
    private String convert(String prompt) {
        return "resultado";
    }
}
