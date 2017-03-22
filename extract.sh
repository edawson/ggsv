samtools view -h $1 \
    | lumpy-sv/scripts/extractSplitReads_BwaMem -i stdin \
    | samtools view -Shb - \
    > sample.splitters.bam &&
    samtools sort sample.splitters.bam -o `basename $1 .bam`.splitters.sorted.bam
