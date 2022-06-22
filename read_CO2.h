*
    read_CO2.h - Library for code for reading a CO2 sensor
    Created by Elaine Williams, March 22, 2022.

    Header file
    contains definitions for the library (list of everything that's inside)
*/


// Define the library for use in the module it's imported into
// If the library has been included twice, prevents issues
#ifndef read_CO2_h
#define read_CO2_h

#include <Arduino.h>


class read_CO2{

    // public: can be accessed by anyone/thing using the library
    public:
        // constructor. creates an instance of the class
        read_CO2(int i2c_address);
        int readCO2(int &CO2level);

    // private: can only be accessed from within the class itself
    private:
        int _i2c_address;

};



#endif // read_CO2_h
