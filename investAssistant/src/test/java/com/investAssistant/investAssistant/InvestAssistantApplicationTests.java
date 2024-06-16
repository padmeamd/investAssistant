package com.investAssistant.investAssistant;

import com.investAssistant.investAssistant.controller.RecommendationController;
import com.investAssistant.investAssistant.service.UserService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.http.ResponseEntity;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class InvestAssistantApplicationTests {

	@Autowired
	private RecommendationController recommendationController;

	@Autowired
	private UserService userService;

	@Autowired
	private TestRestTemplate restTemplate;

	@LocalServerPort
	private int port;

	@Test
	void contextLoads() {
		assertThat(recommendationController).isNotNull();
		assertThat(userService).isNotNull();
	}

	@Test
	void recommendationsEndpointReturnsOk() {
		String url = "http://localhost:" + port + "/api/recommend";
		ResponseEntity<String> response = restTemplate.postForEntity(url, null, String.class);
		assertThat(response.getStatusCodeValue()).isEqualTo(200);
	}
}
