/*
 * ggsv.cpp
 * Main class for ggsv
 *  Created on: Oct 12, 2015
 *      Author: Eric T Dawson
 */


int main(int argc, char* argv[]);

int main(int argc, char* argv[]){
	// read in a fasta reference and build a node for each contig

	// Read in a vcf file. Look up each mutation in the nodes
	// take those nodes and inject mutations into them

	// Collate mapped/unmapped pairs and split (soft-clipped) reads.

	// for reads with only one partner within <window> bp from mutations,
	// try to map the unmapped mate into the alternative node
		// If mate-rescue fails, start assembling through the breakpoint.

	//How to detect translocations??
		// -split reads
		// -Read pair orientation mismatch (i.e. --> and --> or somesuch)

	return 1;
}



