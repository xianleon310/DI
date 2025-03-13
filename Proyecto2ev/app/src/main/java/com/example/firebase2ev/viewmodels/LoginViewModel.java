package com.example.firebase2ev.viewmodels;

import android.content.Context;
import android.content.SharedPreferences;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.firebase2ev.repositories.UserRepository;

public class LoginViewModel extends ViewModel {
    private UserRepository repository;
    private MutableLiveData<String> errorMessage = new MutableLiveData<>();
    private MutableLiveData<Boolean> isLoggedIn = new MutableLiveData<>();

    public LoginViewModel() {
        repository = new UserRepository();
    }

    public LiveData<String> getErrorMessage() {
        return errorMessage;
    }

    public LiveData<Boolean> getIsLoggedIn() {
        return isLoggedIn;
    }

    public void login(String email, String password, Context context) {
        if (email.isEmpty() || password.isEmpty()) {
            errorMessage.setValue("Todos los campos son obligatorios");
            return;
        }

        repository.loginUser(email, password)
                .addOnSuccessListener(authResult -> {
                    // Guardar UID en SharedPreferences
                    SharedPreferences sharedPref = context.getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
                    SharedPreferences.Editor editor = sharedPref.edit();
                    editor.putString("userId", authResult.getUser().getUid());
                    editor.apply();

                    isLoggedIn.setValue(true);
                })
                .addOnFailureListener(e -> errorMessage.setValue(e.getMessage()));
    }
}