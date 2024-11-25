package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;

import com.squareup.picasso.Picasso;

public class InicioFragment extends Fragment {

    public InicioFragment() {
        // Required empty public constructor
    }

    public static InicioFragment newInstance(String param1, String param2) {
        InicioFragment fragment = new InicioFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_inicio, container, false);

        // Configuración del botón para navegar al detalle
        Button botonNavegacion = view.findViewById(R.id.btn_navigate_to_detail);
        botonNavegacion.setOnClickListener(v -> {
            Intent intent = new Intent(getActivity(), DetailActivity.class);
            startActivity(intent);
        });

        // Configuración de la imagen usando Picasso
        ImageView imageView = view.findViewById(R.id.imagen);
        Picasso.get()
                .load(R.drawable.pikachu) // Usa el recurso drawable de Pikachu
                .transform(new CircleTransform()) // Si tienes una transformación circular
                .into(imageView);

        return view;
    }
}
