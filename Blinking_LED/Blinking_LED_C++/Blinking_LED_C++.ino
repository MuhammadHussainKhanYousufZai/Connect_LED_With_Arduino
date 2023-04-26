int ledPin = 14;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPin, LOW);
    delay(1000);
    digitalWrite(ledPin, HIGH);
    delay(1000);
  }
}
