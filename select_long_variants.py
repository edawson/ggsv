import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", dest="infile", required=True, help="A VCF file to strip long variants from")
    parser.add_argument("-l", "--min-length", dest="min_length", required=False, default=10, help="The minimum variant length to select for")

    return parser.parse_args()

if __name__ == "__main__":

