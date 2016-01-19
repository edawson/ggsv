/*
 * SequencePosition.hpp
 *
 *  Created on: Oct 22, 2015
 *      Author: dawsonet
 */

#ifndef CORE_GENOMEGRAPH_SEQUENCEPOSITION_HPP_
#define CORE_GENOMEGRAPH_SEQUENCEPOSITION_HPP_
#include <cstdint>

namespace GenomeGraph{
	class SequencePosition{
	public:
		SequencePosition(std::string contig, int strand, uint32_t coord){
			this->strand = strand;
			this->contig = contig;
			this->coordinate = coord;
		}
		~SequencePosition();
		bool equals(SequencePosition other);
		bool overlaps(SequencePosition other);
		bool in_window(SequencePosition other, int window_size);
	private:
		int strand;
		uint32_t coordinate;
		std::string contig;

	};

}



#endif /* CORE_GENOMEGRAPH_SEQUENCEPOSITION_HPP_ */
