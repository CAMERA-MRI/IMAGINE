/* ──────────── pin map (unchanged) ──────────── */
const int Step_z = 7, Dir_z = 6;
const int Step_x = 5, Dir_x = 4;
const int Step_y = 3, Dir_y = 2;

#define STEPS_PER_MM  1600   // 1-mm move = 533 pulses,(533.33333334) now the modified calibration will be 1066.666667, new value 1600
#define PULSE_US      200            // HIGH / LOW time per pulse

void setup() {
  Serial.begin(9600);                // must match the Python BAUD
  pinMode(Step_z, OUTPUT);  pinMode(Dir_z, OUTPUT);
  pinMode(Step_x, OUTPUT);  pinMode(Dir_x, OUTPUT);
  pinMode(Step_y, OUTPUT);  pinMode(Dir_y, OUTPUT);
}

/* ───────── main loop: parse newline-terminated commands ───── */
void loop() {
  static char line[16];
  static byte idx = 0;

  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n' || c == '\r') {     // end of command
      line[idx] = '\0';
      idx = 0;
      handleCmd(line);
    } else if (idx < sizeof(line) - 1) {
      line[idx++] = c;               // build token
    }
  }
}

/* ───────── command dispatcher ───────── */
void handleCmd(const char *cmd) {
  if      (!strcmp(cmd, "X+")) { digitalWrite(Dir_x, HIGH); moveSteps(Step_x); }
  else if (!strcmp(cmd, "X-")) { digitalWrite(Dir_x, LOW);  moveSteps(Step_x); }
  else if (!strcmp(cmd, "Y+")) { digitalWrite(Dir_y, LOW);  moveSteps(Step_y); } // Reversed direction
  else if (!strcmp(cmd, "Y-")) { digitalWrite(Dir_y, HIGH); moveSteps(Step_y); } // Reversed direction
  else if (!strcmp(cmd, "Z+")) { digitalWrite(Dir_z, HIGH); moveSteps(Step_z); }
  else if (!strcmp(cmd, "Z-")) { digitalWrite(Dir_z, LOW);  moveSteps(Step_z); }
  /* any other string is ignored */
}

/* ───────── 1-mm step routine ───────── */
void moveSteps(int stepPin) {
  for (int i = 0; i < STEPS_PER_MM; ++i) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(PULSE_US);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(PULSE_US);
  }
}