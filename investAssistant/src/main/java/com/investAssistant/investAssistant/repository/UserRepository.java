package com.investAssistant.investAssistant.repository;



import com.investAssistant.investAssistant.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;
import java.util.UUID;

/**
 * Repository interface for User entity.
 */
public interface UserRepository extends JpaRepository<User, UUID> {

    /**
     * Find a user by email.
     *
     * @param email the email of the user
     * @return an optional containing the found user, or empty if not found
     */
    Optional<User> findByEmail(String email);
}
