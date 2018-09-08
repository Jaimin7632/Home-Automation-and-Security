int ldrl = A0;
int light =8;
int fan =13;
int motion = 39;
int piin=22;
int piinfan=23;
int piinlight=24;
int piacin=3;
int piprin=4;
int ac=9;
int pr=10;
int servo=51;
int pidoor=47;
#include<Servo.h>
Servo Servo1;
#include<dht.h>
dht DHT;

// if you require to change the pin number, Edit the pin with your arduino pin.

#define DHT22_PIN 40



void setup() {
//finger
while (!Serial); 
  
  Serial.begin(9600);
//servo 
 Servo1.attach(49);
 pinMode(servo,OUTPUT);
 pinMode(pidoor,INPUT);
  
 
  
//model
  pinMode(ldrl,INPUT);
  pinMode(motion,INPUT);
  pinMode(piin,INPUT);
  pinMode(fan,OUTPUT);
  pinMode(light,OUTPUT);
   pinMode(piacin,INPUT);
  pinMode(piprin,INPUT);
  pinMode(ac,OUTPUT);
  pinMode(pr,OUTPUT);
pinMode(pidoor,INPUT);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(pidoor)){
    digitalWrite(servo,HIGH);
   Servo1.write(70);
  }
  else{
Servo1.write(0);
digitalWrite(servo,LOW);
  }

  
//projector


if(digitalRead(piprin)){
  digitalWrite(pr,0);
  }
  else
  {
    digitalWrite(pr,1);}


  
 if(digitalRead(piin)){
    Serial.print("Motion : ");
    Serial.print(digitalRead(motion));
    Serial.println();
   
   if(digitalRead(motion)){
       digitalWrite(fan,LOW);
       Serial.println("fan");
       }
   else{
    digitalWrite(fan,HIGH);
    Serial.println("fanout");
    }
    int r= analogRead(ldrl);
    Serial.print("light sensor : ");
    Serial.print(r);
    Serial.println();
    
   if(analogRead(ldrl)<300){
       digitalWrite(light,LOW);
       Serial.println("light");
       }
   else{
    digitalWrite(light,HIGH);
    Serial.println("lightout");
    }
    int chk = DHT.read22(DHT22_PIN);
    Serial.print("temp : ");
    Serial.print(DHT.temperature);
    Serial.println();
     if(digitalRead(piacin)){
       if(DHT.temperature> 28.00 )
            {digitalWrite(ac,0);
              } 
            }
        else{digitalWrite(ac,1);}
         }
else{
        if(digitalRead(piinfan)){
              digitalWrite(fan,LOW);
              }
        else{
             digitalWrite(fan,HIGH);
            } 
        if(digitalRead(piinlight)){
            digitalWrite(light,LOW);
          }
         else{
            digitalWrite(light,HIGH);
           }
   if(digitalRead(piacin)){
  digitalWrite(ac,0);
  }
  else
  {
    digitalWrite(ac,1);}

  } 

}



