package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import com.example.firebase2ev.R;
import com.example.firebase2ev.fragments.DashboardFragment;
import com.example.firebase2ev.fragments.DetailFragment;
import com.example.firebase2ev.fragments.FavouritesFragment;
import com.example.firebase2ev.models.Game;

public class DashboardActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        // Cargar DashboardFragment como fragment inicial si no hay estado guardado
        if (savedInstanceState == null) {
            loadFragment(new DashboardFragment());
        }
    }

    public void loadFragment(Fragment fragment) {
        getSupportFragmentManager()
                .beginTransaction()
                .replace(R.id.fragmentContainer, fragment)
                .addToBackStack(null)
                .commit();
    }

    public void navigateToDetail(Game game) {
        DetailFragment detailFragment = DetailFragment.newInstance(game.getId());
        loadFragment(detailFragment);
    }

    public void navigateToFavourites() {
        loadFragment(new FavouritesFragment());
    }

    public void logout() {
        startActivity(new Intent(this, LoginActivity.class)
                .addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK));
        finish();
    }
}