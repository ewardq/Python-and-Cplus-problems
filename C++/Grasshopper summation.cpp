#include <iostream>
#include <string>

using namespace std;

/*  
- - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -

Write a program that finds the summation of every number from 1 to num. The number will 
always be a positive integer greater than 0. Your function only needs to return the result, 
what is shown between parentheses in the example below is how you reach that result and 
it's not part of it, see the sample tests.

For example (Input -> Output):

		2 -> 3 (1 + 2)
		8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

- - - - - - - -  - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -*/

int summation(int num){
	if (num > 0){
		
		int result = 0;               		// Initialize variable
		for( int i = num; i >= 0; i-- ){
			result += i;
		}
		return result;
	}
	else {return 0;}
};

int main(void) {
	cout << "n = 2 : " << summation(2) << endl;
	cout << "n = 8 : " << summation(8) << endl;	
	cout << "n = 1 : " << summation(1) << endl;	
	return 0;
}

/* ====================================  TOP SOLUTION   ====================================

unsigned summation(unsigned num) {
  return num * (num + 1) / 2;
}

=========================================================================================  */