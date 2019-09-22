# exercise 12 (Quenten Lundie)
 
# getting user input for the temperature to convert
degrees_f = int(input("What is the temperature in Farenheit? "))

# formula to convert Farenheit to Celsius is: (degrees farenheit minus 32) multiplied by (5/9) 
degrees_c = (degrees_f-32) * (5 / 9) 

# display the converted temperature to the user
print(degrees_f, "in degrees Farenheit is", degrees_c, " degrees in Celsius.")
