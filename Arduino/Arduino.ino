/*
    Copyright (C) 2025 Valentin König

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
*/

#define POT_COUNT 5
const int potPins[POT_COUNT] = {A6, A1, A0, A2, A3}; // Put your pins accordingly and in the correct order
int potValues[POT_COUNT];

void setup() {
  Serial.begin(9600);
  for(int pin:potPins)
    pinMode(pin, INPUT);
}

void loop() {
  for(int i = 0; i < POT_COUNT; i++) {
    potValues[i] = analogRead(potPins[i]);
    Serial.print((float)potValues[i]/1024);
    if(i != POT_COUNT-1) {
      Serial.print("|");
    }
  }
  Serial.println("");
  delay(10); // Refresh delay
}