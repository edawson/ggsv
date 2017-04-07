touch x.bai x.fai x.gam && rm *.fai *.gam *.bai && \
    python gen_big_descript.py 1000 > mega_descrip.txt && \
    python sim_random_data.py -s 42 -g $(echo $(expr `tail -n 1 mega_descrip.txt | cut -f 3 -d " "` + 2000)) -d mega_descrip.txt > mod.mega.fa && \
    mv Random.original.fa mega.orig.fa && \
python descrip_to_vcf.py mega_descrip.txt > mega.vcf && \
    head -n 2 mod.mega.fa > mega.sing.fa && \
    ../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i mega.sing.fa -f 20 -l 125 -m 700 -s 50 -o alt && \
    ../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i mega.orig.fa -f 20 -l 125 -m 700 -s 50 -o ref && \
    ../vg/bin/vg construct -r mega.orig.fa -v mega.vcf -S -I mod.mega.fa -a -f -m 32 > mega.vg && \
    ../vg/bin/vg index -x mega.xg -g mega.gcsa mega.vg -k 11 && \
    echo "Beginning mapping" && \
    time ../vg/bin/vg map -t 4 -f alt1.fq -f alt2.fq -x mega.xg -g mega.gcsa > alt.mega.gam && \
    time ../vg/bin/vg map -t 4 -f ref1.fq -f ref2.fq -x mega.xg -g mega.gcsa > ref.mega.gam && \
    cat ref.mega.gam alt.mega.gam > het.gam
time ../vg/bin/vg genotype -F mega.orig.fa -I mod.mega.fa -V mega.vcf -G alt.mega.gam mega.vg x > recall.alt.mega.vcf && \

## Run DELLY
time ./bwa/bwa index mega.orig.fa && \
    time ./bwa/bwa mem -R '@RG\tID:alt\tSM:alt' mega.orig.fa alt1.fq alt2.fq | samtools view -bSh - > alt.bam && \
    sambamba sort alt.bam && \
    echo "Delly deletions: " && \
    time ./delly/src/delly call -t DEL -g mega.orig.fa alt.sorted.bam -o alt.del.sv.delly.bcf && \
    echo "Delly insertions: " && \
    time ./delly/src/delly call -t INS -g mega.orig.fa alt.sorted.bam -o alt.ins.sv.delly.bcf && \
     echo "Delly inversion: " && \
    time ./delly/src/delly call -t INV -g mega.orig.fa alt.sorted.bam -o alt.inv.sv.delly.bcf && \
    echo "Delly recall" && \
    time ./delly/src/delly call -v recall.alt.mega.vcf -g mega.orig.fa alt.sorted.bam -o alt.regenotype.delly.bcf && \

## Run LUMPY
./extract.sh alt.bam && \
    time sambamba view -h --num-filter /1294 alt.sorted.bam | samtools sort -@ 2 -o alt.discords.sorted.bam /dev/stdin && \
    echo "Lumpy: " && \
    time ./lumpy-sv/bin/lumpyexpress -B alt.bam -D alt.discords.sorted.bam -S alt.splitters.sorted.bam -o alt.lumpy.vcf && \
    echo "SVTYPER: " && \
    time ./svtyper/svtyper -i alt.lumpy.vcf -B alt.sorted.bam -o alt.svtyper.vcf

exit

