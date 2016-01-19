/*
 * SequenceGraph.hpp
 *
 *  Created on: Oct 13, 2015
 *      Author: dawsonet
 */

#ifndef CORE_SEQUENCEGRAPH_HPP_
#define CORE_SEQUENCEGRAPH_HPP_
#include <vector>
#include <unordered_map>
#include <list>
#include <cstdint>
#include <fstream>
#include <iostream>
#include "SequenceGraph.hpp"

namespace GenomeGraph{
using namespace std;
	class SequenceGraph{
		public:

			SequenceGraph::SequenceGraph();
	//        SequenceGraph::SequenceGraph(istream& in);
			uint64_t get_new_node_id();
			uint64_t get_new_edge_id();
			std::unordered_map<uint64_t, *SequenceNode> get_nodes();
			std::unordered_map<uint64_t, *SequenceEdge> get_edges();
			SequenceGraph::~SequenceGraph(void);
			SequenceGraph::SequenceGraph build(string filename);
			SequenceGraph::SequenceGraph project_mutations(string mut_file, SequenceGraph sg);
		private:
			void init(void);
			std::unordered_map<uint64_t, *SequenceNode> nodes;
			std::unordered_map<uint64_t, *SequenceEdge> edges;
			uint64_t edge_id_counter;
			uint64_t node_id_counter;
			std::unordered_map<SequencePosition, list<SequenceNode> > pileup;
	};







};
#endif /* CORE_SEQUENCEGRAPH_HPP_ */
