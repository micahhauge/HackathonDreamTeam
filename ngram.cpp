#include<fstream>
#include<iostream>
#include<map>
#include<vector>
#include<stdlib.h>


using namespace std;


void GenNgram(map<string,map<int,int>> &noteGramCount , vector<int> noteList,int gramSize);
double CompareModels(map<string,map<int,int>> gramModel1,map<string,map<int,int>> gramModel);

int main(int argv, char* argc[]){
	//setbuf(stdout,NULL);
	ifstream songFile;
	ifstream songFile2;
	int nextNote = 0;
	vector<int> noteList;
	vector<int> noteList2;
	int gramSize = 0;
	map<string,map<int,int>> noteGramCount1;
	map<string,map<int,int>> noteGramCount2;
	
	
	songFile.open(argc[1]);
	
	gramSize = atoi(argc[3]);
	
	while(!songFile.eof()){
		songFile >> nextNote;
		noteList.push_back(nextNote);
	}
	songFile.close();
	
	
	songFile2.open(argc[2]);
	while(!songFile2.eof()){
		songFile2 >> nextNote;
		noteList2.push_back(nextNote);
	}
	songFile.close();
	
	/*noteList.push_back(0);
	noteList.push_back(1);
	noteList.push_back(1);
	noteList.push_back(2);
	noteList.push_back(3);
	noteList.push_back(1);
	noteList.push_back(4);*/
	
	GenNgram(noteGramCount1, noteList,gramSize);
	GenNgram(noteGramCount2, noteList2,gramSize);
	//cout << noteList.size() << endl;
	CompareModels(noteGramCount1,noteGramCount2);
	cout << "test7" << endl;
	
	
}


void GenNgram(map<string,map<int,int>> &noteGramCount , vector<int> noteList,int gramSize){
	string preGram = "";
	int preGramSize = 0;
	
	
	for(int i = 0; i < noteList.size(); i++){
		//cout << i << endl;
		//cout << "PreGram : " << preGram << endl;
		if(preGramSize == gramSize-1){
			//cout << "PostGram: " << noteList[i] << endl;
			if(noteGramCount.find(preGram) != noteGramCount.end() && noteGramCount[preGram].find(i) != noteGramCount[preGram].end()){
				noteGramCount[preGram][noteList[i]]++;
				//cout << "test" <<endl;
			}
			else{
				noteGramCount[preGram][noteList[i]] = 1;
			}
			
			preGram = "";
			preGramSize = 0;
			// 1
			i -= (gramSize-1);
		}
		else{
			// Add the note to the current pre-listing
			preGram += to_string(noteList[i]);
			preGramSize++;
		}
	}
}



double CompareModels(map<string,map<int,int>> gramModel1,map<string,map<int,int>> gramModel2){
	map<string,map<int,int>>::iterator mod1It;
	map<int,int>::iterator mod1It_nest;
	map<string,map<int,int>>::iterator mod2It;
	map<int,int>::iterator mod2It_nest;
	double totalError = 0;
	int matchCount = 0;

	for(mod1It = gramModel1.begin(); mod1It != gramModel1.end(); mod1It++){
		cout << "PRE: " << mod1It->first << endl;
		// find the "pre" for the second model
		mod2It = gramModel2.find(mod1It->first);
		cout << "test1" << endl;
		// loop through each post of the models for comparison
		for(mod1It_nest = mod1It->second.begin(); mod1It_nest != mod1It->second.end(); mod1It_nest++){
			//if(mod2It_nest != NULL && mod1It_nest != NULL){
				
				mod2It_nest = mod2It->second.find(mod1It_nest->first);
				cout << "test2: " << mod2It_nest->second << " , " << mod1It_nest->second << endl;
				if(mod2It_nest != mod2It->second.end()){
					totalError += abs(mod2It_nest->second - mod1It_nest->second)/(mod2It_nest->second + mod1It_nest->second);
					cout << "test3" << endl;
					cout << mod1It_nest->first << " : " << mod1It_nest->second<< endl;
					cout << "test4" << endl;
				}
			//}
			cout << "test5" << endl;
		}
		cout << "test6" << endl;
		//cout << mod1It->second.begin()->first << endl;
	}
	
	cout << "Total Error: " << totalError << endl;
	return 0;
}

