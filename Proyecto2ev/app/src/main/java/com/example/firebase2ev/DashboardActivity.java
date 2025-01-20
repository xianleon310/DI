package com.example.firebase2ev;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.Random;

public class DashboardActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private ImageView imageView;
    private TextView titleText;
    private TextView descriptionText;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        mAuth = FirebaseAuth.getInstance();
        DatabaseReference database = FirebaseDatabase.getInstance().getReference();

        // Inicializar vistas
        imageView = findViewById(R.id.imagen);
        titleText = findViewById(R.id.titulo);
        descriptionText = findViewById(R.id.descripcion);
        Button logoutButton = findViewById(R.id.logoutButton);
        //Genera número aleatorio para que al iniciar sesión se inicie uno de los objetos al azar
        Random random = new Random();
        int numeroAleatorio = random.nextInt(4) + 1;
        database.child("videojuegos").child("videojuego_"+numeroAleatorio).get()
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful() && task.getResult().exists()) {
                        DataSnapshot snapshot = task.getResult();

                        // Obtener datos
                        String name = snapshot.child("name").getValue(String.class);
                        String desc = snapshot.child("desc").getValue(String.class);
                        String url = snapshot.child("url").getValue(String.class);

                        // Actualizar UI
                        titleText.setText(name);
                        descriptionText.setText(desc);

                        // Cargar imagen usando Glide
                        Glide.with(this)
                                .load(url)
                                .fitCenter()
                                .override(800, 600)
                                .into(imageView);
                    } else {
                        Toast.makeText(DashboardActivity.this,
                                "Error al obtener datos del videojuego",
                                Toast.LENGTH_SHORT).show();
                    }
                });

        // Configurar el botón de Logout
        logoutButton.setOnClickListener(v -> {
            mAuth.signOut();
            Intent intent = new Intent(DashboardActivity.this, LoginActivity.class);
            intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK);
            startActivity(intent);
            finish();
        });
    }
}