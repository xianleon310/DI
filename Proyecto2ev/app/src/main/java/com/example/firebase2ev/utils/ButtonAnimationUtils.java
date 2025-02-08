package com.example.firebase2ev.utils;

import android.view.animation.Animation;

import com.example.firebase2ev.R;
import com.google.android.material.button.MaterialButton;

public class ButtonAnimationUtils {

    public static void animateButton(MaterialButton button, Runnable onAnimationEnd) {
        // Obtener las coordenadas centrales del botón
        int cx = button.getWidth() / 2;
        int cy = button.getHeight() / 2;

        // Calcular el radio final de la animación
        float radius = (float) Math.hypot(cx, cy);

        // Crear la animación de revelación circular
        Animation anim = android.view.animation.AnimationUtils.loadAnimation(
                button.getContext(), R.anim.circular_reveal);

        // Añadir listener para ejecutar el código después de la animación
        anim.setAnimationListener(new Animation.AnimationListener() {
            @Override
            public void onAnimationStart(Animation animation) {
                button.setEnabled(false);
            }

            @Override
            public void onAnimationEnd(Animation animation) {
                if (onAnimationEnd != null) {
                    onAnimationEnd.run();
                }
                button.setEnabled(true);
            }

            @Override
            public void onAnimationRepeat(Animation animation) {}
        });

        // Iniciar la animación
        button.startAnimation(anim);
    }
}