#include <iostream>
#include <getopt.h>
#include "stream.hpp"
#include "ggsv.hpp"
#include "vg.pb.h"

using namespace std;
using namespace stream;
using namespace vg;

void print_help(){
  cerr << "ggsv [options] <aln.gam> > out.vcf" << endl;
}

int main_split_read(int argc, char** argv){
  return 1;
}

int main_soft_clip(int argc, char** argv){
  return 1;
}

int main_read_pair(int argc, char** argv){
    return 1;
}



int main(int argc, char** argv){
  int c;
  string infile;
  int threads;

  if (argc < 2){
    print_help();
    exit(0);
  }

  while (true){

    static struct option long_options[] =
    {
      {"help", no_argument, 0, 'h'},
      {"infile", required_argument, 0, 'i'},
      {0,0,0,0}
    };

    int option_index = 0;
    c = getopt_long(argc, argv, "hi:", long_options, &option_index);
    if (c == -1){
      break;
    }

    switch(c){
      case 'i':
        infile = optarg;
        break;
      case '?':
      case 'h':
        print_help();
        exit(0);

      default:
        abort();
    }
  }

  function<void(uint64_t)> handle_count = [](uint64_t count) {
    };

    // the graph is read in chunks, which are attached to this graph
    uint64_t i = 0;
    function<void(Alignment&)> lambda = [](Alignment& a) {
        cerr << a.DebugString() << endl;
      };

    ifstream in;
    in.open(infile);
    if (in.good()){
      for_each_parallel(in, lambda);
    }

      return 1;

}
