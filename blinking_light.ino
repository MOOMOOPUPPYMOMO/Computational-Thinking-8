void setup() {
    pinMode(13, OUTPUT);
}

void loop() { 
    digital write(13, HIGH); 
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);
}