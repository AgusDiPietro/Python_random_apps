import datetime

#Create the datetime object and store the current date and time
time = datetime.now();
month = str(time.month);
day = str(time.day);
hour = str(time.hour);
minute = str(time.minute);

#UI
foods = ["Meat", "Cheese", "Bread"];
print("Welcome to the Grocery List App");
print("Current Date and time: " + month + "/" + day + "\t" + hour + ":" + minute);
print("You currently have " + foods[0] + "and " + foods[1] + "in your list.");

#User Input
food = input("\nType of food to add to the grocery list: ");
foods.append(food.title());
food = input("\nType of food to add to the grocery list: ");
foods.append(food.title());
food = input("\nType of food to add to the grocery list: ");
foods.append(food.title());

#Print and sort the list
print("\nHere is your grocery list: ");
print = foods;
foods.sort();
print("Here the grocery list sorted: ");
print(foods);


