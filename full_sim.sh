python sim_random_data.py -s 42 -f hpv_16.fa -d hpv_descript.txt > mod.hpv.fa && \
python descrip_to_vcf.py hpv_descript.txt > hpv.vcf && \
head -n 2 mod.hpv.fa > sing.fa && \
../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i sing.fa -f 200 -l 125 -m 700 -s 50 -o sangle_alt && \
rm *.fai && \
../vg/bin/vg construct -r hpv_16.fa -v hpv.vcf -S -I mod.hpv.fa -a -f -m 32 > hpv.vg && \
../vg/bin/vg index -x hpv.xg -g hpv.gcsa hpv.vg -k 11 && \
echo "Beginning mapping" && \
time ../vg/bin/vg map -t 4 -f sangle_alt1.fq -f sangle_alt2.fq -x hpv.xg -g hpv.gcsa > hpv.gam && \
time ../vg/bin/vg genotype -F hpv_16.fa -I mod.hpv.fa -V hpv.vcf -G hpv.gam hpv.vg x > recall.vcf && \
cat recall.vcf


#time ../vg/bin/vg map -t 4 -f sangle_alt1.fq -f sangle_alt2.fq -x hpv.xg -g hpv.gcsa > hpv.gam && \
#time ../vg/bin/vg map -t 4 -f sangle_alt1.fq -x hpv.xg -g hpv.gcsa > hpv.gam && \
