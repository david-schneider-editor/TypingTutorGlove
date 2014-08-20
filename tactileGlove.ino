/*
Tactile Glove Driver v. 0.0 (5/14)

*/
const int LEDPin = 13;      // The pin that the LED is attached to
const int finger1 = 3;      // Left pinky
const int finger2 = 4;      // Left ring
const int finger3 = 5;      // Left middle
const int finger4 = 6;      // Left pointer
const int finger5 = 7;      // Left thumb
const int finger6 = 8;      // Right thumb
const int finger7 = 9;      // Right pointer
const int finger8 = 10;     // Right middle
const int finger9 = 11;     // Right ring
const int finger10 = 12;    // Right pinky
const int LEDpin = 13;
char incomingByte;          // Incoming serial
int buzzTime = 250;         // Duration of vibration (mS)

void setup() {
  Serial.begin(9600);
  pinMode(LEDPin, OUTPUT);
  pinMode(finger1, OUTPUT);
  pinMode(finger2, OUTPUT);
  pinMode(finger3, OUTPUT);
  pinMode(finger4, OUTPUT);
  pinMode(finger5, OUTPUT);
  pinMode(finger6, OUTPUT);
  pinMode(finger7, OUTPUT);
  pinMode(finger8, OUTPUT);
  pinMode(finger9, OUTPUT);
  pinMode(finger10, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    Serial.print (incomingByte);

    if (incomingByte == '1') {
      digitalWrite(finger1, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger1, LOW);
      digitalWrite(LEDpin, LOW);
    }
      else if (incomingByte == '2') {
      digitalWrite(finger2, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger2, LOW);
      digitalWrite(LEDpin, LOW);
    } 
      else if (incomingByte == '3') {
      digitalWrite(finger3, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger3, LOW);
      digitalWrite(LEDpin, LOW);
    } 
      else if (incomingByte == '4') {
      digitalWrite(finger4, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger4, LOW);
      digitalWrite(LEDpin, LOW);
    } 
      else if (incomingByte == '5') {
      digitalWrite(finger5, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger5, LOW);
      digitalWrite(LEDpin, LOW);
    }     
      else if (incomingByte == '6') {
      digitalWrite(finger6, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger6, LOW);
      digitalWrite(LEDpin, LOW);
    }  
      else if (incomingByte == '7') {
      digitalWrite(finger7, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger7, LOW);
      digitalWrite(LEDpin, LOW);
    }  
      else if (incomingByte == '8') {
      digitalWrite(finger8, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger8, LOW);
      digitalWrite(LEDpin, LOW);
    }  
      else if (incomingByte == '9') {
      digitalWrite(finger9, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger9, LOW);
      digitalWrite(LEDpin, LOW);
    }  
      else if (incomingByte == 'A') {
      digitalWrite(finger10, HIGH);
      digitalWrite(LEDpin, HIGH);
      delay(buzzTime);
      digitalWrite(finger10, LOW);
      digitalWrite(LEDpin, LOW);
    }  
  }
}
