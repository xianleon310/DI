package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.firebase2ev.R;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class DashboardActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private TextView[] titleTexts=new TextView[4];
    private ImageView[] imageViews=new ImageView[4];
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        mAuth = FirebaseAuth.getInstance();
        DatabaseReference database = FirebaseDatabase.getInstance().getReference();

        // Inicializar vistas
        imageViews[0] = findViewById(R.id.imagen1);
        imageViews[1] = findViewById(R.id.imagen2);
        imageViews[2] = findViewById(R.id.imagen3);
        imageViews[3] = findViewById(R.id.imagen4);
        titleTexts[0] = findViewById(R.id.titulo1);
        titleTexts[1] = findViewById(R.id.titulo2);
        titleTexts[2] = findViewById(R.id.titulo3);
        titleTexts[3] = findViewById(R.id.titulo4);
        Button logoutButton = findViewById(R.id.logoutButton);
        for (int i=0;i<4;i++){
            int index=i;
            titleTexts[i].setOnClickListener(v -> {
                Intent intent = new Intent(DashboardActivity.this, DetailActivity.class);
                // Pasar el índice o ID del videojuego a la siguiente Activity
                intent.putExtra("videojuego_", "videojuego_" + (index + 1));
                startActivity(intent);
            });
            database.child("videojuegos").child("videojuego_"+(i+1)).get()
                    .addOnCompleteListener(task -> {
                        if (task.isSuccessful() && task.getResult().exists()) {
                            DataSnapshot snapshot = task.getResult();

                            // Obtener datos
                            String name = snapshot.child("name").getValue(String.class);
                            String url = snapshot.child("url").getValue(String.class);

                            // Actualizar UI
                            titleTexts[index].setText(name);

                            // Cargar imagen usando Glide
                            Glide.with(this)
                                    .load(url)
                                    .fitCenter()
                                    .override(800, 600)
                                    .into(imageViews[index]);
                        } else {
                            Toast.makeText(DashboardActivity.this,
                                    "Error al obtener datos del videojuego",
                                    Toast.LENGTH_SHORT).show();
                        }
                    });
        }


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