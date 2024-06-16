package com.investAssistant.investAssistant.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@RestController
@RequestMapping("/api")
public class RecommendationController {

    @Value("${python.api.url}")
    private String pythonApiUrl;

    @PostMapping("/recommend")
    public ResponseEntity<?> getRecommendations(@RequestBody Map<String, Object> criteria) {
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<Map> response = restTemplate.postForEntity(pythonApiUrl + "/predict", criteria, Map.class);
        return ResponseEntity.ok(response.getBody());
    }
}
