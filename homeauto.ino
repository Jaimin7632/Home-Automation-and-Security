const int motionsensor = 2;
const int aut = 13;
const int ldrled = 3;
const int myfan = 4;
const int projector = 5;
const int ac = 6;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ldrled,OUTPUT);
  pinMode(myfan,OUTPUT);
  pinMode(aut,INPUT);
  
    pinMode(8,INPUT);
      pinMode(9,INPUT);
        pinMode(10,INPUT);
          pinMode(11,INPUT);
  
}

void loop() {
  
  
  if(digitalRead(aut)){
       int fan = digitalRead(motionsensor);
       if(fan){
       digitalWrite(myfan,HIGH);
       Serial.println("fan");
       }
       else{
         digitalWrite(myfan,LOW);
        Serial.println("fanout"); 
       }
 
 	
       int r=analogRead(A0);// ldr
       if(r <100){
       digitalWrite(ldrled,HIGH);
       Serial.println("light");
       }
       else{
         digitalWrite(ldrled,LOW);
         Serial.println("lightout");
       }
       
       
    if(digitalRead(10)){ digitalWrite(projector,HIGH);
    }
    else{
      digitalWrite(projector,LOW);
    }  
    
    if(digitalRead(11)){ digitalWrite(ac,HIGH);
    }
    else{
      digitalWrite(ac,LOW);
    }  
       
       
  }
  else{
    if(digitalRead(8)){ digitalWrite(myfan,HIGH);
    }
    else{
      digitalWrite(myfan,LOW);
    }  
    
    if(digitalRead(9)){ digitalWrite(ldrled,HIGH);
    }
    else{
      digitalWrite(ldrled,LOW);
    }  
    
    if(digitalRead(10)){ digitalWrite(projector,HIGH);
    }
    else{
      digitalWrite(projector,LOW);
    }  
    
    if(digitalRead(11)){ digitalWrite(ac,HIGH);
    }
    else{
      digitalWrite(ac,LOW);
    }  
  }

}
