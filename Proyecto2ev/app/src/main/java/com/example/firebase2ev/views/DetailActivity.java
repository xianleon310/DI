package com.example.firebase2ev.views;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.bumptech.glide.Glide;
import com.example.firebase2ev.R;
import com.example.firebase2ev.viewmodels.GameViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class DetailActivity extends AppCompatActivity {
    private GameViewModel viewModel;
    private ImageView imageView;
    private TextView titleText, descText;
    private FloatingActionButton favoriteFab;
    private String currentGameId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_detail);

        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        imageView = findViewById(R.id.imagen1);
        titleText = findViewById(R.id.titulo1);
        descText = findViewById(R.id.desc1);
        favoriteFab = findViewById(R.id.favoriteFab);

        // Obtener el ID una sola vez
        currentGameId = getIntent().getStringExtra("videojuego_");

        // Iniciar la carga del juego y verificar favoritos
        viewModel.selectGame(currentGameId);
        viewModel.checkIfFavorite(currentGameId);

        // Observar los cambios en el juego seleccionado
        viewModel.getSelectedGame().observe(this, game -> {
            titleText.setText(game.getName());
            descText.setText(game.getDesc());

            Glide.with(this)
                    .load(game.getUrl())
                    .fitCenter()
                    .override(800, 600)
                    .into(imageView);
        });

        // Observar cambios en el estado de favorito
        viewModel.isFavorite().observe(this, isFavorite -> {
            favoriteFab.setImageResource(isFavorite ?
                    R.drawable.ic_favorite : R.drawable.ic_favorite_border);
        });

        // Configurar el click del FAB
        favoriteFab.setOnClickListener(v -> {
            Boolean currentFavorite = viewModel.isFavorite().getValue();
            if (currentFavorite != null && currentFavorite) {
                viewModel.removeFromFavorites(currentGameId);
            } else {
                viewModel.addToFavorites(currentGameId);
            }
        });
    }
}