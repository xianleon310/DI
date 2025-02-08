package com.example.firebase2ev.fragments;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Switch;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.firebase2ev.R;
import com.example.firebase2ev.adapters.GameAdapter;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.repositories.UserRepository;
import com.example.firebase2ev.viewmodels.GameViewModel;
import com.example.firebase2ev.views.DetailActivity;
import com.example.firebase2ev.views.FavouritesActivity;
import com.example.firebase2ev.views.LoginActivity;

public class DashboardFragment extends Fragment implements GameAdapter.OnGameClickListener {
    private GameViewModel viewModel;
    private GameAdapter adapter;
    private Switch darkModeSwitch;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_dashboard, container, false);

        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        // Configurar RecyclerView
        RecyclerView recyclerView = view.findViewById(R.id.gamesRecyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        adapter = new GameAdapter(this);
        recyclerView.setAdapter(adapter);

        // Configurar botones
        Button logoutButton = view.findViewById(R.id.logoutButton);
        logoutButton.setOnClickListener(v -> {
            new UserRepository().logout();
            startActivity(new Intent(getActivity(), LoginActivity.class)
                    .addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK));
            getActivity().finish();
        });

        Button favoritesButton = view.findViewById(R.id.favoritesButton);
        favoritesButton.setOnClickListener(v -> {
            // Aquí cambiaremos esto para usar Fragment Transaction más adelante
            startActivity(new Intent(getActivity(), FavouritesActivity.class));
        });

        // Configurar switch de tema oscuro
        darkModeSwitch = view.findViewById(R.id.darkModeSwitch);
        SharedPreferences prefs = requireActivity().getSharedPreferences("ThemePrefs", getActivity().MODE_PRIVATE);
        boolean isDarkMode = prefs.getBoolean("isDarkMode", false);
        darkModeSwitch.setChecked(isDarkMode);

        darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            SharedPreferences.Editor editor = prefs.edit();
            editor.putBoolean("isDarkMode", isChecked);
            editor.apply();

            if (isChecked) {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
            } else {
                AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
            }

            requireActivity().recreate();
        });

        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // Observar cambios en la lista de juegos
        viewModel.getGames().observe(getViewLifecycleOwner(), games -> {
            adapter.setGames(games);
        });
    }

    @Override
    public void onGameClick(Game game) {
        // Aquí cambiaremos esto para usar Fragment Transaction más adelante
        Intent intent = new Intent(getActivity(), DetailActivity.class);
        intent.putExtra("videojuego_", game.getId());
        startActivity(intent);
    }
}