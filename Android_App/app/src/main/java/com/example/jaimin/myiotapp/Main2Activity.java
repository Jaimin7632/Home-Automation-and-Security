package com.example.jaimin.myiotapp;

import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.bumptech.glide.Glide;
import com.bumptech.glide.load.engine.DiskCacheStrategy;
import com.bumptech.glide.load.resource.drawable.GlideDrawable;
import com.bumptech.glide.request.RequestListener;
import com.bumptech.glide.request.target.Target;

import java.io.InputStream;
import java.net.URL;

public class Main2Activity extends AppCompatActivity {

    ImageView i;
    Button r,s;
ProgressDialog pDialog;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        i =(ImageView) findViewById(R.id.img);
        r=(Button) findViewById(R.id.button2);
        s=(Button) findViewById(R.id.button);

        pDialog = new ProgressDialog(this);
        pDialog.setCancelable(false);


        final String imgURL  = "http://autohome.srpec.org.in/img.jpg";

        pDialog.setMessage("Downloading Image...");

        i.setImageResource(0);
        imgset(i,imgURL);
        r.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                callFile("dooron.php");
                callFile("deletefile.php");
                Intent i = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(i);
            }
        });

        s.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                callFile("deletefile.php");
                Intent i = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(i);

            }
        });

    }

private void imgset(ImageView i,String imgURL){
    showDialog();
    Glide.with(getApplicationContext()).load(imgURL)
            .thumbnail(0.5f)
            .crossFade()
            .diskCacheStrategy(DiskCacheStrategy.NONE)
            .skipMemoryCache(true)
            .listener(new RequestListener<String, GlideDrawable>() {
                @Override
                public boolean onException(Exception e, String model, Target<GlideDrawable> target, boolean isFirstResource) {
                    hideDialog();
                    return false;

                }

                @Override
                public boolean onResourceReady(GlideDrawable resource, String model, Target<GlideDrawable> target, boolean isFromMemoryCache, boolean isFirstResource) {
                    hideDialog();
                    return false;
                }
            })
            .into(i);



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

    public void showDialog() {
        if (!pDialog.isShowing())
            pDialog.show();
    }

    public void hideDialog() {
        if (pDialog.isShowing())
            pDialog.dismiss();
    }

}
