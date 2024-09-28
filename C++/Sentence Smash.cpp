#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*  
- - - - - - - - - - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -

Write a function that takes an array of words and smashes them together into a sentence 
and returns the sentence. You can ignore any need to sanitize words or add punctuation, 
but you should add spaces between each word. Be careful, there shouldn't be a space at 
the beginning or the end of the sentence!

Example

	['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

- - - - - - - -  - - - - - - - - - - - T A S K  - - - - - - - - - - - - - - - - - - - -*/

std::string smash(const std::vector<std::string>& words){
	std::string result_string = "";
	
	for(int i = 0; i < words.size(); i++){
    
    // Add word to the final string
		result_string.append(words[i]);
		
    // Add a space unless this is the final word
		if( i < words.size()-1){
			result_string.append(" ");
		}
	}
	
	return result_string;
};

int main(void) {
	vector<string> test_vect = {"hello", "world", "this", "is", "great"};
	cout << "vect ['hello', 'world'] >> : " << smash(test_vect) << endl;
	return 0;
}

/* ====================================  TOP SOLUTION   ====================================

std::string smash( const std::vector< std::string >& words ) {
  if ( words.empty() ) return {};
  std::string sentence;
  for ( const auto& word : words ) sentence += word + ' ';
  return sentence.pop_back(), sentence;
}

=========================================================================================  */
