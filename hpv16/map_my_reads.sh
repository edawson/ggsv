vg=../vg/bin/vg
graph=
reads_1=$1
reads_2=$2
gammy=mapped.gam

${vg} map -t 2 -x ref.xg -g ref.gcsa -f ${reads_1} -f ${reads_2} > ${gammy}
