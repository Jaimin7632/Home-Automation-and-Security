int ldrl = A0;
int light = 11;
int fan =13;
int motion = 4;
int piin=22;
int piinfan=23;
int piinlight=24;
int piacin=3;
int piprin=4;
int ac=37;
int pr=39;


void setup() {
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
