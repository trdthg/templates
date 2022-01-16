package com.moflowerlkh.decisionengine;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import springfox.documentation.oas.annotations.EnableOpenApi;

@SpringBootApplication
@EnableScheduling
@EnableWebMvc
public class DecisionEngineApplication {

    public static void main(String[] args) {
        SpringApplication.run(DecisionEngineApplication.class, args);
    }

}