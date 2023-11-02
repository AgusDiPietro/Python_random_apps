
print("Welcome to the Temperature convertion program");

temp_f = float(input("\nwhat is the temperature in degrees Fahrenheit: "));

#Convert temps
temp_c = (5/9)* (temp_f - 32);
temp_k = temp_c + 273;

#Round temps
temp_f = round(temp_f, 2);
temp_c = round(temp_c, 2);
temp_k = round(temp_k, 2);

#Summary
print("\nDegrees Fahreneheit:\t" + str(temp_f));
print("Degrees Celsius:\t" + str(temp_c));
print("Degrees Kelvin:\t\t" + str(temp_k));


2