## Original VCF
echo "OG vcf has $(grep -cv "#" mega.vcf) variants"
echo "$(grep -v "#" mega.vcf | grep -c "INS") INS"
echo "$(grep -v "#" mega.vcf | grep -c "DEL") DEL"
echo "$(grep -v "#" mega.vcf | grep -c "INV") INV"
echo

## Print times:

## vg recall
echo "VG recall will spit back all variants, but how well does it type them?"
echo "Of $(grep -v "#" recall.alt.mega.vcf | grep -c "INS") insertions, $(grep "INS" recall.alt.mega.vcf | grep -c "1/1") are labeled hom alt."
echo "Of $(grep -v "#" recall.alt.mega.vcf | grep -c "DEL") deletions, $(grep "DEL" recall.alt.mega.vcf | grep -c "1/1") are labeled hom alt."
echo "Of $(grep -v "#" recall.alt.mega.vcf | grep -c "INV") inversions, $(grep "INV" recall.alt.mega.vcf | grep -c "1/1") are labeled hom alt."

echo 
## Delly

echo "DELLY INS calls $(bcftools view alt.ins.sv.delly.bcf | grep -cv "#") variants"
echo "$(bcftools view alt.ins.sv.delly.bcf | grep -v "#" |grep -c "INS") INS, $(bcftools view alt.ins.sv.delly.bcf | grep -v "#" | grep "INS" | grep -c "1/1") homozygous alt."
echo

echo "DELLY DEL calls $(bcftools view alt.del.sv.delly.bcf | grep -cv "#") variants"
echo "$(bcftools view alt.del.sv.delly.bcf | grep -v "#" |  grep -c "DEL") DELs, $(bcftools view alt.del.sv.delly.bcf | grep -v "#" |  grep "DEL" | grep -c "1/1") homozygous alt."
echo


echo "DELLY INV calls $(bcftools view alt.inv.sv.delly.bcf | grep -cv "#") variants"
echo "$(bcftools view alt.inv.sv.delly.bcf | grep -v "#" | grep -c "INV") INV, $(bcftools view alt.inv.sv.delly.bcf | grep -v "#" | grep "INV" | grep -c "1/1") homozygous alt."
echo

echo "Delly's regenotype calls $(bcftools view alt.regenotype.delly.bcf | grep -v "#" | grep -c "DEL") deletions, $(bcftools view alt.regenotype.delly.bcf |  grep -v "#" | grep "DEL" | grep -c "1/1") are hom alt."
echo "Delly's regenotype calls $(bcftools view alt.regenotype.delly.bcf | grep -v "#" | grep -c "INS") insertions, $(bcftools view alt.regenotype.delly.bcf | grep -v "#" | grep "INS" | grep -c "1/1") are hom alt."
echo
## Lumpy + SVTYPER
echo "Lumpy calls $(grep -cv "#" alt.lumpy.vcf) variants, and SVTYPE spits out $(grep -cv "#" alt.svtyper.vcf)"
echo "This many insertions: $(grep -v "#" alt.svtyper.vcf | grep -c "INS"), and $(grep "INS" alt.svtyper.vcf | grep -v "#" | grep -c "1/1") hom alts"
echo "This many deletions: $(grep -v "#" alt.svtyper.vcf | grep -c "DEL"), and $(grep "DEL" alt.svtyper.vcf | grep -v "#" |  grep -c "1/1") hom alts"
echo "This many inversions: $(grep -v "#" alt.svtyper.vcf | grep -c "INV"), and $(grep "INV" alt.svtyper.vcf | grep -v "#" |  grep -c "1/1") hom alts"
