package com.moflowerlkh.decisionengine.service;

import com.moflowerlkh.decisionengine.domain.entities.User;
import com.moflowerlkh.decisionengine.service.AuthServiceDTO.JwtResponse;
import com.moflowerlkh.decisionengine.service.AuthServiceDTO.LoginRequest;
import com.moflowerlkh.decisionengine.service.AuthServiceDTO.RefreshRequest;
import com.moflowerlkh.decisionengine.service.AuthServiceDTO.TokenRefreshResponse;
import com.moflowerlkh.decisionengine.util.JwtUtil;
import com.moflowerlkh.decisionengine.vo.BaseResponse;
import lombok.val;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
public class AuthService {

    @Autowired
    AuthenticationManager authenticationManager;
    @Autowired
    RedisService redisService;

    public BaseResponse<JwtResponse> signin(LoginRequest loginRequest) {
        Authentication authentication;
        try {
            authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(loginRequest.getUsername(), loginRequest.getPassword()));
        } catch (UsernameNotFoundException e) {
            return new BaseResponse<>(HttpStatus.FORBIDDEN, "没有该用户");
        } catch (BadCredentialsException e) {
            return new BaseResponse<>(HttpStatus.FORBIDDEN, "密码错误");
        } catch (Exception e) {
            return new BaseResponse<>(HttpStatus.INTERNAL_SERVER_ERROR, "未知错误，请联系管理员");
        }
        if (authentication == null) {
            return new BaseResponse<>(HttpStatus.FORBIDDEN, "认证失败");
        }
        // 获取用户认证信息
        LoginUser loginUser = (LoginUser) authentication.getPrincipal();
        User user = loginUser.getUser();
        String token = JwtUtil.createToken(user.getId().toString());
        String refreshToken = JwtUtil.createRefreshToken(user.getId().toString());
        val jwtResponse = new JwtResponse(token, refreshToken, user.getId(), user.getUsername(), user.getGender());
        // 把token存入redis
        redisService.set("pc_token_" + user.getId(), loginUser);
        return new BaseResponse<>(jwtResponse);
    }

    public BaseResponse<String> logout() {
        UsernamePasswordAuthenticationToken authenticationToken = (UsernamePasswordAuthenticationToken) SecurityContextHolder
            .getContext().getAuthentication();
        LoginUser loginUser = (LoginUser) authenticationToken.getPrincipal();
        Long userid = loginUser.getUser().getId();
        redisService.del("pc_token_" + userid);
        return new BaseResponse<>("登出成功");
    }

    public BaseResponse<TokenRefreshResponse> refrehToken(RefreshRequest request) {
        String refreshToken = request.getRefreshToken();
        if (JwtUtil.validate(refreshToken)) {
            String userID = JwtUtil.getUserIDFromToken(refreshToken);
            String token = JwtUtil.createToken(userID);
            TokenRefreshResponse response = new TokenRefreshResponse(token, refreshToken);
            return new BaseResponse<>(response);
        }
        return new BaseResponse<>(HttpStatus.UNAUTHORIZED, "refresh token 已经过期，请重新登录");
    }
}