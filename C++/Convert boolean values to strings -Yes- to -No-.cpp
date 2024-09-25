#include <iostream>
#include <string>

using namespace std;

/*  
- - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -

Complete the method that takes a boolean value and return a "Yes" string for true,
or a "No" string for false.

- - - - - - - -  - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -*/

std::string bool_to_word(bool value)
{
	if (value == true){ return "Yes";}
	else {return "No";}
};

int main(int argc, char** argv) {
	cout << bool_to_word(true);
	cout << bool_to_word(false);
	return 0;
}

/* ====================================  TOP SOLUTION   ====================================

std::string bool_to_word(bool value)
{
  return value ? "Yes" : "No";
}

=========================================================================================  */
