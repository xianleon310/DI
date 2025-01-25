package com.example.firebase2ev.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.firebase2ev.models.Game;
import com.example.firebase2ev.repositories.GameRepository;
import java.util.List;

public class GameViewModel extends ViewModel {
    private GameRepository repository;
    private MutableLiveData<Game> selectedGame = new MutableLiveData<>();
    private LiveData<List<Game>> games;

    public GameViewModel() {
        repository = new GameRepository();
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
}