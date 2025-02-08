package com.example.firebase2ev.fragments;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.firebase2ev.R;
import com.example.firebase2ev.adapters.GameAdapter;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.viewmodels.GameViewModel;
import com.example.firebase2ev.views.DashboardActivity;
import com.example.firebase2ev.views.DetailActivity;

public class FavouritesFragment extends Fragment implements GameAdapter.OnGameClickListener {
    private GameViewModel viewModel;
    private GameAdapter adapter;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_favourites, container, false);

        // Inicializar ViewModel
        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        // Configurar RecyclerView
        RecyclerView recyclerView = view.findViewById(R.id.favouritesRecyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        adapter = new GameAdapter(this);
        recyclerView.setAdapter(adapter);

        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // Observar favoritos
        viewModel.getFavoriteGames(getViewLifecycleOwner()).observe(getViewLifecycleOwner(), games -> {
            adapter.setGames(games);
        });
    }

    @Override
    public void onGameClick(Game game) {
        ((DashboardActivity) requireActivity()).navigateToDetail(game);
    }
}