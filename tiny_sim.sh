python sim_random_data.py -s 43 -g 1000 -d tiny_descrip > mod.tiny.fa && \
mv Random.original.fa tiny.fa && \
python descrip_to_vcf.py tiny_descrip > tiny.vcf && \
gsed -i "s/Random/tiny/g" mod.tiny.fa && \
gsed -i "s/Random/tiny/g" tiny.fa && \
gsed -i "s/Random/tiny/g" tiny.vcf && \
head -n 2 mod.tiny.fa > tiny.mod.fa && \
../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i tiny.mod.fa -f 10 -l 125 -m 700 -s 50 -o tiny.alt && \
../art_bin_MountRainier/art_illumina -ss HS25 -p -na -i tiny.fa -f 10 -l 125 -m 700 -s 50 -o tiny.ref && \
rm *.fai *.gam && \
../vg/bin/vg construct -r tiny.fa -v tiny.vcf -S -I mod.tiny.fa -a -f -m 32 > tiny.vg && \
../vg/bin/vg index -x tiny.xg -g tiny.gcsa tiny.vg -k 11 && \
echo "Beginning mapping" && \
time ../vg/bin/vg map -t 4 -f alt1.fq -f alt2.fq -x tiny.xg -g tiny.gcsa > alt.gam && \
time ../vg/bin/vg map -t 4 -f ref1.fq -f ref2.fq -x tiny.xg -g tiny.gcsa > ref.gam && \
cat ref.gam alt.gam > het.gam && \
time ../vg/bin/vg genotype -F tiny.fa -I mod.tiny.fa -V tiny.vcf -G alt.gam tiny.vg x > recall.alt.vcf && \
cat recall.alt.vcf
