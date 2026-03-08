#!/usr/bin/env python
# coding: utf-8

# Publications markdown generator for academicpages
#
# Reads publications.csv and generates _publications/*.md files with frontmatter.
# CSV columns: pub_date,authors,title,venue,url_slug,paper_url,tag,code_url,extra_links,doi

import pandas as pd
import os

publications = pd.read_excel("publications.xlsx", header=0)

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)

for row, item in publications.iterrows():
    print(item.pub_date, item.url_slug)
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    md_filename = os.path.basename(md_filename)

    md = "---\n"
    md += 'title: "' + item.title + '"\n'
    md += "collection: publications\n"
    md += "date: " + str(item.pub_date) + "\n"
    md += "venue: '" + html_escape(item.venue) + "'\n"
    md += "authors: '" + item.authors + "'\n"
    md += 'tag: "' + item.tag + '"\n'

    if len(str(item.paper_url)) > 5:
        md += "paperurl: '" + item.paper_url + "'\n"

    if len(str(item.get('code_url', ''))) > 5:
        md += "codeurl: '" + item.code_url + "'\n"

    if len(str(item.get('extra_links', ''))) > 5:
        md += "extra_links: '" + item.extra_links + "'\n"

    if len(str(item.get('doi', ''))) > 5:
        md += "doi: '" + item.doi + "'\n"

    md += "---"

    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)

print(f"\nGenerated {len(publications)} publication files.")
