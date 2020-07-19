package com.example.jaimin.myiotapp;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

/**
 * Created by Jaimin on 8/10/2017.
 */
public class handle extends BroadcastReceiver{

    @Override
    public void onReceive(Context context, Intent intent) {

        // TODO Auto-generated method stub
        if (intent.getAction().equals(Intent.ACTION_BOOT_COMPLETED)){

            context.startService(new Intent(context,myService.class));
            Toast.makeText(context,"iot app service start",Toast.LENGTH_LONG).show();
        }
    }

}