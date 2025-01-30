package com.example.firebase2ev.views;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Switch;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
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
    private Switch darkModeSwitch;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Obtener preferencia de Dark Mode antes de cargar la vista
        SharedPreferences sharedPref = getSharedPreferences("AppConfig", MODE_PRIVATE);
        boolean darkMode = sharedPref.getBoolean("darkMode", false);

        if (darkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }

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

        // Configurar Switch para Dark Mode
        darkModeSwitch = findViewById(R.id.darkModeSwitch);
        darkModeSwitch.setChecked(darkMode);

        darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            SharedPreferences.Editor editor = sharedPref.edit();
            editor.putBoolean("darkMode", isChecked);
            editor.apply();

            // Cambia el tema y recarga la actividad
            if (isChecked) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
            } else {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
            }
            recreate(); // Recargar la actividad para aplicar el cambio de tema
        });
    }

    @Override
    public void onGameClick(Game game) {
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("videojuego_", game.getId());
        startActivity(intent);
    }
}
