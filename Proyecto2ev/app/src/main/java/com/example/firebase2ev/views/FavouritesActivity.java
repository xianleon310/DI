package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.firebase2ev.R;
import com.example.firebase2ev.adapters.GameAdapter;
import com.example.firebase2ev.viewmodels.GameViewModel;

public class FavouritesActivity extends AppCompatActivity {
    private GameViewModel viewModel;
    private GameAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_favourites);

        // Inicializar ViewModel
        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        // Configurar RecyclerView
        RecyclerView recyclerView = findViewById(R.id.favouritesRecyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        adapter = new GameAdapter(game -> {
            // Click en un juego favorito
            Intent intent = new Intent(this, DetailActivity.class);
            intent.putExtra("videojuego_", game.getId());
            startActivity(intent);
        });
        recyclerView.setAdapter(adapter);

        // Observar favoritos
        viewModel.getFavoriteGames(this).observe(this, games -> {
            adapter.setGames(games);
        });
    }
}