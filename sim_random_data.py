import argparse
import random
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fasta", dest="fasta", required=False)
    parser.add_argument("-t", "--type", type=str, dest="type", default=[""], required=False, nargs='+', help="One or several of del, ins, tand, trans to insert into sequence")
    parser.add_argument("-s", "--seed", type=int, dest="seed", required=False, default=42)
    parser.add_argument("-p", "--start", type=int, dest="start", required=False, default=0)
    parser.add_argument("-l", "--length", type=int, dest="length", required=False, default=0)
    parser.add_argument("-d", "--descrip", type=str, dest="descrip", required=False)
    parser.add_argument("-g", "--genome-length", type=int, dest="genomelen", required=False, default=10000)



    return parser.parse_args()

def random_seq(size):
    alph = "ACTG"
    return "".join(random.choice(alph) for i in xrange(size))

def make_insertion(seq, start, size):
    ins = random_seq(size)
    return "".join([seq[0:start], ins, seq[start+size:]]), ins


def make_deletion(seq, start, size):
    if start > len(seq):
        raise Exception("Start of variant must fall within sequence length.")
    return "".join([seq[:start], seq[start+size:]])

def make_tandem_duplication(seq, rpt,  start, size):
    tand = seq[start:size]
    tand = "".join( [ tand for i in xrange(0,rpt)])
    return "".join( [seq[:start], tand, seq[start + size:] ] )

def make_balanced_translocation(src, dest, start_src, start_dest, size, reciprocal=False):
    return


def make_unbalanced_translocation(src, dest, start_src, start_dest, size):
    return


def parse_fa(infile):
    name = ""
    seq = ""
    with open(infile, "r") as ifi:
        for line in ifi:
            if line.startswith(">"):
                name = line.strip()
            else:
                seq += line.strip()
    return name, seq

if __name__ == "__main__":
    #random.seed(args.seed)
    insertion_tracker = {}
    args = parse_args()

    start = args.start
    size = args.length

    if args.seed is not None:
        random.seed(int(args.seed))


    fafi = None
    out_seq = None

    if args.fasta is not None:
        fafi = parse_fa(args.fasta)
    else:
        fafi = ("Random", random_seq(args.genomelen))

    with open(fafi[0].strip(">") + ".original.fa", "w") as unmodded:
        unmodded.write( ">" + fafi[0] + "\n")
        unmodded.write(fafi[1] + "\n")


    ## variant description file
    ## it's pretty much a bed file
    ## varType contig startPos size optInsertionSequence
    offset = 0
    if args.descrip is not None:
        outvar = fafi[1]
        with open(args.descrip, "r") as ifi:
            for line in ifi:
                tokens = line.strip().split()
                if tokens[0] == "deletion":
                    outvar = make_deletion(outvar, int(tokens[2]), int(tokens[3]))
                elif tokens[0] == "insertion":
                    ins = make_insertion(outvar, int(tokens[2]), int(tokens[3]))
                    outvar = ins[0]
                    insertion_tracker[ "_".join( [str(tokens[2]), str(tokens[3]) ])] = ins[1]
                    pass
                elif tokens[0] == "tandem_duplication":
                    pass
                elif tokens[0] == "translocation":
                    pass
        print ">", fafi[0], "\n", outvar
        for i in insertion_tracker:
            print ">", i, "\n", insertion_tracker[i]

    if "ins" in args.type:
        out_seq = make_insertion(fafi[1], start, size)
        print out_seq

    elif "del" in args.type:
        out_seq = make_deletion(fafi[1], start, size)
        print fafi[0], "\n", out_seq

    elif "tand" in args.type:
        out_seq = make_tandem_duplication(fafi[1], start, size)
        print fafi[0], "\n", out_seq

    elif "trans" in args.type:
        out_seq = make_translocation(fafi[1], fafi[1], start, start+size, size)
        print fafi[0], "\n", out_seq
