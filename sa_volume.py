#!/usr/bin/env python3
# Created by: Billy Terimpundu
# Created on: Dec 2, 2021
# This program asks the user for the length of a cube
# It then calculates the volume and surface area and a rectangular prism
import math

def main():
    # input
    print("Today we will calculate the volume and")
    print("surface area of a rectangular prism")
    length = int(input("Enter the length (cm): "))

    # process
    volume = 7 * 4 * 3
    surface_area = 2 *(4*7+3*7+3*4)

    #  output
    print("")
    print ("Volume = {} cm^3". format (volume))
    print ("Surface Area = {} cm^2". format (surface_area))
 
 
if __name__ == "__main__":
    main()