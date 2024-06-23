package com.investAssistant.investAssistant.service;

import com.investAssistant.investAssistant.entity.User;
import com.investAssistant.investAssistant.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpMethod;

import java.util.Optional;
import java.util.Map;

/**
 * Service class for handling user-related operations.
 */
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;

    @Autowired
    private RestTemplate restTemplate;

    /**
     * Register a new user.
     *
     * @param user the user to register
     * @return the registered user
     */
    public User registerUser(User user) {
        user.setPassword(bCryptPasswordEncoder.encode(user.getPassword()));
        return userRepository.save(user);
    }

    /**
     * Find a user by email.
     *
     * @param email the email of the user
     * @return an optional containing the found user, or empty if not found
     */
    public Optional<User> findByEmail(String email) {
        return userRepository.findByEmail(email);
    }

    /**
     * Get file content from Python API.
     *
     * @return the content of the file
     */
    public String getFileContent() {
        String url = "http://localhost:5000/api/get-file-content";
        ResponseEntity<Map> response = restTemplate.exchange(url, HttpMethod.GET, null, Map.class);
        Map<String, Object> responseBody = response.getBody();
        return responseBody != null ? (String) responseBody.get("content") : null;
    }
}
