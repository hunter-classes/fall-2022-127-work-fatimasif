// Project-04-C++
// Base Project: Write a working C++ program in a file named main.cpp in your cpp folder. The program should print out the string “Hello World!” followed by a newline.

#include <iostream>

int main()
{
std::cout << "Hello World!" << std::endl;
return 0;


// Extra 1
// your program must show that you understand an if statement and a loop. You can modify your program in any way to exhibit this.

// Determine which of two numbers is greater
// Determine the absolute value of a number
// Calculate the sum of values from 1 to some larger numbers

{
// Determine which of two numbers is greater
int num1 = 10;
int num2 = 20;

if (num1 > num2)
{
std::cout << num1 << " is greater than " << num2 << std::endl;
}
else
{
std::cout << num1 << " is not greater than " << num2 << std::endl;
}

// Determine the absolute value of a number
int num3 = -10;
if (num3 < 0)
{
num3 = -num3;
}
std::cout << "The absolute value of " << num3 << " is " << num3 << std::endl;

// Calculate the sum of values from 1 to some larger number
int num4 = 100;
int sum = 0;
for (int i = 1; i <= num4; i++)
{
sum += i;
}
std::cout << "The sum of values from 1 to " << num4 << " is " << sum << std::endl;

return 0;
}

// Extra 2
// Make sure you’ve implemeted at least one function that takes in at least one parameter and returns a value. For example. if you determine the abolute value of a number for your program, you could write a function that takes in an integer parameter and returns its absolue value.

// Function that takes in an integer parameter and returns its absolute value
int getAbsoluteValue(int num)
{
if (num < 0)
{
num = -num;
}
return num;
}

{
// Determine the absolute value of a number
int num = -10;
int abs_value = getAbsoluteValue(num);
std::cout << "The absolute value of " << num << " is " << abs_value << std::endl;

return 0;
}

}







