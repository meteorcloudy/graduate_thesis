jobname=thesis
./clean.sh
rm $jobname.pdf
pdflatex -shell-escape ./$jobname.tex
./clean.sh
clear
