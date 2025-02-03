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
    private static final String THEME_PREFS = "ThemePrefs";
    private static final String IS_DARK_MODE = "isDarkMode";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Aplicar tema antes de crear la actividad
        applyTheme();

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

        // Inicializar el switch con el valor actual
        darkModeSwitch = findViewById(R.id.darkModeSwitch);
        SharedPreferences prefs = getSharedPreferences(THEME_PREFS, MODE_PRIVATE);
        boolean isDarkMode = prefs.getBoolean(IS_DARK_MODE, false);
        darkModeSwitch.setChecked(isDarkMode);

        // Configurar el listener del switch
        darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            SharedPreferences.Editor editor = getSharedPreferences(THEME_PREFS, MODE_PRIVATE).edit();
            editor.putBoolean(IS_DARK_MODE, isChecked);
            editor.apply();

            // Aplicar el cambio de tema
            if (isChecked) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
            } else {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
            }

            // Recrear la actividad para aplicar el cambio
            recreate();
        });
    }

    private void applyTheme() {
        SharedPreferences prefs = getSharedPreferences(THEME_PREFS, MODE_PRIVATE);
        boolean isDarkMode = prefs.getBoolean(IS_DARK_MODE, false);

        if (isDarkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }
    }

    @Override
    public void onGameClick(Game game) {
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("videojuego_", game.getId());
        startActivity(intent);
    }
}