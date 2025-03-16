package com.example.firebase2ev.fragments;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

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
import com.example.firebase2ev.views.DashboardActivity;
import com.google.android.material.appbar.MaterialToolbar;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.ArrayList;

public class DashboardFragment extends Fragment implements GameAdapter.OnGameClickListener {
    private GameViewModel viewModel;
    private GameAdapter adapter;
    private boolean isDarkMode;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_dashboard, container, false);

        viewModel = new ViewModelProvider(this).get(GameViewModel.class);

        // Configurar toolbar
        MaterialToolbar toolbar = view.findViewById(R.id.toolbar);

        // Inflar el menú programáticamente
        toolbar.inflateMenu(R.menu.dashboard_menu);

        toolbar.setOnMenuItemClickListener(item -> {
            int id = item.getItemId();
            if (id == R.id.action_favorites) {
                ((DashboardActivity) requireActivity()).navigateToFavourites();
                return true;
            } else if (id == R.id.action_profile) {
                ((DashboardActivity) requireActivity()).navigateToProfile();
                return true;
            } else if (id == R.id.action_logout) {
                ((DashboardActivity) requireActivity()).logout();
                return true;
            }else if (id==R.id.action_clear_favorites){
                clearAllFavorites();
                return true;
            }
            return false;
        });
        RecyclerView recyclerView = view.findViewById(R.id.gamesRecyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        adapter = new GameAdapter(this);
        recyclerView.setAdapter(adapter);

        return view;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        viewModel.getNonFavoriteGames().observe(getViewLifecycleOwner(), games -> {
            adapter.setGames(games);

        });
    }

    @Override
    public void onGameClick(Game game) {
        ((DashboardActivity) requireActivity()).navigateToDetail(game);
    }

    private void clearAllFavorites() {
        viewModel.clearAllFavorites().addOnCompleteListener(task -> {
            if (task.isSuccessful()) {
                // Mostrar mensaje de éxito
                Toast.makeText(getContext(), "Favoritos eliminados correctamente", Toast.LENGTH_SHORT).show();
            } else {
                // Mostrar mensaje de error
                Toast.makeText(getContext(), "Error al eliminar favoritos", Toast.LENGTH_SHORT).show();
            }
        });
    }

}