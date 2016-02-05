import argparse
import soft_clip
import vg_pb2
import split_read
import fragment_pair
import multiprocessing as mp
import json
import sys
import signal
from util import parse_fastq_file

def parse_args():
    parser = argparse.ArgumentParser();
    #parser.add_argument("-i", dest="infile", required=True, type=str)
    #parser.add_argument("-a", "--analysis", dest="analysis", required)
    parser.add_argument("-t", "--threads", dest="cores", required=False, type=int, default=1)
    parser.add_argument("-s", "--svtype", dest="svtype", choices=["SR", "RP", "SC", ""], default="", required=False)
    parser.add_argument("-g", "--gam", dest="gam", required=True, type=str)
    parser.add_argument("-j", "--json", dest="json", required=False, type=bool, default=False)
    parser.add_argument("-i", "--stream", dest="stream", required=False, type=bool, default=False)
    parser.add_argument("-c", "--counts", dest="counts", required=False, type=str, default=None)
    parser.add_argument("-r", "--reads", dest="reads", required=False, type=str)
    return parser.parse_args()


## TODO deserializes protobuf
def for_each_input(s):
    return

def parse_input(infile, isJson, isStream):
    if isStream and isJson:
        for line in sys.stdin:
            yield json.loads(line)
    elif isJson:
        with open(infile, "r") as ifi:
            for line in ifi:
                yield json.loads(line)
    else:
        raise NotImplementedError

## Takes in the alignment and parses it for quals at corresponding
## bases. This is harder than it sounds.
## It then multiples the quality score at a site-edit with the depth
## from the population at that site-edit and returns a tuple
## of length site-edits
def build_qual_depth_vector(alignment, pos_edit_to_count, min_score=0.0):
    mP = make_pos
    mE = make_edit
    vec = None
    ## We'll need the quals
    quals = alignment["quality"]
    ## and the path
    path = alignment["path"]
    mapping = path["mapping"]
    ## Next up: walk the path from the beginning
    ## keep track of the distance in the read,
    ## which should stay below 8kb or so.
    ## at each edit we find, check if it's in the
    ## pos_to_edit_to_count. If it is, multiply
    ## the corresponding quality at that position
    ## by the depth at the position-edit.
    ## If no edit is present or no quality is given,
    ## place a minimum score in the cell.
    for m in mapping:

    return vec

def make_edit(edit):
    for p in edit:
        try:
            p["from_length"]
            from_length = int(p["from_length"])
        except KeyError:
            from_length = 0;
        try:
            seq = p["sequence"]
        except KeyError:
            seq = ""
        try:
            to_length = int(p["to_length"])
        except KeyError:
            to_length = 0
        return from_length, to_length, seq

## Takes an edit and filters it out if
## from_len == to_len and seq is empty
def isMatch(ed):
    if ed[0] == ed[1] and \
    ed[2] == "":
        return True
    else:
        return False

## Generates a dict of dicts of the form
## pos : edit : count
## for each alignment
## these can then be merged into a large dictionary
def build_counts(alignment):
    iM = isMatch
    mE = make_edit
    mP = make_pos
    path = alignment["path"]
    mapping = path["mapping"]
    pos_to_edit_to_count = {}
    for m in mapping:
        pos = mP(m["position"])
        ##iterate over edits
        pos_hash = "_".join([str(pos[0]), str(pos[1])])
        for e in m["edit"]:
            ed = mE(m["edit"])
            ## Only store edits that are not exact matches
#            if iM(ed):
#                continue
            e_hash = "_".join([str(ed[0]), str(ed[1]), str(ed[2])])
            if pos_hash in pos_to_edit_to_count:
                if e_hash in pos_to_edit_to_count[pos_hash]:
                    pos_to_edit_to_count[pos_hash][e_hash] += 1
                else:
                    pos_to_edit_to_count[pos_hash][e_hash] = 1
            else:
                pos_to_edit_to_count[pos_hash] = {}
                pos_to_edit_to_count[pos_hash][e_hash] = 1
    return pos_to_edit_to_count

def make_pos(pos):
    try:
        offset = int(pos["offset"])
    except KeyError:
        offset = 0
    try:
        n_id = int(pos["node_id"])
    except KeyError:
        n_id = 0
    return n_id, offset


def process_json(alignment):
    return

def parse_counts_file(count_file):
    counts_dict = {}
    with open(count_file, "r") as cfi:
        for line in cfi:
            tokens = line.strip().split("\t")
            counts_dict[tokens[0]] = {str(tokens[1]): int(tokens[2])}
    return counts_dict

def init_worker():
    signal.signal(signal.SIGINT, signal.SIG_IGN)

if __name__ == "__main__":
    args = parse_args()

    pool = mp.Pool(args.cores, init_worker)
    ## Read in VG proto file.

    data = parse_input(args.gam, args.json, args.stream)
    pos_to_edit_to_count = {}
    try:
        ## Generates a generator of dictionaries
        ## pos: edit : count
        ## that needs to be collapsed
        if (args.counts is None):
            ret = pool.imap_unordered(build_counts, data, 20)
            for a_dict in ret:
                for a_pos in a_dict:
                    if a_pos not in pos_to_edit_to_count:
                        pos_to_edit_to_count[a_pos] = a_dict[a_pos]
                    else:
                        for an_edit in a_dict[a_pos]:
                            if an_edit in pos_to_edit_to_count[a_pos]:
                                pos_to_edit_to_count[a_pos][an_edit] += 1
                            else:
                                pos_to_edit_to_count[a_pos][an_edit] = a_dict[a_pos][an_edit]
            for i in pos_to_edit_to_count:
                for j in pos_to_edit_to_count[i]:
                    print "\t".join([i, j, str(pos_to_edit_to_count[i][j])])
        ## Use a counts file for depth-based calling
        elif (args.counts is not None):
            print "Using counts file: ", args.counts
            ## Going to need the counts and the gam
            ## TODO we store counts as a DICT, is this going to be efficient for large
            ## sequences??
            pos_to_edit_to_count = parse_counts_file(args.counts)
            ## map edits in the alignments to





            ## We use a generator for this...
            ## TODO may be more efficient to load into memory if we can.
            ## TODO WHERE ARE THE QUALS IN GAM???????
            #reads = parse_fastq_file(args.reads)





    except KeyboardInterrupt:
        pool.terminate()
        pool.join()
        #raise Exception()
        exit(1)
    else:
        pool.close()
        pool.join()



## look for soft clips, split reads, or related fragments
## based on user input.
