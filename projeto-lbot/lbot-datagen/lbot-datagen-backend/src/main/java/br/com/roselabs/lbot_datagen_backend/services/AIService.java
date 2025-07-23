package br.com.roselabs.lbot_datagen_backend.services;

import lombok.RequiredArgsConstructor;
import org.springframework.ai.openai.OpenAiChatModel;
import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.charset.StandardCharsets;

@Service
@RequiredArgsConstructor
public class AIService {

    private final OpenAiChatModel openAiChatModel;

    public String normalizePromptImCm(String prompt) {
        try {
            String systemPrompt = loadPromptFromFile("static/prompts/normalize-prompts-in-cm.txt");
            String fullPrompt = systemPrompt + prompt;

            return openAiChatModel.call(fullPrompt);
        } catch (IOException e) {
            throw new RuntimeException("Erro ao carregar arquivo de prompt", e);
        }
    }

    public String convertToLML(String prompt) {
        return convert(prompt);
    }

    private String convert(String prompt) {
        try {
            String systemPrompt = loadPromptFromFile("static/prompts/convert-to-lml.txt");
            String fullPrompt = systemPrompt + prompt;

            return openAiChatModel.call(fullPrompt);
        } catch (IOException e) {
            throw new RuntimeException("Erro ao carregar arquivo de prompt", e);
        }
    }

    private String loadPromptFromFile(String filePath) throws IOException {
        ClassPathResource resource = new ClassPathResource(filePath);
        return resource.getContentAsString(StandardCharsets.UTF_8);
    }
}