import math

side_a = float(input("What is the first leg of the triangle?:"));
side_b = float(input("What is the second leg of the triangle?:"));

side_a = round(side_a, 1);
side_b = round(side_b, 1);

#Calculation
side_c = math.sqrt(side_a**2 + side_b**2);
side_c = round(side_c, 3);

area = 0.5*side_a*side_b;
area = round(area, 3);

#Summary
print("\nFor a triangle with legs of " + str(side_a) + " and " + str(side_b) + " the hypotenyse is " + str(side_c) + ".");
print("\nAnd the area is " + str(area) + ".");