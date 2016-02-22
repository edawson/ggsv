import vg_pb2
from collections import namedtuple


class SV:
    def __init__(self):
        return

class Evidence:
    def __init__(self):
        return

def generate_gam_alignment(gam):
	with open(gam, "r") as gfi:
    return

def parse_gam_json(gamfile):
	with open(gamfile, "r") as gfi:
		for line in gfi:
			j_rec = json.loads(line)
			seq = jrec["sequence"]
			quals = j_rec["quality"]
			path = j_rec["path"]
		    #mapping = path["mapping"]
			Alignment = namedtuple("Alignment", "sequence quality path")
			yield Alignment(seq, quals, path)

def write_vcf_header():
	ret = ""
	ret += "##Version=VCF4.1\n"
	ret += "##Source=ggsv\n"
	ret+="CHROM\tPOS\tID\tALT\tREF\tQual\n"
    return ret

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
