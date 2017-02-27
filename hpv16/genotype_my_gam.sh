vg=../vg/bin/vg

${vg} index -d mapped.gam.index -N mapped.gam
${vg} genotype ref.vg mapped.gam.index -v -a augmented.vg 2> /dev/null > mapped.vcf
