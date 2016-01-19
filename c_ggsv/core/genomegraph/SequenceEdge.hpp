/*
 * SequenceEdge.hpp
 *
 *  Created on: Oct 22, 2015
 *      Author: dawsonet
 */

#ifndef CORE_GENOMEGRAPH_SEQUENCEEDGE_HPP_
#define CORE_GENOMEGRAPH_SEQUENCEEDGE_HPP_
#include "SequenceGraph.hpp"
#include "SequenceNode.hpp"

namespace GenomeGraph{
class SequenceEdge{
	public:
		SequenceEdge();
		SequenceNode* get_source();
		SequenceNode* get_sink();
	private:
		uint64_t id;
		SequenceNode* source;
		SequenceNode* sink;
};

}


#endif /* CORE_GENOMEGRAPH_SEQUENCEEDGE_HPP_ */
