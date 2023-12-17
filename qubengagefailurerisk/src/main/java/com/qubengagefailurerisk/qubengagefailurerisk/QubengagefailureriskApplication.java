package com.qubengagefailurerisk.qubengagefailurerisk;

import java.util.Map;

import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@CrossOrigin(origins = "*")
@SpringBootApplication
public class QubengagefailureriskApplication {

    public static void main(String[] args) {
        SpringApplication.run(QubengagefailureriskApplication.class, args);
    }

    @GetMapping("/check_risk")
    public ResponseEntity<?> checkRisk(@RequestParam double engagementScore, @RequestParam int cutOff) {
        try {

            if (engagementScore*100 < cutOff) {
                return ResponseEntity.ok(Map.of("studentFailureRisk", "Student is at risk of failure."));
            } else {
                return ResponseEntity.ok(Map.of("studentFailureRisk", "Student is not at risk of failure."));
            }
            
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.internalServerError().body(Map.of("error", "An Error Occurred in the Application"));
        }
    }

}
