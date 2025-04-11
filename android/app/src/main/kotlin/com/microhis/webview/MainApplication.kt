package com.microhis.webview

import io.flutter.app.FlutterApplication
import androidx.multidex.MultiDex
import android.content.Context
import android.webkit.WebView
import android.os.Build
import android.os.StrictMode

class MainApplication : FlutterApplication() {
    override fun onCreate() {
        super.onCreate()
        
        // 启用 WebView 调试
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
            WebView.setWebContentsDebuggingEnabled(true)
        }
        
        // 配置 StrictMode
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            StrictMode.setVmPolicy(StrictMode.VmPolicy.Builder()
                .detectAll()
                .penaltyLog()
                .build())
        }
        
        try {
            // 预初始化 WebView
            WebView(this).destroy()
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    override fun attachBaseContext(base: Context) {
        super.attachBaseContext(base)
        MultiDex.install(this)
    }
} 