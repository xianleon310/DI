package com.example.firebase2ev.utils;

import android.view.View;

public class LoadingUtils {
    public static void showLoading(View loadingLayout) {
        loadingLayout.setVisibility(View.VISIBLE);
    }

    public static void hideLoading(View loadingLayout) {
        loadingLayout.setVisibility(View.GONE);
    }
}