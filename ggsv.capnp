@0xec1eb48f4f0a275d;
struct Graph{
	nodes @0 :List(Node);
	edges @1 :List(Edge);
	paths @2 :List(Path);
}

struct Node{
	sequence @0 :Text;
	name @1 :Text;
	id @2 :UInt64;
	data @3 :Data;
}

struct Edge{
	source @0 :UInt64;
	sink @1 :UInt64;
	fromSource @2 :Bool;
	toSink @3 :Bool;
	data @4 :Data;
}

struct Info{
	id @0 :Text;
	str @1 :Text;
	int @2 :Int64;
	data @3 :Data;
}

struct Edit{
	fromLength @0 :Int32;
	toLength @1 :Int32;
	sequence @2 :Text;
}

struct Mapping{
	position @0 :Position;
	edits @1 :List(Edit);
	isReverese @2 :Bool;
}

struct Position{
	nodeId @0 :UInt64;
	offset @1 :UInt64;
}

struct Path{
	name @0 :Text;
	mapping @1 :List(Mapping);
}

struct Alignment{
	sequence @0 :Text;
	path @1 :Path;
	name @2 :Text;
	quality @3 :Data;
	mappingQuality @4 :Int32;
	score @5 :Int32;
	queryPosition @6 :Int32;
	isReverse @7 :Bool;
	sampleName @8 :Text;
	readGroup @9 :Text;
	prevGragment @10 :Alignment;
	nextFragment @11 :Alignment;
	data @12 :Data;
	isSecondary @13 :Bool;
}

struct Fragment{
	alignments @0 :List(Alignment);
}

struct KmerMatch{
	sequence @0 :Text;
	nodeId @1 :UInt64;
	position @2 :Int32;
	isBackward @3 :Bool;
}

struct BasePileup{
	refBase @0 :Int32;
	numBases @1 : Int32;
	bases @2 :Text;
	qualities @3 :Data;
}

struct NodePileup{
	nodeId @0 :UInt64;
	basePileups @1 :List(BasePileup);
}
