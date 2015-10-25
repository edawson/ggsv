/*
 * SequenceNode.hpp
 *
 *  Created on: Oct 22, 2015
 *      Author: dawsonet
 */

#ifndef CORE_GENOMEGRAPH_SEQUENCENODE_HPP_
#define CORE_GENOMEGRAPH_SEQUENCENODE_HPP_


namespace GenomeGraph{
	class SequenceNode{
		public:
			SequenceNode();
			SequenceNode(uint64_t id, string sequence, SequencePosition sp);
			SequenceNode split_node(long posStart, long posEnd);
			SequenceNode merge_node(SequenceNode other, long posStart, long posEnd);
			SequenceEdge* add_neighbor(SequenceNode* neighbor);
			void set_sequence(std::string sequence);
			void set_id(uint64_t id);
			void set_position(SequencePosition sp);
			std::string get_sequence();
			uint64_t get_id();
			SequencePosition get_position();
		private:
			std::string sequence;
			uint64_t id;
			std::unordered_map<uint64_t, *SequenceEdge> edges;
			SequencePosition position;
	};
};
#endif /* CORE_GENOMEGRAPH_SEQUENCENODE_HPP_ */
