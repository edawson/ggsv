/*
 * SequenceNode.hpp
 *
 *  Created on: Oct 13, 2015
 *      Author: dawsonet
 */

#ifndef CORE_GENOMEGRAPH_SEQUENCENODE_HPP_
#define CORE_GENOMEGRAPH_SEQUENCENODE_HPP_

namespace GenomeGraph{
class SeqNode{
	public:
		SeqNode();
		SeqNode splitNode(long posStart, long posEnd);
		SeqNode mergeNode(SeqNode other, long posStart, long posEnd);
	};
};




#endif /* CORE_GENOMEGRAPH_SEQUENCENODE_HPP_ */
