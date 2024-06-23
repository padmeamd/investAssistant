package com.investAssistant.investAssistant.controller;

import com.investAssistant.investAssistant.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class RecommendationController {

    @Autowired
    private UserService userService;

    @GetMapping("/file-content")
    public String getFileContent() {
        return userService.getFileContent();
    }
}
