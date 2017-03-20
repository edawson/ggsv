touch x.gam && \
touch x.fai && \
python sim_random_data.py -s 42 -f hpv_16.fa -d hpv_descript.txt > mod.hpv.fa && \
python descrip_to_vcf.py hpv_descript.txt > hpv.vcf && \
head -n 2 mod.hpv.fa > sing.fa && \
../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i sing.fa -f 50 -l 125 -m 700 -s 50 -o alt && \
../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i hpv_16.fa -f 50 -l 125 -m 700 -s 50 -o ref && \
rm *.fai && \
../vg/bin/vg construct -r hpv_16.fa -v hpv.vcf -S -I mod.hpv.fa -a -f -m 32 > hpv.vg && \
../vg/bin/vg index -x hpv.xg -g hpv.gcsa hpv.vg -k 11 && \
echo "Beginning mapping" && \
time ../vg/bin/vg map -t 4 -f alt1.fq -f alt2.fq -x hpv.xg -g hpv.gcsa > alt.gam 2> map.vg.time.txt && \
time ../vg/bin/vg map -t 4 -f ref1.fq -f ref2.fq -x hpv.xg -g hpv.gcsa > ref.gam && \
cat ref.gam alt.gam > het.gam
../vg/bin/vg index -d alt.gam.index -N alt.gam && \
../vg/bin/vg index -d ref.gam.index -N ref.gam && \
../vg/bin/vg index -d het.gam.index -N het.gam && \
echo "VG Recall: "
time ../vg/bin/vg genotype -F hpv_16.fa -I mod.hpv.fa -V hpv.vcf -G alt.gam hpv.vg x > recall.alt.vcf && \
cat recall.alt.vcf

## Run DELLY
time ./bwa/bwa mem -R '@RG\tID:alt\tSM:alt' hpv_16.fa alt1.fq alt2.fq | samtools view -bSh - > alt.tmp.bam && \
sambamba sort -o alt.bam alt.tmp.bam && \
echo "Delly deletions: " && \
time ./delly/src/delly call -t DEL -g hpv_16.fa alt.bam -o alt.del.sv.delly.bcf && \
echo "Delly insertions: " && \
time ./delly/src/delly call -t INS -g hpv_16.fa alt.bam -o alt.ins.sv.delly.bcf && \
echo "Delly recall" && \
time ./delly/src/delly call -v recall.alt.vcf -g hpv_16.fa alt.bam -o alt.regenotype.delly.bcf
#bcftools view alt.del.sv.delly.bcf && \
#bcftools view alt.ins.sv.delly.bcf && \
#bcftools view alt.regenotype.delly.bcf

## Run LUMPY
./extract.sh alt.bam && \
time sambamba view -h --num-filter /1294 alt.bam | samtools sort -@ 2 -o alt.discords.bam - && \
echo "Lumpy: " && \
time ./lumpy-sv/bin/lumpyexpress -B alt.bam -D alt.discords.bam -S alt.splitters.bam -o alt.lumpy.vcf && \
echo "SVTYPER: " && \
time ./svtyper/svtyper -i alt.lumpy.vcf -B alt.bam -o alt.svtyper.vcf
#cat alt.svtyper.vcf

#time ../vg/bin/vg genotype -C -v -r HPV16 hpv.vg alt.gam.index > alt.geno.vcf && \
#time ../vg/bin/vg genotype -C -v -r HPV16 hpv.vg ref.gam.index > ref.geno.vcf && \
#time ../vg/bin/vg genotype -C -v -r HPV16 hpv.vg het.gam.index > het.geno.vcf


#time ../vg/bin/vg map -t 4 -f sangle_alt1.fq -f sangle_alt2.fq -x hpv.xg -g hpv.gcsa > hpv.gam && \
#time ../vg/bin/vg map -t 4 -f sangle_alt1.fq -x hpv.xg -g hpv.gcsa > hpv.gam && \
