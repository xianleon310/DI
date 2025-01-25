package com.example.firebase2ev.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.firebase2ev.repositories.UserRepository;

public class RegisterViewModel extends ViewModel {
    private UserRepository repository;
    private MutableLiveData<String> errorMessage = new MutableLiveData<>();
    private MutableLiveData<Boolean> isRegistered = new MutableLiveData<>();

    public RegisterViewModel() {
        repository = new UserRepository();
    }

    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }

    public LiveData<Boolean> getIsRegistered() {
        return isRegistered;
    }

    public void register(String fullName, String email, String password, String confirmPassword,
                         String phone, String address) {
        if (!validateInput(fullName, email, password, confirmPassword, phone, address)) {
            return;
        }

        repository.registerUser(fullName, email, password, phone, address)
                .addOnSuccessListener(authResult -> isRegistered.setValue(true))
                .addOnFailureListener(e -> errorMessage.setValue(e.getMessage()));
    }

    private boolean validateInput(String fullName, String email, String password,
                                  String confirmPassword, String phone, String address) {
        if (fullName.isEmpty() || email.isEmpty() || password.isEmpty() ||
                confirmPassword.isEmpty() || phone.isEmpty() || address.isEmpty()) {
            errorMessage.setValue("Todos los campos son obligatorios");
            return false;
        }
        if (!password.equals(confirmPassword)) {
            errorMessage.setValue("Las contraseñas no coinciden");
            return false;
        }
        return true;
    }
}