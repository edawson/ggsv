python sim_random_data.py -s 42 -f hpv_16.fa -d mega_descrip.txt > mod.hpv.fa && \
python descrip_to_vcf.py mega_descrip.txt > hpv.vcf && \
head -n 2 mod.hpv.fa > sing.fa && \
../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i sing.fa -f 200 -l 125 -m 700 -s 50 -o alt && \
../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i hpv_16.fa -f 200 -l 125 -m 700 -s 50 -o ref && \
rm *.fai && \
../vg/bin/vg construct -r hpv_16.fa -v hpv.vcf -S -I mod.hpv.fa -a -f -m 32 > hpv.vg && \
../vg/bin/vg index -x hpv.xg -g hpv.gcsa hpv.vg -k 11 && \
echo "Beginning mapping" && \
time ../vg/bin/vg map -t 4 -f alt1.fq -f alt2.fq -x hpv.xg -g hpv.gcsa > alt.gam && \
time ../vg/bin/vg map -t 4 -f ref1.fq -f ref2.fq -x hpv.xg -g hpv.gcsa > ref.gam && \
cat ref.gam alt.gam > het.gam
../vg/bin/vg index -d alt.gam.index -N alt.gam && \
../vg/bin/vg index -d ref.gam.index -N ref.gam && \
../vg/bin/vg index -d het.gam.index -N het.gam && \
time ../vg/bin/vg genotype -F hpv_16.fa -I mod.hpv.fa -V hpv.vcf -G alt.gam hpv.vg x > recall.alt.vcf && \
cat recall.alt.vcf


#time ../vg/bin/vg map -t 4 -f sangle_alt1.fq -f sangle_alt2.fq -x hpv.xg -g hpv.gcsa > hpv.gam && \
#time ../vg/bin/vg map -t 4 -f sangle_alt1.fq -x hpv.xg -g hpv.gcsa > hpv.gam && \
