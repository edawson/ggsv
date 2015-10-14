/*
 * sim.cpp
 *
 *  Created on: Oct 14, 2015
 *      Author: dawsonet
 */

#include <cstdio>
#include <iostream>
#include "../io/fastahack/Fasta.h"

using namespace std;

int main(int argc, char* argv[]);
void printUsage();

void printUsage(){
	cout << "Usage: svsim -i <infile> -r <referenceGenome>" << endl;
}

int main(int argc, char* argv[]){


	if (argc <= 1){
		printUsage();
	}
	return 1;
	// Parse user arguments


	string myFasta = "ref.fa";

	// Load fasta file
	FastaReference fr;
	fr.open(myFasta);

	//Build fasta index for fasta file provided
	bool buildIndex = true;
	if (buildIndex) {
	        FastaIndex* fai = new FastaIndex();
	        cerr << "generating fasta index file for " << myFasta << endl;
	        fai->indexReference("ref.fa");
	        fai->writeIndexFile((string) myFasta + fai->indexFileExtension());
	    }

	// Parse VCF mutation file and search/replace them in the reference to
	// generate the individual sequence.


}


