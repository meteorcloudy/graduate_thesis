rm *.pdf
./clean.sh
for file in $(ls *.tex); do
	pdflatex $file
done
./clean.sh
