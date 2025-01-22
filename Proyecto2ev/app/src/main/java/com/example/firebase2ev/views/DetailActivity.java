package com.example.firebase2ev.views;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.firebase2ev.R;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class DetailActivity extends AppCompatActivity {
    private ImageView imageView;
    private TextView titleText;
    private TextView descText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_detail);
        // Inicializar vistas
        imageView = findViewById(R.id.imagen1);
        titleText = findViewById(R.id.titulo1);
        descText = findViewById(R.id.desc1);

        // Obtener el ID del videojuego
        String videojuegoId = getIntent().getStringExtra("videojuego_");
        System.out.println(videojuegoId);
        // Obtener referencia a la base de datos
        DatabaseReference database = FirebaseDatabase.getInstance().getReference();
        database.child("videojuegos").child(videojuegoId).get()
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful() && task.getResult().exists()) {
                        DataSnapshot snapshot = task.getResult();

                        // Obtener datos usando los nombres exactos de tu JSON
                        String name = snapshot.child("name").getValue(String.class);
                        String url = snapshot.child("url").getValue(String.class);
                        String desc = snapshot.child("desc").getValue(String.class);

                        // Actualizar UI
                        titleText.setText(name);
                        descText.setText(desc);

                        // Cargar imagen usando Glide
                        Glide.with(this)
                                .load(url)
                                .fitCenter()
                                .override(800, 600)
                                .into(imageView);
                    } else {
                        Toast.makeText(DetailActivity.this,
                                "Error al obtener datos del videojuego",
                                Toast.LENGTH_SHORT).show();
                    }
                });
    }
}