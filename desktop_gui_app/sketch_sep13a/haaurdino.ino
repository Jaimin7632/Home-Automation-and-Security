int ldrl = A0;
int light =8;
int fan =13;
int motion = 4;
int piin=22;
int piinfan=23;
int piinlight=24;
int piacin=3;
int piprin=4;
int ac=37;
int pr=39;
//finger
#include <Adafruit_Fingerprint.h>
#include <SoftwareSerial.h>

int getFingerprintIDez();
SoftwareSerial mySerial(11,10);
Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);




void setup() {
//finger
while (!Serial); 
  
  Serial.begin(9600);
  finger.begin(57600);
  
  if (finger.verifyPassword()) {
    Serial.println("Found fingerprint sensor!");
  } else {
    Serial.println("Did not find fingerprint sensor :(");
    while (1);
  }
  
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
  Serial.begin(9600);
}

void loop() {
//finger
  getFingerprintID();
  delay(50);        

//ac and projector

if(digitalRead(piacin)){
  digitalWrite(ac,0);
  }
  else
  {
    digitalWrite(ac,1);}

if(digitalRead(piprin)){
  digitalWrite(pr,0);
  }
  else
  {
    digitalWrite(pr,1);}


  
 if(digitalRead(piin)){
   if(1){
       digitalWrite(fan,LOW);
       Serial.println("fan");
       }
   else{
    digitalWrite(fan,HIGH);
    Serial.println("fanout");
    }
    int r= analogRead(ldrl);
    
   if(1){
       digitalWrite(light,LOW);
       Serial.println("light");
       }
   else{
    digitalWrite(light,HIGH);
    Serial.println("lightout");
    }    
 
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
   
  } 

}


//finger
uint8_t getFingerprintID() {
  uint8_t p = finger.getImage();
  switch (p) {
    case FINGERPRINT_OK:
      
      break;
    case FINGERPRINT_NOFINGER:
      
      return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      
      return p;
    case FINGERPRINT_IMAGEFAIL:
      
      return p;
    default:
      
      return p;
  }

  // OK success!

  p = finger.image2Tz();
  switch (p) {
    case FINGERPRINT_OK:
      
      break;
    case FINGERPRINT_IMAGEMESS:
          return p;
    case FINGERPRINT_PACKETRECIEVEERR:
      
      return p;
    case FINGERPRINT_FEATUREFAIL:
      
      return p;
    case FINGERPRINT_INVALIDIMAGE:
      
      return p;
    default:
      
      return p;
  }
  
  // OK converted!
  p = finger.fingerFastSearch();
  if (p == FINGERPRINT_OK) {
    Serial.println("Found a print match!");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_NOTFOUND) {
    Serial.println("123456789");
    return p;
  } else {
    Serial.println("Unknown error");
    return p;
  }   
  int m=finger.fingerID;
  // found a match!
  if(m<=9){
    
    Serial.print("000"+finger.fingerID);
    }
  if(m>9 && m<=99){  
  Serial.print("00"+finger.fingerID); 
  }
  if(m>99 && m<=999){  
  Serial.print("0"+finger.fingerID); 
  }
  if(m>999){
    
    Serial.print(finger.fingerID);
    }
  //Serial.println(finger.confidence); 
}

// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK) return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return -1;
  
  // found a match!
  int m=finger.fingerID;
  
  if(m<=9){
    
    Serial.print("000"+finger.fingerID);
    }
  if(m>9 && m<=99){  
  Serial.print("00"+finger.fingerID); 
  }
  if(m>99 && m<=999){  
  Serial.print("0"+finger.fingerID); 
  }
  if(m>999){
    
    Serial.print(finger.fingerID);
    }
   
  //Serial.println(finger.confidence);
  return finger.fingerID; 
}