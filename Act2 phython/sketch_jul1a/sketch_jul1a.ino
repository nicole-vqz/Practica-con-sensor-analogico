char car;
int val;
const int pinFotoresistencia = 36; //GPIO 36 (VP)

void setup() {
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
    car = Serial.read();
    if (car == 'r') {
      val = analogRead(pinFotoresistencia); // Lee el pin 36 (Devuelve de 0 a 4095)
      Serial.println(val);
    }
  }
}