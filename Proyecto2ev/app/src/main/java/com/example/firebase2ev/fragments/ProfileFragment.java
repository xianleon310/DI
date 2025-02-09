package com.example.firebase2ev.fragments;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;

import com.example.firebase2ev.R;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.switchmaterial.SwitchMaterial;
import com.google.android.material.textfield.TextInputEditText;
import com.google.firebase.auth.AuthCredential;
import com.google.firebase.auth.EmailAuthProvider;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

public class ProfileFragment extends Fragment {

    private TextInputEditText currentPasswordEdit, newPasswordEdit;
    private SwitchMaterial darkModeSwitch;
    private MaterialButton changePasswordButton;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_profile, container, false);

        currentPasswordEdit = view.findViewById(R.id.currentPasswordEditText);
        newPasswordEdit = view.findViewById(R.id.newPasswordEditText);
        darkModeSwitch = view.findViewById(R.id.darkModeSwitch);
        changePasswordButton = view.findViewById(R.id.changePasswordButton);

        // Configurar estado inicial del switch de modo oscuro
        SharedPreferences prefs = requireActivity().getSharedPreferences("ThemePrefs", Context.MODE_PRIVATE);
        boolean isDarkMode = prefs.getBoolean("isDarkMode", false);
        darkModeSwitch.setChecked(isDarkMode);

        // Listener para cambiar modo oscuro
        darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            SharedPreferences.Editor editor = prefs.edit();
            editor.putBoolean("isDarkMode", isChecked);
            editor.apply();

            if (isChecked) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
            } else {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
            }

            requireActivity().recreate();
        });

        // Listener para cambiar contraseña
        changePasswordButton.setOnClickListener(v -> changePassword());

        return view;
    }

    private void changePassword() {
        String currentPassword = currentPasswordEdit.getText() != null ?
                currentPasswordEdit.getText().toString() : "";
        String newPassword = newPasswordEdit.getText() != null ?
                newPasswordEdit.getText().toString() : "";

        if (currentPassword.isEmpty() || newPassword.isEmpty()) {
            Toast.makeText(getContext(), R.string.all_fields_required, Toast.LENGTH_SHORT).show();
            return;
        }

        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        if (user != null && user.getEmail() != null) {
            AuthCredential credential = EmailAuthProvider.getCredential(user.getEmail(), currentPassword);

            user.reauthenticate(credential).addOnCompleteListener(task -> {
                if (task.isSuccessful()) {
                    user.updatePassword(newPassword).addOnCompleteListener(updateTask -> {
                        if (updateTask.isSuccessful()) {
                            Toast.makeText(getContext(), R.string.password_updated, Toast.LENGTH_SHORT).show();
                            currentPasswordEdit.setText("");
                            newPasswordEdit.setText("");
                        } else {
                            Toast.makeText(getContext(), R.string.password_update_error, Toast.LENGTH_SHORT).show();
                        }
                    });
                } else {
                    Toast.makeText(getContext(), R.string.current_password_error, Toast.LENGTH_SHORT).show();
                }
            });
        }
    }
}