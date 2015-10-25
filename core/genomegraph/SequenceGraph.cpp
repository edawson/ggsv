/*
 * SequenceGraph.cpp
 *
 *  Created on: Oct 22, 2015
 *      Author: dawsonet
 */

#include "SequenceGraph.hpp"
#include "SequenceNode.hpp"
#include <cstdint>

namespace GenomeGraph{
using namespace std;

void init(void){

}

GenomeGraph::SequenceGraph::SequenceGraph::SequenceGraph() {
	node_id_counter = 0;
	edge_id_counter = 0;
	edges = unordered_map<uint64_t, *SequenceEdge> ();
	nodes = unordered_map<uint64_t, *SequenceNode> ();
}

//TODO
SequenceGraph::SequenceGraph build(string fasta_name, SequenceGraph sg){
	// Open fasta file

	//For seq in fasta,
	//	build a node for seq
	//	return new SeqGraph
	return NULL;
}

//TODO
SequenceGraph::SequenceGraph project_mutations(string mut_file, SequenceGraph sg){
	//For record in VCF
	//	split/merge fasta nodes to make new paths in the graph
	//	return a new SeqGraph
	return NULL;
}
//TODO Destructor
SequenceGraph::~SequenceGraph(void){

}

uint64_t GenomeGraph::SequenceGraph::get_new_node_id() {
	return (++node_id_counter);
}

uint64_t GenomeGraph::SequenceGraph::get_new_edge_id() {
	return (++edge_id_counter);
}

std::unordered_map<uint64_t, *SequenceNode> GenomeGraph::SequenceGraph::get_nodes() {
	return nodes;
}

std::unordered_map<uint64_t, *SequenceEdge> GenomeGraph::SequenceGraph::get_edges() {
	return edges;
}

}
