#include <Servo.h>

int servoPanPin = 3;     // Control pin for servo motor
int servoTiltPin = 9;     // Control pin for servo motor

int pos = 0;                 // position

Servo panServo;
Servo tiltServo;

void setup()
{
 Serial.begin(9600);
 panServo.attach(servoPanPin);  
 tiltServo.attach(servoTiltPin);
 panServo.write(90);
 tiltServo.write(90);
}

void loop()
{
 if ( Serial.available())
 {
   char ch = Serial.read();
   if(ch >= '0' && ch <= '9')              // is ch a number?  
      pos = pos * 10 + ch - '0';           // yes, accumulate the value
   else if(ch == 'p' || ch == 'P')  // pan
   {
     panServo.write(pos);          
     Serial.print("Pan Servo angle: ");
     Serial.println(pos);
     pos = 0;
   }
   else if(ch == 't' || ch == 'T')  // tilt
   {
     tiltServo.write(pos);        
     Serial.print("Tilt Servo angle: ");
     Serial.println(pos);
     pos = 0;
   }  
 }
}
