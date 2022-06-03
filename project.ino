int lightsensor = A0;
int lightval;
bool open = false;

void setup() {
    Serial.begin(9600);
}

void loop() {
    lightval = analogRead(lightsensor);
    if (lightval > 10){
        if (open == false)
            Particle.publish("isopen", "1");
        open = true;
        delay(20000);
    } else {
        if (open == true)
            Particle.publish("isopen", "0");
        open = false;
        delay(20000);
    }
}