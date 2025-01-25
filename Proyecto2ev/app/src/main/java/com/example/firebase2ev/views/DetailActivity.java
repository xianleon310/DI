package com.example.firebase2ev.views;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.bumptech.glide.Glide;
import com.example.firebase2ev.R;
import com.example.firebase2ev.viewmodels.GameViewModel;

public class DetailActivity extends AppCompatActivity {
    private GameViewModel viewModel;
    private ImageView imageView;
    private TextView titleText, descText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_detail);

        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        imageView = findViewById(R.id.imagen1);
        titleText = findViewById(R.id.titulo1);
        descText = findViewById(R.id.desc1);

        String videojuegoId = getIntent().getStringExtra("videojuego_");
        viewModel.selectGame(videojuegoId);

        viewModel.getSelectedGame().observe(this, game -> {
            titleText.setText(game.getName());
            descText.setText(game.getDesc());

            Glide.with(this)
                    .load(game.getUrl())
                    .fitCenter()
                    .override(800, 600)
                    .into(imageView);
        });
    }
}