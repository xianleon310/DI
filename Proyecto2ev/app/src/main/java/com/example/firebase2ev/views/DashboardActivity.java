package com.example.firebase2ev.views;

import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import com.example.firebase2ev.R;
import com.example.firebase2ev.fragments.DashboardFragment;
import com.example.firebase2ev.fragments.DetailFragment;
import com.example.firebase2ev.fragments.FavouritesFragment;
import com.example.firebase2ev.fragments.ProfileFragment;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.repositories.UserRepository;

public class DashboardActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        if (savedInstanceState == null) {
            loadFragment(new DashboardFragment(), false);
        }
    }

    public void loadFragment(Fragment fragment, boolean addToBackStack) {
        FragmentTransaction transaction = getSupportFragmentManager()
                .beginTransaction()
                .setCustomAnimations(
                        R.anim.slide_in_right,
                        R.anim.slide_out_left,
                        android.R.anim.slide_in_left,
                        android.R.anim.slide_out_right
                )
                .replace(R.id.fragmentContainer, fragment);

        if (addToBackStack) {
            transaction.addToBackStack(null);
        }

        transaction.commit();
    }

    public void navigateToDetail(Game game) {
        loadFragment(DetailFragment.newInstance(game.getId()), true);
    }

    public void navigateToFavourites() {
        loadFragment(new FavouritesFragment(), true);
    }

    public void navigateToProfile() {
        loadFragment(new ProfileFragment(), true);
    }

    public void logout() {
        new UserRepository().logout();
        startActivity(new Intent(this, LoginActivity.class)
                .addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_NEW_TASK));
        finish();
    }

    @Override
    public void onBackPressed() {
        if (getSupportFragmentManager().getBackStackEntryCount() > 0) {
            getSupportFragmentManager().popBackStack();
        } else {
            super.onBackPressed();
        }
    }
}