#include <iostream>
#include <string>

using namespace std;

/*  
- - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -

Alex just got a new hula hoop, he loves it but feels discouraged because his little brother
is better than him.

Write a program where Alex can input (n) how many times the hoop goes round and it will 
return him an encouraging message:

   - If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
   - If he doesn't get 10 hoops, return the string "Keep at it until you get it".

- - - - - - - -  - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -*/

std::string hoop_count(int n)
{
	if (n >= 10){
		return "Great, now move on to tricks";
	}
	else {return "Keep at it until you get it";}
};

int main(int argc, char** argv) {
	cout << "n = -100 : " << hoop_count(-100) << endl;
	cout << "n = 0 : " << hoop_count(0) << endl;
	cout << "n = 1 : " << hoop_count(1) << endl;
	cout << "n = 10 : " << hoop_count(10) << endl;	
	cout << "n = 11 : " << hoop_count(11) << endl;
	cout << "n = 110 : " << hoop_count(110) << endl;	
	return 0;
}

/* ====================================  TOP SOLUTION   ====================================

#include <string>
std::string hoop_count(unsigned n) {
   return (n >= 10) ? "Great, now move on to tricks" : "Keep at it until you get it";
}

=========================================================================================  */