// Project-04-C++

#include <iostream>
#include <cstdlib> 

// Extra 2: Create a working function with a parameter
// Make sure you’ve implemeted at least one function that takes in at least one parameter and returns a value. For example. if you determine the abolute value of a number for your program, you could write a function that takes in an integer parameter and returns its absolue value.
int absoluteValue(int num) {
  // If the number is a negative, it will return the positive value of the number
  if (num < 0) {
    return -1 * num;
  }
  // If the number is positive then it will return the number itself
  else {
    return num;
  }
}

int main()
{
// Base Project: Write a working C++ program in a file named main.cpp in your cpp folder. The program should print out the string “Hello World!” followed by a newline.
std::cout << "Hello World!" << std::endl;

// Extra 1
// Your program must show that you understand an if statement and a loop. You can modify your program in any way to exhibit this.

{
// Determine which of two numbers is greater
// Choosing a random number from the range 0 - 99 (std::rand() % 100)
int num1 = std::rand() % 100;
int num2 = std::rand() % 100;

std::cout << "The two numbers are: " << num1 << " and " << num2 << std::endl;

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

// Calculate the sum of values from 1 to a random number (0 - 99)
int num4 = std::rand() % 100;
int sum = 0;
for (int i = 1; i <= num4; i++)
{
sum += i;
}
std::cout << "The sum of values from 1 to " << num4 << " is " << sum << std::endl;
}

// Creating a for loop that prints the numbers 1 - 10
for(int i = 1; i <= 10; i++){
  std::cout << i << std::endl;
}

// Extra 2
// Testing the function 
  int getAbsoluteValue(int x);
  // print result(s) of diff trials
  std::cout << absoluteValue(100) << std::endl;
  std::cout << absoluteValue(-22) << std::endl;
  std::cout << absoluteValue(-7) << std::endl;

  return 0;

}