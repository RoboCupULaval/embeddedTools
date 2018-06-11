
int triggerPin = 5;
int firstPulseMS = 50;
int secondPulseMS1 = 100;
int secondPulseMS2 = 150;
int secondPulseMS3 = 200;
int delayBetweenPulseMS = 50;

char incomingByte = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("------------------------------------------------");
  Serial.println("Welcome to the fabulous world of spot weldering!");
  Serial.println("DON'T FORGET THAT IT'S A DANGEROUS WORLD!");
  Serial.println("------------------------------------------------");
  Serial.println();
  printSettings();
  printHelp();
   pinMode(triggerPin, OUTPUT);
}

void loop() {
  handleSerial();
}

void handleSerial(void) {
  if(Serial.available() > 0) {
    incomingByte = Serial.read();
    switch(incomingByte) {
      case '1':
        Serial.println("Pre-solder pulse");
        digitalWrite(triggerPin, HIGH);
        delay(firstPulseMS);
        digitalWrite(triggerPin, LOW);
        break;
      case '2':
        Serial.println("Solder pulse");
        digitalWrite(triggerPin, HIGH);
        delay(secondPulseMS1);
        digitalWrite(triggerPin, LOW);
        break;
      case '3':
        Serial.println("Solder pulse");
        digitalWrite(triggerPin, HIGH);
        delay(secondPulseMS2);
        digitalWrite(triggerPin, LOW);
        break;
      case '4':
        Serial.println("Solder pulse");
        digitalWrite(triggerPin, HIGH);
        delay(secondPulseMS3);
        digitalWrite(triggerPin, LOW);
        break;
      case 'a':
        Serial.println("Auto solder 1");
        digitalWrite(triggerPin, HIGH);
        delay(firstPulseMS);
        digitalWrite(triggerPin, LOW);
        delay(delayBetweenPulseMS);
        digitalWrite(triggerPin, HIGH);
        delay(secondPulseMS1);
        digitalWrite(triggerPin, LOW);
        break;
      case 'b':
        Serial.println("Auto solder 2");
        digitalWrite(triggerPin, HIGH);
        delay(firstPulseMS);
        digitalWrite(triggerPin, LOW);
        delay(delayBetweenPulseMS);
        digitalWrite(triggerPin, HIGH);
        delay(secondPulseMS2);
        digitalWrite(triggerPin, LOW);
        break;
      case 'c':
        Serial.println("Auto solder 3");
        digitalWrite(triggerPin, HIGH);
        delay(firstPulseMS);
        digitalWrite(triggerPin, LOW);
        delay(delayBetweenPulseMS);
        digitalWrite(triggerPin, HIGH);
        delay(secondPulseMS3);
        digitalWrite(triggerPin, LOW);
        break;
      case 's':
        Serial.println("STOP!!");
        digitalWrite(triggerPin, LOW);
        break;
      case 'h':
        printHelp();
        break;
      case '\r': 
      case '\n':
        break;
      default:
        Serial.println("\nUnknown command\n");
        break;
    }
  }
}

void printSettings(void) {
  Serial.println("------------------------------------------------");
  Serial.println("Settings");
  Serial.print("Trigger pin : ");
  Serial.println(triggerPin);
  Serial.print("First pulse time : ");
  Serial.print(firstPulseMS);
  Serial.println(" ms");
  Serial.print("Delay between pulse : ");
  Serial.print(delayBetweenPulseMS);
  Serial.println(" ms");
  Serial.print("Second pulse time 1 : ");
  Serial.print(secondPulseMS1);
  Serial.println(" ms");
  Serial.print("Second pulse time 2 : ");
  Serial.print(secondPulseMS2);
  Serial.println(" ms");
  Serial.print("Second pulse time 3 : ");
  Serial.print(secondPulseMS3);
  Serial.println(" ms");
  Serial.println();
  Serial.println("------------------------------------------------");
}

void printHelp(void) {
  Serial.println("------------------------------------------------");
  Serial.println("Help menu");
  Serial.println();
  Serial.println("1 : Pre-solder pulse");
  Serial.println("2 : Solder pulse short");
  Serial.println("3 : Solder pulse mid");
  Serial.println("4 : Solder pulse long");
  Serial.println("a : Auto solder 1 (two pulses short)");
  Serial.println("b : Auto solder 2 (two pulses mid)");
  Serial.println("c : Auto solder 3 (two pulses long)");
  Serial.println("s : Force stop (not implemented!)");
  Serial.println("h : Print this help");
  Serial.println();
  Serial.println("------------------------------------------------");
  Serial.println();
}

