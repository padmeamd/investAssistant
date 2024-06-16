package com.investAssistant.investAssistant.service;



import com.investAssistant.investAssistant.entity.Recommendation;
import com.investAssistant.investAssistant.repository.RecommendationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RecommendationService {

    @Autowired
    private RecommendationRepository recommendationRepository;

    public List<Recommendation> getAllRecommendations() {
        return recommendationRepository.findAll();
    }

    public Recommendation getRecommendationById(Long id) {
        return recommendationRepository.findById(id).orElse(null);
    }

    public Recommendation createRecommendation(Recommendation recommendation) {
        return recommendationRepository.save(recommendation);
    }

    public Recommendation updateRecommendation(Long id, Recommendation recommendationDetails) {
        Recommendation recommendation = recommendationRepository.findById(id).orElse(null);
        if (recommendation != null) {
            recommendation.setRecommendationDetails(recommendationDetails.getRecommendationDetails());
            recommendation.setUser(recommendationDetails.getUser());
            return recommendationRepository.save(recommendation);
        }
        return null;
    }

    public void deleteRecommendation(Long id) {
        recommendationRepository.deleteById(id);
    }
}
