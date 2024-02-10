int solenoidPin = A2; // This is the output pin on the Arduino we are using
int incomingByte;    // Variable to store incoming serial data

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);           // Initialize serial communication
  pinMode(solenoidPin, OUTPUT); // Sets the pin as an output
}

void loop() {
  // Check if data is available to read from the serial port

    if (Serial.available() > 0) {
    // read the incoming byte:
      incomingByte = Serial.read();

    // Check the value of the incoming byte
        // say what you got:
    // Serial.print("I received: ");
    // Serial.println(incomingByte, DEC);

    if (incomingByte == '1') {
        // Switch Solenoid ON for 2 seconds
        digitalWrite(solenoidPin, HIGH);
        delay(2000)
        digitalWrite(solenoidPin, LOW);

    } else if (incomingByte == '0') {
        // Switch Solenoid OFF
        digitalWrite(solenoidPin, LOW);
    }
  }
  // Add any additional code you want to run in the loop
}