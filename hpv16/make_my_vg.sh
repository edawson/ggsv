vg=../vg/bin/vg
ref=hpv_16.fa


${vg} construct -m 400 -r ${ref} > ref.vg
${vg} index -x ref.xg -g ref.gcsa -k 12 ref.vg
