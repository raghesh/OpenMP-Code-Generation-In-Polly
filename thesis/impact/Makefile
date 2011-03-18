chapters := $(wildcard Chapters/*.tex)
frontbackmatter := $(wildcard FrontBackmatter/*.tex)
code := $(wildcard code/*/*.c)
svg-objects:= $(patsubst %.svg,%.pdf,$(wildcard images/*/*/*.svg)) \
	      $(patsubst %.svg,%.pdf,$(wildcard images/*.svg))
plot-objects:= $(patsubst %.plot,%.pdf,$(wildcard images/*/*/*.plot)) \
	      $(patsubst %.plot,%.pdf,$(wildcard images/*/*.plot))

all: paper.pdf

%.svg: %.plot
	cd `dirname $?` && gnuplot `basename $?`

%.pdf: %.svg
	inkscape --export-pdf=`echo $? | sed -e 's/svg/pdf/'` $?

paper.pdf: paper.tex  paper.bib $(code) $(svg-objects) $(plot-objects) 
	pdflatex -shell-escape paper && bibtex paper && pdflatex -shell-escape paper && pdflatex -shell-escape paper
