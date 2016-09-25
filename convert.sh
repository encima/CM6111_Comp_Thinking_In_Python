#!/bin/bash

jupyter nbconvert --to latex $1.ipynb --output output/$1.tex
cd output/
pdflatex $1.tex
rm $1.log $1.out $1.aux
