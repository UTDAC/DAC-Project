/*
    read_CO2.cpp - Library for reading CO2 sensor code
    Created by Elaine Williams, March 22, 2022.

    Source file
    contains the actual code
*/

#include "Arduino.h"
#include "read_CO2.h"
//#include <Serial.h>

// library allows for communication with I2C / TWI devices
#include <Wire.h> //#include "Wire.h"


// constructor
read_CO2::read_CO2(int i2c_address){

    // save value as a private variable for use in other functions
    _i2c_address = i2c_address ;

    // Begin communication via I2C / TWI
    Wire.begin();

}

int read_CO2::readCO2(int &CO2level){

    byte recValue[4] = {0,0,0,0};

    Wire.beginTransmission(_i2c_address);
    Wire.write(0x22);
    Wire.write(0x00);
    Wire.write(0x08);
    Wire.write(0x2A);
    Wire.endTransmission();
    delay(30);


    Wire.requestFrom(_i2c_address, 4);
    delay(20);
    //return Wire.available();
    byte i=0;
    while(Wire.available())
    {
        recValue[i] = Wire.read();
        i++;
    }
    byte checkSum = recValue[0] + recValue[1] + recValue[2];
    CO2level = (recValue[1] << 8) + recValue[2];

    //Serial.println("%s",(char*)recValue);
    //char recVal ;
    //recVal = ("%s",(char*)recValue);

    //return i;

    if (i == 0){
        return 2;
    }
    else if(checkSum == recValue[3]){
        return 0;
    }
    else{
        return 1;
    }

}
