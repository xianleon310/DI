package com.example.firebase2ev.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.repositories.GameRepository;
import com.example.firebase2ev.repositories.UserRepository;

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
        userRepository.addToFavorites(gameId);
    }

    public void removeFromFavorites(String gameId) {
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
}