package com.example.firebase2ev.views;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.lifecycle.ViewModelProvider;

import com.example.firebase2ev.R;
import com.example.firebase2ev.viewmodels.LoginViewModel;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.appbar.MaterialToolbar;

public class LoginActivity extends AppCompatActivity {
    private LoginViewModel viewModel;
    private TextInputEditText emailEdit, passwordEdit;

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
        setContentView(R.layout.activity_login);

        viewModel = new ViewModelProvider(this).get(LoginViewModel.class);

        MaterialToolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        emailEdit = findViewById(R.id.emailEditText);
        passwordEdit = findViewById(R.id.passwordEditText);

        MaterialButton loginButton = findViewById(R.id.loginButton);
        MaterialButton registerButton = findViewById(R.id.registerButton);

        loginButton.setOnClickListener(v -> login());
        registerButton.setOnClickListener(v -> startActivity(new Intent(this, RegisterActivity.class)));

        viewModel.getErrorMessage().observe(this, error ->
                Toast.makeText(this, error, Toast.LENGTH_SHORT).show());

        viewModel.getIsLoggedIn().observe(this, isLoggedIn -> {
            if (isLoggedIn) {
                startActivity(new Intent(this, DashboardActivity.class));
                finish();
            }
        });
    }

    private void login() {
        String email = emailEdit.getText() != null ? emailEdit.getText().toString() : "";
        String password = passwordEdit.getText() != null ? passwordEdit.getText().toString() : "";
        viewModel.login(email, password);
    }
}