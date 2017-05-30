#include <CapacitiveSensor.h>
CapacitiveSensor capSensor = CapacitiveSensor(4,8);
CapacitiveSensor capSensor1 = CapacitiveSensor(4,7);
CapacitiveSensor capSensor2 = CapacitiveSensor(4,6);
CapacitiveSensor capSensor3 = CapacitiveSensor(4,5);
CapacitiveSensor capSensor4 = CapacitiveSensor(4,3);
CapacitiveSensor capSensor5 = CapacitiveSensor(4,2);
CapacitiveSensor capSensor6 = CapacitiveSensor(4,9);
CapacitiveSensor capSensor7 = CapacitiveSensor(4,10);
CapacitiveSensor capSensor8 = CapacitiveSensor(4,11);  
CapacitiveSensor capSensor9 = CapacitiveSensor(4,12);
CapacitiveSensor capSensor10 = CapacitiveSensor(4,13);

void setup() {

    Serial.begin(9600);
   

}//Fin de la funcion setup.

void loop() {

    long sensorValue = capSensor.capacitiveSensor(30);
    

    if(sensorValue > 0) {
        Serial.println(1);
    }
    long sensorValue1 = capSensor1.capacitiveSensor(30);
    

    if(sensorValue1 > 0) {
        Serial.println(2);
    }
    long sensorValue2 = capSensor2.capacitiveSensor(30);
    
    if(sensorValue2 > 0) {
        Serial.println(3);
    }
    long sensorValue3 = capSensor3.capacitiveSensor(30);
    
    if(sensorValue3 > 0) {
        Serial.println(4);
    }
    long sensorValue4 = capSensor4.capacitiveSensor(30);
    
    if(sensorValue4 > 0) {
        Serial.println(5);
    }
    
    
    long sensorValue5 = capSensor5.capacitiveSensor(30);
    
    if(sensorValue5 > 0) {
        Serial.println(6);
    }
    long sensorValue6 = capSensor6.capacitiveSensor(30);
    
    if(sensorValue6> 0) {
        Serial.println(7);
    }
    long sensorValue7 = capSensor7.capacitiveSensor(30);
    
    if(sensorValue7> 0) {
        Serial.println(8);
    }
    long sensorValue8 = capSensor8.capacitiveSensor(30);
    
    if(sensorValue8> 0) {
        Serial.println(9);
    }
    long sensorValue9 = capSensor9.capacitiveSensor(30);
    
    if(sensorValue9> 0) {
        Serial.println(10);
    }
    long sensorValue10 = capSensor10.capacitiveSensor(30);
    
    if(sensorValue10> 0) {
        Serial.println(11);
    }
    delay(500);

}//Fin de la funcion loop.
