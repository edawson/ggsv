/*
 * sim.cpp
 *
 *  Created on: Oct 14, 2015
 *      Author: dawsonet
 */

#include <cstdio>
#include <iostream>
#include <fstream>
#include <getopt.h>
#include <vector>
#include "../io/fastahack/Fasta.h"
#include "../io/fastahack/Region.h"
#include "../io/fastahack/split.h"


using namespace std;

//TODO implement methods for insertion, deletion,
// intrachromosomal translocation, interchromosomal translocation,
// and duplication/tandem duplication.
int main(int argc, char* argv[]);
void printUsage();
//TODO Methods for inserting variation
// makeDeletion();
// makeInsertion();
// makeDuplication();
// makeTandemDuplication();
// makeErroneousDuplication();
// makeTranslocation();
// makeInversion();

void printUsage(){
    cerr << "Usage: svsim -v <VCFfile> -r <referenceGenome> [-i -h]" << endl;
    cerr << "[ -i ] Index fasta file (Default is to not produce an index)" << endl;
    cerr << "[ -h ] Print the help message and exit" << endl;
}

int main(int argc, char* argv[]){


    if (argc <= 1){
        printUsage();
        exit(1);
    }

    // Parse user arguments

    string mut_file;
    string reference;
    bool buildIndex = false;
    int c;
    int opt_ind = 0;

    while (true){
        static struct option long_options[] = {
            {"mut_file", required_argument, 0, 'v'},
            {"reference", required_argument, 0, 'r'},
            {"help", no_argument, 0, 'h'},
            {"buildIndex", no_argument, 0, 'i'}
        };
        c = getopt_long(argc, argv, "v:r:hi", long_options, &opt_ind);

        if (c == -1){
            break;
        }


        switch (c){

            // Should probably figure out what this even does.
            case 0:
                if (long_options[opt_ind].flag != 0){
                    break;
                }
                printf ("option %s", long_options[opt_ind].name);
                if (optarg)
                    printf (" with arg %s", optarg);
                printf ("\n");
                break;

            case 'v':
                mut_file = optarg;
                break;

            case 'r':
                reference = optarg;
                break;

            case 'h':
                printUsage();
                exit(0);
                break;

            case 'i':
                buildIndex = true;
                break;

            case '?':
                printUsage();
                exit(1);

            default:
                abort();

        }
    }


    string myFasta = reference;

    // Load fasta file
    //TODO fails here when an index already exists with vector out
    // of bounds.....
    FastaReference fr;
    fr.open(myFasta);

    cerr << "Using reference " << myFasta << endl;

    //Build fasta index for fasta file provided

    if (buildIndex) {
        //TODO destroy previous fasta index
        //
        // Build a new fasta index file with name <FastaFile>.fai
        FastaIndex::FastaIndex* fai = new FastaIndex::FastaIndex();
        cerr << "Generating fasta index file for " << myFasta << endl;
        fai->FastaIndex::indexReference(myFasta);
        fai->FastaIndex::writeIndexFile((string) myFasta + fai->FastaIndex::indexFileExtension());
    }

    // Parse VCF mutation file and search/replace them in the reference to
    // generate the individual sequence. Don't load the file into
    // memory.
    string var_line;
    ifstream ifi;
    ifi.open(mut_file);
    std::vector<std::string > splits;
    std::string seq;
    while (!ifi.eof()){
        getline(ifi, var_line);
        std::vector<std::string > splits = split(var_line, '\t');
        if (splits.size() <= 0)
            continue;

        // TODO VCFs have headers that begin with an octothorpe.
        // only process lines that do not begin with an octothorpe
        if (splits[0][0] != '#'){
                // TODO Grab relevant subsequence from reference.
                seq = fr.getSequence(splits[0]);
                cout << ">" << splits[0][0] << endl;
                cout << seq << endl;
                // TODO Inject the desired mutation into the subsequence and return
                // the modified sequence.
                // if (DEL) in splits[7]:
                //  make_deletion(dest_seq, start, len)
                //elif (INS):
                //
                //elif (DUP):
                //
                //elif (INV):
                //
                //elif (CNV):
                //
                //TODO ME subtypes
                //
                //must be a SNP
                //elif (splits[3].size() == 1 && splits[4].size() == 1){
                //
                //}
                // Append the modified sequence to the output.
        }
    }
    return 0;
}


