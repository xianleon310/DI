package com.example.firebase2ev.repositories;

import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;
import java.util.Map;

public class UserRepository {
    private FirebaseAuth mAuth;
    private DatabaseReference database;

    public UserRepository() {
        mAuth = FirebaseAuth.getInstance();
        database = FirebaseDatabase.getInstance().getReference();
    }

    public UserRepository(FirebaseAuth mAuth, DatabaseReference database) {
        this.mAuth = mAuth;
        this.database = database;
    }

    public Task<AuthResult> registerUser(String fullName, String email, String password, String phone, String address) {
        return mAuth.createUserWithEmailAndPassword(email, password)
                .addOnSuccessListener(result -> {
                    String userId = result.getUser().getUid();
                    Map<String, Object> user = new HashMap<>();
                    user.put("fullName", fullName);
                    user.put("email", email);
                    user.put("phone", phone);
                    user.put("address", address);

                    database.child("users").child(userId).setValue(user);
                });
    }

    public Task<AuthResult> loginUser(String email, String password) {
        return mAuth.signInWithEmailAndPassword(email, password);
    }

    public void logout() {
        mAuth.signOut();
    }
    
    // Método para añadir a favoritos
    public Task<Void> addToFavorites(String gameId) {
        String userId = mAuth.getCurrentUser().getUid();
        return database.child("users")
                .child(userId)
                .child("favoritos")
                .child(gameId)
                .setValue(true);
    }

    // Método para eliminar de favoritos
    public Task<Void> removeFromFavorites(String gameId) {
        String userId = mAuth.getCurrentUser().getUid();
        return database.child("users")
                .child(userId)
                .child("favoritos")
                .child(gameId)
                .removeValue();
    }

    // Método para verificar si un juego está en favoritos
    public Task<DataSnapshot> isFavorite(String gameId) {
        String userId = mAuth.getCurrentUser().getUid();
        return database.child("users")
                .child(userId)
                .child("favoritos")
                .child(gameId)
                .get();
    }
}