# Jupyter notebook markdown generator

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process. The .py files are pure python that do the same things if they are executed in a terminal, they just don't have pretty documentation.


# Updated by Hui. Steps: 

1. Edit publications.xlsx file 
2. Export to .csv file 
3. Run `python pub2md/py` to produce .md files in folder `_publications`. 

