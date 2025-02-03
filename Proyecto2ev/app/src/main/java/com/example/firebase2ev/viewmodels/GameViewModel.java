package com.example.firebase2ev.viewmodels;

import androidx.lifecycle.LifecycleOwner;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.repositories.GameRepository;
import com.example.firebase2ev.repositories.UserRepository;

import java.util.ArrayList;
import java.util.List;

public class GameViewModel extends ViewModel {
    private GameRepository repository;
    private MutableLiveData<Game> selectedGame = new MutableLiveData<>();
    private LiveData<List<Game>> games;
    private UserRepository userRepository;
    private MutableLiveData<Boolean> isFavorite = new MutableLiveData<>();

    public GameViewModel() {
        repository = new GameRepository();
        userRepository = new UserRepository();
        games = repository.getAllGames();
    }

    public LiveData<List<Game>> getGames() {
        return games;
    }

    public void selectGame(String gameId) {
        repository.getGame(gameId).addOnSuccessListener(snapshot -> {
            Game game = new Game(
                    snapshot.getKey(),
                    snapshot.child("name").getValue(String.class),
                    snapshot.child("desc").getValue(String.class),
                    snapshot.child("url").getValue(String.class)
            );
            selectedGame.setValue(game);
        });
    }

    public LiveData<Game> getSelectedGame() {
        return selectedGame;
    }

    public void addToFavorites(String gameId) {
        isFavorite.postValue(true);
        userRepository.addToFavorites(gameId);
    }

    public void removeFromFavorites(String gameId) {
        isFavorite.postValue(false);
        userRepository.removeFromFavorites(gameId);
    }

    public LiveData<Boolean> isFavorite() {
        return isFavorite;
    }

    public void checkIfFavorite(String gameId) {
        userRepository.isFavorite(gameId).addOnSuccessListener(snapshot -> {
            isFavorite.setValue(snapshot.exists());
        });
    }

    public LiveData<List<Game>> getFavoriteGames(LifecycleOwner lifecycleOwner) {
        MutableLiveData<List<Game>> result = new MutableLiveData<>();

        userRepository.getFavoriteGames().observe(lifecycleOwner, favoriteIds -> {
            if (favoriteIds != null && !favoriteIds.isEmpty()) {
                List<Game> favorites = new ArrayList<>();

                // Obtener los detalles de cada juego favorito
                for (String gameId : favoriteIds) {
                    repository.getGame(gameId).addOnSuccessListener(snapshot -> {
                        Game game = new Game(
                                snapshot.getKey(),
                                snapshot.child("name").getValue(String.class),
                                snapshot.child("desc").getValue(String.class),
                                snapshot.child("url").getValue(String.class)
                        );
                        favorites.add(game);
                        result.setValue(favorites);
                    });
                }
            } else {
                result.setValue(new ArrayList<>());
            }
        });

        return result;
    }
}