
print("Welcome to the Letter Counter App")

#Get user input
name = input("\nWhat is your name: ").title().strip();

print("Hello, " + name + "!");

print("I will count the number of times that a specific letter appears in a message.");
message = input("\nPlease enter the message; ");
letter = input("\nPlease introduce the letter: ");

#Standarize to lower case
message = message.lower();
letter = letter.lower();

#Get the count and si
letter_count = message.count(letter);
print("\n" + name + " your message has " + str(letter_count) + " " + letter + " 's inm it,");a