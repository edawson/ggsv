import random
import math
import argparse
from collections import defaultdict

mutation_types = ["deletion", "insertion", "inversion"]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--genome", type = str, dest="genome", required = True)
    parser.add_argument("-n", "--num-muts", type = int, dest="num_muts", default = 10, required = False)
    parser.add_argument("-l", "--max-len", type = int, default = 1500, dest="max_len", required = False)
    return parser.parse_args()

def rand_mut(start, max_pos, max_len, min_len = 5):
    random.seed()
    t = random.sample(mutation_types, 1)[0]
    pos = math.floor(random.uniform(start, max_pos))
    length = math.floor(random.uniform(min_len, min(max_len, max_pos - start)))
    random.seed(42)
    return pos, length, t

def legal(first, second):
    tmp = None
    if first[0] > second[0]:
        tmp = second
        second = first
        first = tmp

    return (first[0] + first[1] < second[0])


def mutate(seq_name, seq_len, num_muts, maxlen):
    current_genome_length = seq_len
    current_mut_count = 0
    

    start = 0
    muts = []

    ## Produce a random list of mutations within the genome,
    ## but do no checking about whether they overlap
    while current_mut_count < num_muts:
        mut = rand_mut(start, seq_len, maxlen)
        current_mut_count += 1
        muts.append(mut)

    muts.sort(key=lambda x : x[0])
    for i in range(0, len(muts) - 1):
        if legal(muts[i], muts[i + 1]):
            continue
        else:
            current_mut = muts[i]
            m = rand_mut(current_mut[0], muts[i + 1][0] - 1, maxlen) 
            muts[i] = m

    return muts



if __name__ == "__main__":
    random.seed(42) 
    args = parse_args()
    seq_dict = defaultdict(str)
    seq_length_dict = defaultdict(int)
    with open(args.genome, "r") as ifi:
        current_key = ""
        for line in ifi:
            if line.startswith(">"):
                current_key = line.strip().strip(">")
                seq_dict[ current_key ] = ""
                seq_length_dict[ current_key ] = 0
            else:
                seq_dict[current_key] += line.strip()
                seq_length_dict[current_key] += len(line.strip())

    for i in seq_length_dict:
        muts = mutate(i, seq_length_dict[i], args.num_muts, args.max_len)
        for j in muts:
            print("\t".join([str(j[2]), i, str(j[0]), str(j[1])]))
        


    #for i in seq_length_dict:
    #    mut_dict = mutate(i, seq_length_dict(i), args.num_muts, args.maxlen)
    #    for j in mut_dict:
    #        print (mut_dict[j])
