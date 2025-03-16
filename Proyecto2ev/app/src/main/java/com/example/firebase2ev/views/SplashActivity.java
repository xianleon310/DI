package com.example.firebase2ev.views;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;

import com.example.firebase2ev.R;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class SplashActivity extends AppCompatActivity {
    private static final int SPLASH_TIME_OUT = 2000;
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Aplicar tema antes de crear la actividad
        SharedPreferences prefs = getSharedPreferences("ThemePrefs", MODE_PRIVATE);
        boolean isDarkMode = prefs.getBoolean("isDarkMode", false);
        if (isDarkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        mAuth = FirebaseAuth.getInstance();

        new Handler().postDelayed(() -> {
            // Verificar si hay un usuario almacenado en SharedPreferences
            SharedPreferences sharedPref = getSharedPreferences("AppConfig", MODE_PRIVATE);
            String userId = sharedPref.getString("userId", null);
            Intent intent;

            if (userId != null) {
                intent = new Intent(SplashActivity.this, DashboardActivity.class);
            } else {
                intent = new Intent(SplashActivity.this, LoginActivity.class);
            }

            startActivity(intent);
            finish();
        }, SPLASH_TIME_OUT);
    }
}