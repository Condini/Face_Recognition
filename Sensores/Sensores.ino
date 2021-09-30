#include <SPI.h>
#include <MFRC522.h>
 
#define SS_PIN 10
#define RST_PIN 9
#define INF_1 8
#define INF_2 7
#define INF_3 6
#define botao 5
#define led_r 4
#define led_g 3

String uid;
String uid_DB;
String name_DB;

MFRC522 mfrc522(SS_PIN, RST_PIN);   
 
void setup() 
{
  Serial.begin(9600);  
  SPI.begin();      
  mfrc522.PCD_Init();   
  pinMode(INF_1, INPUT);
  pinMode(INF_3, INPUT);
  pinMode(INF_3, INPUT);

  pinMode(led_lav, OUTPUT);

}
void loop() 
{
  captura_dados() 
}

void captura_dados(){
  if(digitalRead(INF_1) == LOW){
    Serial.print("1");
  } else {
    Serial.print("0");
  }
  if(digitalRead(INF_2) == LOW){
    Serial.print("1");
  } else {
    Serial.print("0");
  }
  if(digitalRead(INF_3) == LOW){
    Serial.print("1");
  } else {
    Serial.print("0");
  }

  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     String var_1 = mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ";
     String var_2 = mfrc522.uid.uidByte[i], HEX;
     content.concat(var_1);
     content.concat(var_2);
  }
  content.toUpperCase();
  uid = content.substring(1);
  Serial.println(uid);

  
}
