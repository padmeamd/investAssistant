package com.investAssistant.investAssistant.controller;

import com.investAssistant.investAssistant.entity.User;
import com.investAssistant.investAssistant.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

/**
 * REST controller for authentication operations.
 */
@RestController
@RequestMapping("/api/auth")
public class AuthController {

    @Autowired
    private UserService userService;

    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;

    /**
     * Register a new user.
     *
     * @param user the user to register
     * @return the registered user
     */
    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody User user) {
        User registeredUser = userService.registerUser(user);
        return ResponseEntity.ok(registeredUser);
    }

    /**
     * Authenticate a user.
     *
     * @param credentials the user credentials
     * @return the authenticated user, or an error response if authentication fails
     */
    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody Map<String, String> credentials) {
        String email = credentials.get("email");
        String password = credentials.get("password");
        User existingUser = userService.findByEmail(email).orElse(null);
        if (existingUser != null && bCryptPasswordEncoder.matches(password, existingUser.getPassword())) {
            return ResponseEntity.ok(existingUser);
        } else {
            return ResponseEntity.status(401).body("Invalid email or password");
        }
    }
}
