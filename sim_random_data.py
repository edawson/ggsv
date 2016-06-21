import argparse
import random
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fasta", dest="fasta", required=True)
    parser.add_argument("-t", "--type", type=str, dest="type", required=False, default=["del"], nargs='+', help="One or several of del, ins, tand, trans to insert into sequence")
    parser.add_argument("-s", "--seed", type=int, dest="seed", required=False, default=42)
    parser.add_argument("-p", "--start", type=int, dest="start", required=False, default=0)
    parser.add_argument("-l", "--length", type=int, dest="length", required=False, default=10);


    return parser.parse_args()

def random_seq(size):
    alph = "ACTG"
    return "".join(random.choice(alph) for i in xrange(size))

def make_insertion(seq, start, size):
    ins = random_seq(size)
    return "".join([seq[0:start], ins, seq[start+size:]])


def make_deletion(seq, start, size):
    return "".join([seq[:start], seq[start+size:]])

def make_translocation(src, dest, start_src, start_dest, size):
    return

def make_tandem_duplication(seq, start, size):
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
    args = parse_args()

    start = args.start
    size = args.length


    fafi = None
    out_seq = None
    if args.fasta is not None:
        fafi = parse_fa(args.fasta)

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
