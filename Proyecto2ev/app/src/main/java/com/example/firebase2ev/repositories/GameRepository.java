package com.example.firebase2ev.repositories;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import com.example.firebase2ev.models.Game;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import java.util.ArrayList;
import java.util.List;

public class GameRepository {
    private DatabaseReference database;

    public GameRepository() {
        database = FirebaseDatabase.getInstance().getReference("videojuegos");
    }

    public Task<DataSnapshot> getGame(String gameId) {
        return database.child(gameId).get();
    }

    public LiveData<List<Game>> getAllGames() {
        MutableLiveData<List<Game>> games = new MutableLiveData<>();

        database.get().addOnCompleteListener(task -> {
            if (task.isSuccessful()) {
                List<Game> gameList = new ArrayList<>();
                for (DataSnapshot snapshot : task.getResult().getChildren()) {
                    Game game = new Game(
                            snapshot.getKey(),
                            snapshot.child("name").getValue(String.class),
                            snapshot.child("desc").getValue(String.class),
                            snapshot.child("url").getValue(String.class)
                    );
                    gameList.add(game);
                }
                games.setValue(gameList);
            }
        });
        return games;
    }
}