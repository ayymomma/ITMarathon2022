package com.otp.otpserver.services.impl;

import com.otp.otpserver.model.dao.LoginTokenRepository;
import com.otp.otpserver.model.dao.UserRepository;
import com.otp.otpserver.model.exception.HttpResponseException;
import com.otp.otpserver.model.pojo.dto.user.UserRequest;
import com.otp.otpserver.model.pojo.dto.user.UserResponse;
import com.otp.otpserver.model.pojo.dto.user.UserWithToken;
import com.otp.otpserver.model.pojo.erd.LoginToken;
import com.otp.otpserver.model.pojo.erd.User;
import com.otp.otpserver.services.UserService;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

import java.sql.Timestamp;
import java.util.Optional;
import java.util.UUID;

@Service
public class UserServiceImpl implements UserService {
    private final UserRepository userRepository;
    private final LoginTokenRepository loginTokenRepository;

    public UserServiceImpl(UserRepository userRepository, LoginTokenRepository loginTokenRepository) {
        this.userRepository = userRepository;
        this.loginTokenRepository = loginTokenRepository;
    }

    @Override
    public UserWithToken login(String username, String password) {
        User findUser = userRepository.findByUsernameAndPassword(username, password);

        if(findUser == null)
            throw new HttpResponseException("Wrong credentials.", HttpStatus.NOT_FOUND);

        // A user was found, create token
        LoginToken token = new LoginToken();

        UUID uuid = UUID.randomUUID();
        token.setToken(uuid.toString());
        token.setUserId(findUser.getUserId());
        token.setTimestamp(new Timestamp(System.currentTimeMillis()));

        LoginToken saved = loginTokenRepository.save(token);

        UserWithToken tokenUser = new UserWithToken();
        tokenUser.setUsername(findUser.getUsername());
        tokenUser.setToken(token.getToken());
        tokenUser.setRole(findUser.getRole());

        return tokenUser;
    }

    @Override
    public UserResponse register(UserRequest userRequest) {
        User existing = userRepository.findByUsername(userRequest.getUsername());

        if(existing != null)
            throw new HttpResponseException("User already exists!", HttpStatus.CONFLICT);

        if(!userRequest.getPassword().equals(userRequest.getRepeatPassword()))
            throw new HttpResponseException("Passwords are not the same!", HttpStatus.CONFLICT);

        User newUser = new User();
        newUser.setRole("USER");
        newUser.setUsername(userRequest.getUsername());
        newUser.setPassword(userRequest.getPassword());
        newUser.setUserId(null);

        User saved = userRepository.save(newUser);

        return new UserResponse(saved);
    }

    @Override
    public UserResponse logout(String token){
        Optional<LoginToken> exists = loginTokenRepository.findById(token);

        if(exists.isEmpty())
            throw new HttpResponseException("Token was not found", HttpStatus.NOT_FOUND);

        LoginToken fromDb = exists.get();
        loginTokenRepository.delete(fromDb);

        Optional<User> user = userRepository.findById(fromDb.getUserId());

        if(user.isEmpty())
            throw new HttpResponseException("User was not found", HttpStatus.NOT_FOUND);

        return new UserResponse(user.get());
    }

    @Override
    public User validateToken(String token) {
        Optional<LoginToken> tokenFound = loginTokenRepository.findById(token);
        if(tokenFound.isEmpty())
            throw new HttpResponseException("Invalid token! Unauthorized!", HttpStatus.UNAUTHORIZED);

        Optional<User> found = userRepository.findById(tokenFound.get().getUserId());
        if(found.isEmpty())
            throw new HttpResponseException("User not exist!", HttpStatus.NOT_FOUND);

        return found.get();
    }

    @Override
    public User getUserById(Integer userId) {
        Optional<User> user = userRepository.findById(userId);

        if(user.isEmpty()) return null;
        return user.get();
    }


}
