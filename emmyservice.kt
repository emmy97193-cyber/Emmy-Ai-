package com.boss.emmyai

import android.app.Service
import android.content.Intent
import android.graphics.PixelFormat
import android.net.Uri
import android.os.IBinder
import android.provider.Settings
import android.view.Gravity
import android.view.LayoutInflater
import android.view.MotionEvent
import android.view.View
import android.view.WindowManager
import android.widget.ImageView
import android.widget.Toast

class EmmyService : Service() {

    private lateinit var windowManager: WindowManager
    private lateinit var dragonView: View

    override fun onCreate() {
        super.onCreate()
        windowManager = getSystemService(WINDOW_SERVICE) as WindowManager

        if (!Settings.canDrawOverlays(this)) {
            val intent = Intent(
                Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                Uri.parse("package:$packageName")
            )
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            startActivity(intent)
            return
        }

        dragonView = LayoutInflater.from(this).inflate(R.layout.emmy_overlay, null)

        val params = WindowManager.LayoutParams(
            350,
            350,
            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,
            WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,
            PixelFormat.TRANSLUCENT
        )
        params.gravity = Gravity.TOP or Gravity.END
        params.y = 300

        windowManager.addView(dragonView, params)

        val dragon = dragonView.findViewById<ImageView>(R.id.emmyDragon)

        dragon.animate().translationY(-40f).setDuration(700)
            .withEndAction {
                dragon.animate().translationY(0f).setDuration(700).start()
            }.start()

        dragon.setOnClickListener {
            Toast.makeText(this, "Hi, I'm EMMY-AI", Toast.LENGTH_SHORT).show()
        }

        dragon.setOnTouchListener { _, event ->
            if (event.action == MotionEvent.ACTION_MOVE) {
                params.x = event.rawX.toInt()
                params.y = event.rawY.toInt()
                windowManager.updateViewLayout(dragonView, params)
            }
            true
        }
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
