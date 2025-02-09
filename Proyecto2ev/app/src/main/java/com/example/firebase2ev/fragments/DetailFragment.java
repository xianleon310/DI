package com.example.firebase2ev.fragments;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.bumptech.glide.Glide;
import com.example.firebase2ev.R;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.viewmodels.GameViewModel;
import com.google.android.material.appbar.MaterialToolbar;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class DetailFragment extends Fragment {
    private GameViewModel viewModel;
    private ImageView imageView;
    private TextView titleText, descText;
    private FloatingActionButton favoriteFab;
    private String currentGameId;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_detail, container, false);

        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        // Inicializar vistas
        imageView = view.findViewById(R.id.imagen1);
        titleText = view.findViewById(R.id.titulo1);
        descText = view.findViewById(R.id.desc1);
        favoriteFab = view.findViewById(R.id.favoriteFab);

        // Configurar toolbar
        MaterialToolbar toolbar = view.findViewById(R.id.toolbar);
        toolbar.setNavigationOnClickListener(v ->
                requireActivity().getSupportFragmentManager().popBackStack()
        );
        toolbar.inflateMenu(R.menu.detail_menu);
        toolbar.setOnMenuItemClickListener(item -> {
            if (item.getItemId() == R.id.action_share) {
                shareGame();
                return true;
            }
            return false;
        });

        // Obtener el ID del juego de los argumentos
        if (getArguments() != null) {
            currentGameId = getArguments().getString("videojuego_");
            if (currentGameId != null) {
                viewModel.selectGame(currentGameId);
                viewModel.checkIfFavorite(currentGameId);
            }
        }

        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // Observar cambios en el juego seleccionado
        viewModel.getSelectedGame().observe(getViewLifecycleOwner(), game -> {
            titleText.setText(game.getName());
            descText.setText(game.getDesc());
            imageView.setContentDescription("Imagen detallada del juego " + game.getName());

            // También actualizamos el título de la toolbar
            MaterialToolbar toolbar = view.findViewById(R.id.toolbar);
            toolbar.setTitle(game.getName());

            Glide.with(this)
                    .load(game.getUrl())
                    .fitCenter()
                    .override(800, 600)
                    .into(imageView);
        });

        // Observar cambios en el estado de favorito
        viewModel.isFavorite().observe(getViewLifecycleOwner(), isFavorite -> {
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

    private void shareGame() {
        Game game = viewModel.getSelectedGame().getValue();
        if (game != null) {
            Intent shareIntent = new Intent(Intent.ACTION_SEND);
            shareIntent.setType("text/plain");
            shareIntent.putExtra(Intent.EXTRA_TEXT,
                    "¡Mira este juego! " + game.getName() + "\n" + game.getDesc());
            startActivity(Intent.createChooser(shareIntent, "Compartir juego"));
        }
    }

    public static DetailFragment newInstance(String gameId) {
        DetailFragment fragment = new DetailFragment();
        Bundle args = new Bundle();
        args.putString("videojuego_", gameId);
        fragment.setArguments(args);
        return fragment;
    }

}