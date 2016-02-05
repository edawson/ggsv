import vg_pb2
from collections import namedtuple


class SV:
    def __init__(self):
        return

class Evidence:
    def __init__(self):
        return

def parse_gam(gam):
    return

def parse_gam_json(gamfile):
    return

def write_vcf_header():
    return

def write_vcf(variants):
    return

def reverse_alignment():
    return

def parse_fastq_file(fastq_file):
    FASTQRecord = namedtuple("FASTQRecord", "id, sequence, annotation, score")
    i = 0
    records = {}
    rec = None
    iden = ""
    seq = ""
    anno = ""
    scr = ""
    with open(fastq_file, "r") as ffi:
        for line in ffi:
            i += 1
            if i % 4 == 1:
               iden = line.strip().strip("@")
                #rec = FASTQRecord(id=line.strip().strip("@"), sequence="", annotation="", score="")
            elif i % 4 == 2:
                seq = line.strip()
                #rec.sequence = line.strip()
            elif i % 4 == 3:
                anno = line.strip().strip("+")
                #rec.annotation = line.strip().strip("+")
            elif i % 4 == 0:
                scr = line.strip()
                #rec.score = line.strip()
                rec = FASTQRecord(id = iden, sequence = seq, annotation = anno, score = scr)
                iden = ""; seq = ""; anno = ""; scr = ""
                yield rec
    #return records
