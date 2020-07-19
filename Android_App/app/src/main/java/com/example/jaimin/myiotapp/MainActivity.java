package com.example.jaimin.myiotapp;

import android.annotation.TargetApi;

import android.app.Activity;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.graphics.Color;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.RelativeLayout;
import android.widget.Switch;
import android.widget.Toast;
import android.widget.ToggleButton;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivity extends Activity {

    ToggleButton t;
    Switch fan,light,ac,projector;
    RelativeLayout r;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        t=(ToggleButton)findViewById(R.id.toggleButton2);
        fan=(Switch)findViewById(R.id.switch2);
        light=(Switch)findViewById(R.id.switch3);
        ac=(Switch)findViewById(R.id.switch4);
        projector=(Switch)findViewById(R.id.switch5);
        startService(new Intent(getBaseContext(), myService.class));
        setState();
        final long period = 5000;
        new Timer().schedule(new TimerTask() {
            @Override
            public void run() {
                setState();

            }
        }, 0, period);


        t.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (t.isChecked()) {
                    callFile("autowork.php");
                    fan.setClickable(false);
                    light.setClickable(false);
                    ac.setClickable(false);
                    projector.setClickable(false);
                } else {
                    callFile("manualwork.php");
                    fan.setClickable(true);
                    light.setClickable(true);
                    ac.setClickable(true);
                    projector.setClickable(true);
                }
            }
        });
        fan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (fan.isChecked()) {
                    callFile("fanon.php");
                } else {
                    callFile("fanoff.php");
                }
            }
        });
        light.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (light.isChecked()) {
                    callFile("lighton.php");
                } else {
                    callFile("lightoff.php");
                }
            }
        });
        ac.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (ac.isChecked()) {
                    callFile("acon.php");
                } else {
                    callFile("acoff.php");
                }
            }
        });
        projector.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (projector.isChecked()) {
                    callFile("projectoron.php");
                } else {
                    callFile("projectoroff.php");
                }
            }
        });



    }
    public void setState(){

        RequestQueue queue = Volley.newRequestQueue(getApplicationContext());
        StringRequest stringRequest = new StringRequest(Request.Method.GET,"http://autohome.srpec.org.in/getstate.php",
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        try {
                            Log log;
                            //converting response to json object
                            JSONObject obj = new JSONObject(response);


                            if(obj.getString("auto").equals("1")){
                                t.setChecked(true);
                                fan.setClickable(false);
                                light.setClickable(false);
                                ac.setClickable(false);
                                projector.setClickable(false);
                            }else{
                                t.setChecked(false);
                                fan.setClickable(true);
                                light.setClickable(true);
                                ac.setClickable(true);
                                projector.setClickable(true);
                            }

                            if(obj.getString("fan").equals("1")){
                                fan.setChecked(true);
                            }else{fan.setChecked(false);}

                            if(obj.getString("light").equals("1")){
                                light.setChecked(true);
                            }else{light.setChecked(false);}

                            if(obj.getString("ac").equals("1")){
                                ac.setChecked(true);
                            }else{
                                ac.setChecked(false);
                            }

                            if(obj.getString("projector").equals("1")){
                                projector.setChecked(true);
                            }else{
                                projector.setChecked(false);
                            }


                        } catch (Exception e) {

                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }});
        queue.add(stringRequest);


    }
    public void callFile(String s){

        RequestQueue queue = Volley.newRequestQueue(getApplicationContext());
        StringRequest stringRequest = new StringRequest(Request.Method.GET,"http://autohome.srpec.org.in/"+s,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }});
        queue.add(stringRequest);


    }

}
