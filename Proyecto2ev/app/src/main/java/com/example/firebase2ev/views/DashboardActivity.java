package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.bumptech.glide.Glide;
import com.example.firebase2ev.R;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.repositories.UserRepository;
import com.example.firebase2ev.viewmodels.GameViewModel;

public class DashboardActivity extends AppCompatActivity {
    private GameViewModel viewModel;
    private TextView[] titleTexts = new TextView[4];
    private ImageView[] imageViews = new ImageView[4];

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        viewModel = new ViewModelProvider(this).get(GameViewModel.class);
        initializeViews();
        setupObservers();
        setupLogout();
    }

    private void initializeViews() {
        for(int i = 0; i < 4; i++) {
            titleTexts[i] = findViewById(getResources().getIdentifier("titulo" + (i+1), "id", getPackageName()));
            imageViews[i] = findViewById(getResources().getIdentifier("imagen" + (i+1), "id", getPackageName()));

            int index = i;
            titleTexts[i].setOnClickListener(v -> {
                viewModel.selectGame("videojuego_" + (index + 1));
                startActivity(new Intent(this, DetailActivity.class));
            });
        }
    }

    private void setupObservers() {
        viewModel.getGames().observe(this, games -> {
            for(int i = 0; i < Math.min(games.size(), 4); i++) {
                Game game = games.get(i);
                titleTexts[i].setText(game.getName());
                Glide.with(this)
                        .load(game.getUrl())
                        .fitCenter()
                        .override(800, 600)
                        .into(imageViews[i]);
            }
        });
    }

    private void setupLogout() {
        findViewById(R.id.logoutButton).setOnClickListener(v -> {
            new UserRepository().logout();
            startActivity(new Intent(this, LoginActivity.class)
                    .addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK));
            finish();
        });
    }
}