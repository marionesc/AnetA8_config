/************************************************************************************************************/
/* Created by Marion ESCOUTELOUP                                                                            */
/* GITHUB : maesc                                                                                           */
/*                                                                                                          */
/* Day creation : 25/04/2022                                                                                */
/* Day update :   25/04/2022                                                                                */
/*                                                                                                          */
/* For the anet A8 -- personal printer installation                                                         */
/************************************************************************************************************/
/*                                     maesc @2022 all rights reserved                                      */
/************************************************************************************************************/


/*** LIBRARY USED ***/
#include <Wire.h>                     // I2C communication library
#include <SoftwareSerial.h>           // Serial discussion library
#include <ArduinoJson.h>              // JSON format (for java communication) library

#include <SHT1x.h>                    // Temperature & humidity sensor library

/*** GLOBALS CONSTANT ***/
#define PRINTER_NAME "ANET_A8"

/* Current temperature & humidity */
#define PIN_IN_DATA_TH1   51
#define PIN_IN_CLOCK_TH1  53
SHT1x sht1x(PIN_IN_DATA_TH1, PIN_IN_CLOCK_TH1);

#define SETTING_MAXIMUM_TEMPERATURE 128   // Datasheet value
#define SETTING_MINIMUM_TEMPERATURE 40    // Datasheet value
#define SETTING_MAXIMUM_HUMIDITY 90       // Datasheet value -- maximum precision
#define SETTING_MINIMUM_HUMIDITY 10       // Datasheet value -- minimum precision

/*** GLOBALS FUNCTIONS ***/

/** This function read the real temperature in celsius with sht1x sensor by Adafruit
   no @param
   @return temperature
*/
float getRealTemperatureC() {
  float temperature = floor(sht1x.readTemperatureC());

  // Sensor broken or not connected
  boolean temp1_valid = (temperature >= SETTING_MINIMUM_TEMPERATURE && temperature <= SETTING_MAXIMUM_TEMPERATURE);
  if (!temp1_valid)
    temperature = -173;

  return temperature;
}

/** This function read the real temperature in farrenheit with sht1x sensor by Adafruit
   no @param
   @return temperature
*/
float getRealTemperatureF() {
  float temperature = floor(sht1x.readTemperatureF());

  // Sensor broken or not connected
  boolean temp1_valid = (temperature >= (SETTING_MINIMUM_TEMPERATURE + 173) && temperature <= (SETTING_MAXIMUM_TEMPERATURE + 173));
  if (!temp1_valid)
    temperature = -1;

  return temperature;
}

/** This function read the real humidity with sht1x sensor by Adafruit
   no @param
   @return humidity
*/
float getRealHumidity() {
  float humidity = floor(sht1x.readHumidity());

  // Sensor broken or not connected
  boolean hum1_valid = (humidity >= SETTING_MINIMUM_HUMIDITY && humidity <= SETTING_MAXIMUM_HUMIDITY);
  if (!hum1_valid)
    humidity = -1;

  return humidity;
}


/*** MAIN CODE ***/
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.print("Hello world. \n Start of arduino configuration for anet A8 control station. \n\n");

  // PIN IN INIT

  // PIN OUT INIT

  // INIT FUNCTION
  // JSON init
  StaticJsonDocument<200> printerName;
  printerName["confirmation"][PRINTER_NAME] = true;
  serializeJson(printerName, Serial);
  Serial.println();


}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Temperature : " + String(getRealTemperatureC()) + "°C || " + String(getRealTemperatureF()) + " °F \n");
  Serial.print("Humidite : " + String(getRealTemperatureC()) + "%RH \n");
  delay(5000);

}
