package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.firebase2ev.R;
import com.example.firebase2ev.viewmodels.RegisterViewModel;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;
import java.util.Map;

public class RegisterActivity extends AppCompatActivity {
    //ANTES
    //private FirebaseAuth mAuth;
    //private DatabaseReference database;

    //AHORA
    private RegisterViewModel viewModel;
    private EditText fullNameEdit, emailEdit, passwordEdit, confirmPasswordEdit, phoneEdit, addressEdit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        //ANTES
        //mAuth = FirebaseAuth.getInstance();
        //database = FirebaseDatabase.getInstance().getReference();

        //AHORA
        viewModel = new ViewModelProvider(this).get(RegisterViewModel.class);
        initializeViews();
        setupObservers();


        findViewById(R.id.registerButton).setOnClickListener(v -> registerUser());
    }
    //NOVO
    private void initializeViews() {
        fullNameEdit = findViewById(R.id.fullNameEditText);
        emailEdit = findViewById(R.id.emailEditText);
        passwordEdit = findViewById(R.id.passwordEditText);
        confirmPasswordEdit = findViewById(R.id.confirmPasswordEditText);
        phoneEdit = findViewById(R.id.phoneEditText);
        addressEdit = findViewById(R.id.addressEditText);
    }
    //NOVO
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
        //ANTES
        /*String fullName = ((EditText) findViewById(R.id.fullNameEditText)).getText().toString();
        String email = ((EditText) findViewById(R.id.emailEditText)).getText().toString();
        String password = ((EditText) findViewById(R.id.passwordEditText)).getText().toString();
        String confirmPassword = ((EditText) findViewById(R.id.confirmPasswordEditText)).getText().toString();
        String phone = ((EditText) findViewById(R.id.phoneEditText)).getText().toString();
        String address = ((EditText) findViewById(R.id.addressEditText)).getText().toString();
        if (fullName.isEmpty() || email.isEmpty() || password.isEmpty() || confirmPassword.isEmpty() || phone.isEmpty() || address.isEmpty()){
            Toast.makeText(this,"Cubre todos los campos.",Toast.LENGTH_SHORT).show();
            return;
        }
        if (!password.equals(confirmPassword)) {
            Toast.makeText(this, "Las contraseñas no coinciden.", Toast.LENGTH_SHORT).show();
            return;
        }

        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {
                        String userId = mAuth.getCurrentUser().getUid();
                        DatabaseReference userRef = database.child("users").child(userId);

                        // Crear un mapa con los datos del usuario
                        Map<String, Object> user = new HashMap<>();
                        user.put("fullName", fullName);
                        user.put("phone", phone);
                        user.put("address", address);

                        // Guardar los datos en la base de datos
                        userRef.setValue(user)
                                .addOnCompleteListener(saveTask -> {
                                    if (saveTask.isSuccessful()) {
                                        Toast.makeText(RegisterActivity.this, "Registro exitoso.", Toast.LENGTH_SHORT).show();
                                        Intent intent = new Intent(RegisterActivity.this, DashboardActivity.class);
                                        startActivity(intent);
                                        finish();
                                    } else {
                                        Toast.makeText(RegisterActivity.this, "Error al guardar los datos.", Toast.LENGTH_SHORT).show();
                                    }
                                });
                    } else {
                        Toast.makeText(RegisterActivity.this, "Error en el registro: " + task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
    }*/
