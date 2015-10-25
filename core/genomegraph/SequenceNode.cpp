/*
 * SequenceGraph.cpp
 *
 *  Created on: Oct 22, 2015
 *      Author: dawsonet
 */

#include "SequenceNode.hpp"
#include "SequenceEdge.hpp"
#include "SequencePosition.hpp"

namespace GenomeGraph{

	using namespace std;



SequenceNode::SequenceNode() {
	id = 0;
	sequence = "";
	position = NULL;
}

SequenceNode::SequenceNode(uint64_t id, string sequence,
		SequencePosition sp) {
	this->id = id;
	this->sequence = sequence;
	this->position = sp;
}

SequenceNode SequenceNode::split_node(long posStart, long posEnd) {
}

SequenceNode SequenceNode::merge_node(SequenceNode other, long posStart,
		long posEnd) {
}

SequenceEdge* SequenceNode::add_neighbor(SequenceNode* neighbor) {
}

void SequenceNode::set_sequence(std::string sequence) {
}

void SequenceNode::set_id(uint64_t id) {
}

void SequenceNode::set_position(SequencePosition sp) {
}

std::string SequenceNode::get_sequence() {
}

uint64_t SequenceNode::get_id() {
}

SequencePosition SequenceNode::get_position() {
}
}
