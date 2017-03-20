import sys
import random

def get_mut(max_genome_len, prev_pos, type_l, prev_len, maxvarlen):
# Get a random position between the last variant and the end of the genome
    geno_len = max_genome_len
    if (geno_len <= prev_pos + prev_len + 1):
        geno_len += 1500
    curr_pos = random.randint(prev_pos + prev_len + 1, geno_len)
    mtype = type_l[random.randint(0,len(type_l) - 1)]
    msize = random.randint(10, maxvarlen)
# Get a random size, less than the end of the genome
# but if the genome is too small, just extend it
    if geno_len < curr_pos + msize + 1000:
        geno_len = random.randint(curr_pos + msize, curr_pos + msize + 1000)
    mut_string = " ".join( [mtype, gen_name, str(curr_pos), str(msize)] ) 
    return mut_string, curr_pos, msize, geno_len

if __name__ == "__main__":
    gen_name = "Random"    
    num_muts = int(sys.argv[1])
    prev_pos = 0
    prev_len = 0
    maxvarlen = 1500
    type_l = ["insertion","deletion", "inversion"]
    geno_len = 10000
    for i in xrange(0, num_muts):
        m, cpos, plen, glen = get_mut(geno_len, prev_pos, type_l, prev_len, maxvarlen)
        print m
        geno_len = glen
        prev_pos = cpos
        prev_len = plen
