#include<Servo.h>
Servo Servo1;
void setup()
{Servo1.attach(49);
pinMode(51,OUTPUT);
pinMode(47,INPUT);

}
void loop()
{
  if(digitalRead(47)){
    digitalWrite(51,HIGH);
Servo1.write(70);
  }
  else{
Servo1.write(0);
digitalWrite(51,LOW);
  }
}
