package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.firebase2ev.R;
import com.example.firebase2ev.utils.ButtonAnimationUtils;
import com.example.firebase2ev.viewmodels.RegisterViewModel;
import com.google.android.material.appbar.MaterialToolbar;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.textfield.TextInputEditText;

public class RegisterActivity extends AppCompatActivity {
    private RegisterViewModel viewModel;
    private TextInputEditText fullNameEdit, emailEdit, passwordEdit, confirmPasswordEdit,
            phoneEdit, addressEdit;
    private MaterialButton registerButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        viewModel = new ViewModelProvider(this).get(RegisterViewModel.class);

        // Configurar toolbar
        MaterialToolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        toolbar.setNavigationOnClickListener(v -> onBackPressed());

        initializeViews();
        setupObservers();

        registerButton = findViewById(R.id.registerButton);
        registerButton.setOnClickListener(v -> {
            ButtonAnimationUtils.animateButton((MaterialButton) v, this::registerUser);
        });
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
                startActivity(new Intent(this, DashboardActivity.class)
                        .addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK));
                finish();
            }
        });
    }

    private void registerUser() {
        String fullName = fullNameEdit.getText() != null ? fullNameEdit.getText().toString() : "";
        String email = emailEdit.getText() != null ? emailEdit.getText().toString() : "";
        String password = passwordEdit.getText() != null ? passwordEdit.getText().toString() : "";
        String confirmPassword = confirmPasswordEdit.getText() != null ?
                confirmPasswordEdit.getText().toString() : "";
        String phone = phoneEdit.getText() != null ? phoneEdit.getText().toString() : "";
        String address = addressEdit.getText() != null ? addressEdit.getText().toString() : "";

        viewModel.register(fullName, email, password, confirmPassword, phone, address,this);
    }
}