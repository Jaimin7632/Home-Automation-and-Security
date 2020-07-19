package com.example.jaimin.myiotapp;

import android.annotation.TargetApi;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.support.annotation.Nullable;
import android.support.v4.app.NotificationCompat;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by Jaimin on 8/10/2017.
 */
public class myService extends Service {


    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
    @Override
    public void onCreate() {
     }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {


        final long period = 3000;
try {
    new Timer().schedule(new TimerTask() {
        @Override
        public void run() {
            checkNotification();

        }
    }, 0, period);
}
catch (Exception e){
    startService(new Intent(getBaseContext(), myService.class));
}

        return START_STICKY;
    }

    public void checkNotification(){
        RequestQueue queue = Volley.newRequestQueue(getApplicationContext());
        StringRequest stringRequest = new StringRequest(Request.Method.GET,"http://autohome.srpec.org.in/notify1.php",
                new Response.Listener<String>() {
                    @TargetApi(26)
                    @Override
                    public void onResponse(String response) {
                        try {
                            JSONObject obj = new JSONObject(response);

                            String s =obj.getString("msg");
                            if(!s.equals("")){
                                PendingIntent resultPendingIntent =
                                        PendingIntent.getActivity(
                                                getApplicationContext(),
                                                0,
                                                new Intent(getApplicationContext(), Main2Activity.class),
                                                PendingIntent.FLAG_UPDATE_CURRENT
                                        );
                                NotificationCompat.Builder mBuilder =
                                        new NotificationCompat.Builder(getApplicationContext())
                                                .setSmallIcon(R.drawable.as)
                                                .setContentTitle("Warning")
                                                .setContentText(s);
                                mBuilder.setVibrate(new long[] { 0, 1000, 1000, 1000, 1000,1000, 1000,1000, 1000 });

                                int mNotificationId = 001;
// Gets an instance of the NotificationManager service
                                NotificationManager mNotifyMgr =
                                        (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
                                mBuilder.setContentIntent(resultPendingIntent);
// Builds the notification and issues it.
                                mNotifyMgr.notify(mNotificationId, mBuilder.build());

                            }
                        } catch (JSONException e) {
                            e.printStackTrace();

                        }

                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {


                    }});
        queue.add(stringRequest);

    }

}
