#include <iostream>

// this is a single line comment

/*
  This is a multi line
  comment
  to compile:
  g++ intro.cpp
  or
  g++ -o intor intro.cpp
  to run:
  ./a.out
  or
  ./intro.cpp
  
  
 */

int main()  // here to end of line is a comment 
{
  int x = 21;
  double d = 21;
  char c;
  std::string s = "this is a string";
  
//  int y;

//  y = 30;
  
//    int a=10, b=20;
  
  std::cout << "Hello World!\n" << std::endl;
  std::cout << "the var x = " << x << "\n";
  std::cout << "Doubles: " <<d<< " " <<d/2<< std::endl;
  // int returns value 10 instead of 10.5 because it deals with integers
  std::cout << "Ints: " <<x<< " " <<x/2<< std::endl;

  d = x/2.0;
  std::cout << d << "\n";
  
  return 0;
  
}