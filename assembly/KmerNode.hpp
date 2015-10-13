/*
 * KmerNode.hpp
 *
 *  Created on: Oct 13, 2015
 *      Author: dawsonet
 */

#ifndef ASSEMBLY_KMERNODE_HPP_
#define ASSEMBLY_KMERNODE_HPP_

#include <string>
#include <vector>

class KmerNode{
public:
	int get_color();
	int set_color(int color);

	std::vector<std::string> kmerize();
	KmerNode merge(KmerNode otherNode);
private:
	int color;
	std::string sequence;


};

#endif /* ASSEMBLY_KMERNODE_HPP_ */
