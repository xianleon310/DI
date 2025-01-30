package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.firebase2ev.R;
import com.example.firebase2ev.viewmodels.RegisterViewModel;

public class RegisterActivity extends AppCompatActivity {
    private RegisterViewModel viewModel;
    private EditText fullNameEdit, emailEdit, passwordEdit, confirmPasswordEdit, phoneEdit, addressEdit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        viewModel = new ViewModelProvider(this).get(RegisterViewModel.class);
        initializeViews();
        setupObservers();


        findViewById(R.id.registerButton).setOnClickListener(v -> registerUser());
    }

    private void initializeViews() {
        fullNameEdit = findViewById(R.id.fullNameEditText);
        emailEdit = findViewById(R.id.emailEditText);
        passwordEdit = findViewById(R.id.passwordEditText);
        confirmPasswordEdit = findViewById(R.id.confirmPasswordEditText);
        phoneEdit = findViewById(R.id.phoneEditText);
        addressEdit = findViewById(R.id.addressEditText);
    }

    private void setupObservers() {
        viewModel.getErrorMessage().observe(this, error ->
                Toast.makeText(this, error, Toast.LENGTH_SHORT).show());

        viewModel.getIsRegistered().observe(this, isRegistered -> {
            if (isRegistered) {
                startActivity(new Intent(this, DashboardActivity.class));
                finish();
            }
        });
    }

    private void registerUser() {
        viewModel.register(
                fullNameEdit.getText().toString(),
                emailEdit.getText().toString(),
                passwordEdit.getText().toString(),
                confirmPasswordEdit.getText().toString(),
                phoneEdit.getText().toString(),
                addressEdit.getText().toString()
        );
    }
}