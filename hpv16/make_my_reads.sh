infasta=$1
wgsim -e 0.0 -N 10000 -1 125 -2 125 -r 0.0 -S 42 -A 0.0 -h -d 600 $infasta `basename ${infasta} .fa`_1.fa `basename ${infasta} .fa`_2.fa
