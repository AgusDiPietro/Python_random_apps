
print('Welcome to Fibnonacci app')

num = int(input("How manny digits of the Fibonacci Sequence would you like to compute: "));

#Values of Fib
fib = [1,1,2,3,5]
for i in range(num-2):
    new_fib = fib[1] + fib [i+1]
    fib.append(new_fib)

#Display Fib values
print("The first " + str(num) + " number of the fibonacci Sequence are: ");
for number in fib:
    print(number);

#Golden ratio
golden = []
for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)

#Display golden ratio values
print(" The corresponding Golden ratio values are: ")
for ratio in golden:
    print(ratio)