filename=acoustic

bib:
	bibtex ${filename}||true

nomencl:
	makeindex ${filename}.nlo -s nomencl.ist -o ${filename}.nls -t ${filename}.nlg

pdf:
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode ${filename}.tex

lilypond:
	lilypond-book --pdf ${filename}.lytex

read:
	evince ${filename}.pdf &

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg}

all:
	make pdf
	make bib
	make pdf
	make pdf
	make read
