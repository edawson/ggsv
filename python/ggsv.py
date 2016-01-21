import argparse
import soft_clip
import vg_pb2
import split_read
import fragment_pair

def parse_args():
    parser = argparse.ArgumentParser();
    parser.add_argument("-i", dest="infile", required=True, type=str)
    parser.add_argument("-c", dest="cores", required=False, type=int, default=1)
    return parser.parse_args()


if __name__ == "__main__":
    print "Testing"
## Read in VG proto file.

## look for soft clips, split reads, or related fragments
## based on user input.
