package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.firebase2ev.R;
import com.example.firebase2ev.adapters.GameAdapter;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.repositories.UserRepository;
import com.example.firebase2ev.viewmodels.GameViewModel;

public class DashboardActivity extends AppCompatActivity implements GameAdapter.OnGameClickListener {
    private GameViewModel viewModel;
    private GameAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        // Configurar RecyclerView
        RecyclerView recyclerView = findViewById(R.id.gamesRecyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        adapter = new GameAdapter(this);
        recyclerView.setAdapter(adapter);

        // Observar cambios en la lista de juegos
        viewModel.getGames().observe(this, games -> {
            adapter.setGames(games);
        });

        // Configurar botón de logout
        findViewById(R.id.logoutButton).setOnClickListener(v -> {
            new UserRepository().logout();
            startActivity(new Intent(this, LoginActivity.class)
                    .addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK));
            finish();
        });

        // Configurar botón de favoritos
        findViewById(R.id.favoritesButton).setOnClickListener(v -> {
            startActivity(new Intent(this, FavouritesActivity.class));
        });
    }
    @Override
    public void onGameClick(Game game) {
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("videojuego_", game.getId());
        startActivity(intent);
    }
}