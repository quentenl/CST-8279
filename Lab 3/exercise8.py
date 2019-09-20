# exercise 8 (Quenten Lundie)
#import math module
import math

radius_circ = int(input("What is the radius of the circle in cm?  "))

# use radius to calculate area usin pi*r^2
area_circ = math.pi * math.pow(radius_circ , 2)

#print output to user of area 
print("The area of a circle with a radius of", radius_circ, " is", round(area_circ,3) , "cm^2" )