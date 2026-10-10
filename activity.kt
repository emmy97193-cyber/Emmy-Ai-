package com.emmyguard.app

import android.content.Context
import android.content.pm.PackageManager
import android.os.*
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import org.json.JSONArray
import org.json.JSONObject
import java.net.URL

class MainActivity : AppCompatActivity() {
    lateinit var textView: TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        textView = TextView(this)
        textView.setPadding(40,100,40,40)
        setContentView(textView)

        val battery = getBattery()
        val storage = getStorageFree()
        val apps = scanApps()

        textView.text = "EmmyGuard Scanning...\nBattery: $battery%\nStorage Free: $storage%\nApps: ${apps.size}\n\nChecking AI..."

        Thread {
            try {
                val url = URL("https://YOUR-BACKEND-URL/analyze")
                val json = JSONObject()
                json.put("battery", battery)
                json.put("storage_free_percent", storage)
                val arr = JSONArray()
                apps.take(50).forEach {
                    val o = JSONObject()
                    o.put("name", it.name)
                    o.put("permissions", JSONArray(it.perms))
                    arr.put(o)
                }
                json.put("apps", arr)

                val conn = url.openConnection() as java.net.HttpURLConnection
                conn.requestMethod = "POST"
                conn.setRequestProperty("Content-Type", "application/json")
                conn.doOutput = true
                conn.outputStream.write(json.toString().toByteArray())

                val result = conn.inputStream.bufferedReader().readText()
                runOnUiThread { textView.text = "RESULT:\n$result" }
            } catch(e: Exception) {
                runOnUiThread { textView.text = "Error: ${e.message}\n\nAndroid Scan Results:\nBattery $battery%\n${apps.filter{it.perms.size>10}.take(5).joinToString("\n"){it.name + " -> " + it.perms.size + " perms"}}" }
            }
        }.start()
    }

    fun getBattery(): Int {
        val bm = getSystemService(Context.BATTERY_SERVICE) as BatteryManager
        return bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
    }

    fun getStorageFree(): Int {
        val stat = StatFs(Environment.getDataDirectory().path)
        return ((stat.availableBytes * 100) / stat.totalBytes).toInt()
    }

    data class AppRisk(val name: String, val perms: List<String>)

    fun scanApps(): List<AppRisk> {
        val pm = packageManager
        val apps = pm.getInstalledApplications(PackageManager.GET_META_DATA)
        return apps.map {
            val perms = try {
                pm.getPackageInfo(it.packageName, PackageManager.GET_PERMISSIONS).requestedPermissions?.toList()?: emptyList()
            } catch(e: Exception){ emptyList() }
            AppRisk(it.packageName, perms)
        }
    }
}
