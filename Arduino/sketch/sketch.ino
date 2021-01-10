#include <U8g2lib.h>
 
#define led 2
#define buzz 5
#define button 6

int player = 1;

U8G2_SSD1306_128X64_NONAME_1_HW_I2C u8g2(U8G2_R2, /* reset=*/U8X8_PIN_NONE);

void setup() {
  Serial.begin(9600);
  u8g2.setBusClock(100000);
  u8g2.begin();
  pinMode(led, OUTPUT);
  pinMode(buzz, OUTPUT);
  pinMode(button, INPUT);
  delay(100);
}

void loop() {
  char in = Serial.read();
  if(in == '1') {
    u8g2.setFont(u8g2_font_t0_16b_mr);
    u8g2.setCursor(44, 46);
    u8g2.print(F("Dice rolling...."));
    while (true) {
      if(digitalRead(button)) {
        u8g2.clear();
        int no = random(1, 7);
        Serial.println(no);
        u8g2.setCursor(44,30);
        u8g2.print(String(no)); 
        break;
      } 
    }
  }
  if(in == '6') {
    digitalWrite(led, HIGH);
    delay(2000);
    digitalWrite(led, LOW);
  }
  else if(in == '7') {
    tone(buzz, 300);
    delay(2000);
    noTone(buzz);
  }
  else if(in == '8') {
    digitalWrite(led, HIGH);
    tone(buzz, 300);
    delay(2000);
    digitalWrite(led, LOW);
    noTone(buzz);
  }
  delay(100);
}
