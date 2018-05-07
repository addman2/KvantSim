C=pdflatex
B=biber


hellomake: $(OBJ)
	$(C) Introduction_ESPRESSO.tex
	$(C) Introduction_ASE.tex
	$(C) Introduction_CSP.tex
	$(B) Introduction_CSP
	$(C) Introduction_CSP.tex
	$(C) Introduction_CSP.tex
	$(C) Skills.tex

.PHONY: clean

clean:
	rm -f *.aux *.pdf *.log
