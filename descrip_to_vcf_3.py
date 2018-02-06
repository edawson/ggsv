import sys


##  CHROM POS ID REF ALT QUAL FILTER INFO
if __name__ == "__main__":
    header = "##fileformat=VCFv4.0\n"
    header += "##source=ggsv\n"
    #header += "##reference="
    header += "##INFO=<ID=SVTYPE,Number=1,Type=String,Description=\"SV Type\">\n"
    header += "##INFO=<ID=SVLEN,Number=1,Type=String,Description=\"SV length\">\n"
    header += "##INFO=<ID=END,Number=1,Type=String,Description=\"SV End\">\n"
    header += "##CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO"

    print( header)
    
    ## insertion HPV16 100 10
    offset = 0
    with open(sys.argv[1], "r") as ifi:
        for line in ifi:
            tokens = line.strip().split()
            if tokens[0] == "deletion":
                pos = str( int(tokens[2]) + offset )
                #offset -= int(tokens[3])
                svlen_str = "SVLEN=" + tokens[3]
                end_str = "END=" + str( int(tokens[2]) + offset + int(tokens[3]))
                svtype_str = "SVTYPE=" + "DEL"
                info_str = ";".join( [svlen_str, svtype_str, end_str] )
                varlist = [tokens[1], pos, ".", "A", "<DEL>", "99", "PASS", info_str]
                print( "\t".join( varlist ))
            elif tokens[0] == "insertion":
                pos = str( int(tokens[2]) + offset )
                #offset += int(tokens[3])
                svlen_str = "SVLEN=" + tokens[3]
                svtype_str = "SVTYPE=" + "INS"
                end_str = "END=" + str( int(tokens[2]) + offset + int(tokens[3]))
                info_str = ";".join( [svlen_str, svtype_str, end_str] )
                alt_str = "<" + "_".join([ tokens[2], tokens[3] ]) + ">"
                varlist = [tokens[1], pos, ".", "A", alt_str , "99", "PASS", info_str]
                print( "\t".join( varlist ))
            elif tokens[0] == "tandem_duplication":
                pass
            elif tokens[0] == "translocation":
                pass
            elif tokens[0] == "inversion":
                pos = str( int(tokens[2]) + offset )
                #offset += int(tokens[3])
                svlen_str = "SVLEN=" + tokens[3]
                svtype_str = "SVTYPE=" + "INV"
                end_str = "END=" + str( int(tokens[2]) + offset + int(tokens[3]))
                info_str = ";".join( [svlen_str, svtype_str, end_str] )
                alt_str = "<" + "INV" + ">"
                varlist = [tokens[1], pos, ".", "A", alt_str , "99", "PASS", info_str]
                print( "\t".join( varlist ))
