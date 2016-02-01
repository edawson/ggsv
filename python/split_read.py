import re
import multiprocessing


def parse_gam(gamfile):
    raise Error()

def is_split(read):
    raise Error()

def get_position(read):
    raise Error()

if __name__ == "__main__":
    gam = sys.argv[1]
    aligned = parse_gam(gam)
    ## iterate over reads - look for those that align to multiple regions
