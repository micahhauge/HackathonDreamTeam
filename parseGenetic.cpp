#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <map>
#include <iterator>
#include <string>

using namespace std;

// last file in training data
const int LAST_FILE_INDEX = 41; // # of measures in the genetically-generated song

struct Note{
	float duration;
	int start, pitch, value; // "value" is the final value used in the n-gram
	string velocity;
};

typedef vector <Note> noteList;

int main(){
	ifstream is;
	string outstring = "";

	for (int fileTag = 1; fileTag <= LAST_FILE_INDEX; fileTag++){

		is.open("./gToParse/m" + to_string(fileTag) + ".txt");
		assert(is);

		map<int, noteList> songMap;

		Note temp;

		// input
		while (is >> temp.start){
		      	is >> temp.duration;
			is >> temp.pitch;
			temp.value = temp.pitch; // default final value to current pitch
			getline(is, temp.velocity);
			songMap[temp.start].push_back(temp);
		} // end of while

		auto nextIndex = songMap.begin();

		// flatten
		// CARE: when we print, we will only use the FIRST index of songMap[i][INDEX].
		// 	because that's going to be the unique value for that timestamp.
		for (auto it = songMap.begin(); it != songMap.end(); ++it){
			nextIndex = it;
			nextIndex++;

			if (!songMap[it->first].empty() && !songMap[nextIndex->first].empty() &&
					( (it->first + songMap[it->first][0].duration) > songMap[nextIndex->first][0].start) ){ // if current start time + current duration > next start time, then overlapping notes and add

				switch(songMap.size()){
					// main comparison logic for n-gram:
					// if notes are played simultaneously, add their pitch values
					// CARE: each note's value is defaulted to pitch, so in the case where notes are not simultaneous,
					// 	(up to 1 extra note on top of simultaneous notes in current implementation)
					// 	the pitch will not change
					case 1: songMap[it->first][0].value += songMap[nextIndex->first][0].pitch;
						break;
					case 2: songMap[it->first][0].value += songMap[it->first][songMap.size()-1].pitch +
										songMap[nextIndex->first][0].pitch;
						break;
					case 3: songMap[it->first][0].value += songMap[it->first][songMap.size()-1].pitch +
										songMap[it->first][songMap.size()-2].pitch +
										songMap[nextIndex->first][0].pitch;
						break;
					case 4: songMap[it->first][0].value += songMap[it->first][songMap.size()-1].pitch +
										songMap[it->first][songMap.size()-2].pitch +
										songMap[it->first][songMap.size()-3].pitch +
										songMap[nextIndex->first][0].pitch;
						break;
					case 5: songMap[it->first][0].value += songMap[it->first][songMap.size()-1].pitch +
										songMap[it->first][songMap.size()-2].pitch +
										songMap[it->first][songMap.size()-3].pitch +
										songMap[it->first][songMap.size()-4].pitch +
										songMap[nextIndex->first][0].pitch;
						break;
					case 6: songMap[it->first][0].value += songMap[it->first][songMap.size()-1].pitch +
										songMap[it->first][songMap.size()-2].pitch +
										songMap[it->first][songMap.size()-3].pitch +
										songMap[it->first][songMap.size()-4].pitch +
										songMap[it->first][songMap.size()-5].pitch +
										songMap[nextIndex->first][0].pitch;
					        break;
					default: break;
				};// end switch cases

			}// end if simultaneous

		}// end for auto

		ofstream outfile;
		outfile.open("./gParsed/out" + to_string(fileTag) + ".txt");

		for (auto it = songMap.begin(); it != songMap.end(); ++it){
			if (!songMap[it->first].empty()){

				for (int i = 0; i < songMap[it->first][0].duration; i++){
					// write to file
					outstring += to_string(songMap[it->first][0].value) + " ";

				} // end duration repetition for
			}
		}// end auto for

		outfile.close();

		is.close();

	}// end looping through all files

	cout << outstring;

}
