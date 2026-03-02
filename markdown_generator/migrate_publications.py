#!/usr/bin/env python
"""One-time migration script: parse _pages/publications.md into publications.csv."""

import re
import csv
import os


def estimate_date(tag, venue, year):
    """Estimate a publication date from venue text and year."""
    month_map = {
        'january': '01', 'jan': '01', 'february': '02', 'feb': '02',
        'march': '03', 'mar': '03', 'april': '04', 'apr': '04',
        'may': '05', 'june': '06', 'jun': '06',
        'july': '07', 'jul': '07', 'august': '08', 'aug': '08',
        'september': '09', 'sep': '09', 'october': '10', 'oct': '10',
        'november': '11', 'nov': '11', 'december': '12', 'dec': '12',
    }
    venue_lower = venue.lower()
    for month_name, month_num in month_map.items():
        if month_name in venue_lower:
            return f'{year}-{month_num}-01'

    tag_lower = tag.lower()
    if 'neurips' in tag_lower or 'nips' in tag_lower:
        return f'{year}-12-01'
    if 'icml' in tag_lower or 'exait' in tag_lower:
        return f'{year}-07-01'
    if 'iclr' in tag_lower:
        return f'{year}-05-01'
    if 'asplos' in tag_lower:
        return f'{year}-04-01'
    if 'eurosys' in tag_lower:
        return f'{year}-04-01'
    if 'mlsys' in tag_lower:
        return f'{year}-05-01'
    if 'chi' in tag_lower:
        return f'{year}-05-01'
    if 'pldi' in tag_lower:
        return f'{year}-06-01'
    if 'mobisys' in tag_lower or 'mobicom' in tag_lower:
        return f'{year}-06-01'
    if 'hpdc' in tag_lower:
        return f'{year}-06-01'
    if 'vldb' in tag_lower:
        return f'{year}-08-01'
    if 'pact' in tag_lower:
        return f'{year}-10-01'
    if 'ismm' in tag_lower:
        return f'{year}-06-01'
    if 'mmsys' in tag_lower:
        return f'{year}-03-01'
    if 'acm mm' in tag_lower or re.match(r"mm'\d", tag_lower):
        return f'{year}-10-01'
    if 'sensys' in tag_lower:
        return f'{year}-11-01'
    if 'pacificvis' in tag_lower:
        return f'{year}-04-01'
    if 'icdm' in tag_lower:
        return f'{year}-12-01'
    if 'sc\'' in tag_lower:
        return f'{year}-11-01'
    if 'cgo' in tag_lower:
        return f'{year}-04-01'
    if 'icme' in tag_lower:
        return f'{year}-07-01'
    if 'automl' in tag_lower:
        return f'{year}-07-01'
    if 'crossfl' in tag_lower:
        return f'{year}-06-01'
    if 'fse' in tag_lower:
        return f'{year}-11-01'
    if 'mipr' in tag_lower:
        return f'{year}-08-01'
    if 'arith' in tag_lower:
        return f'{year}-06-01'
    if 'ismm' in tag_lower:
        return f'{year}-06-01'
    if 'cc\'' in tag_lower:
        return f'{year}-03-01'
    if 'icde' in tag_lower:
        return f'{year}-04-01'
    if 'spawc' in tag_lower:
        return f'{year}-07-01'

    # Default to June
    return f'{year}-06-01'


def extract_year_from_tag(tag):
    """Extract year from tag like NeurIPS'24 -> 2024, SC'18 -> 2018."""
    m = re.search(r"'(\d{2})(?:\]|$|\s)", tag)
    if m:
        yy = int(m.group(1))
        return str(2000 + yy) if yy < 50 else str(1900 + yy)
    m = re.search(r"@(\d{2})(?:\]|$|\s)", tag)
    if m:
        yy = int(m.group(1))
        return str(2000 + yy) if yy < 50 else str(1900 + yy)
    return None


def generate_slug(tag, title):
    """Generate a URL slug from tag and title."""
    # Clean tag: NeurIPS'24 -> neurips24
    slug_tag = re.sub(r"['@]", '', tag.lower())
    slug_tag = re.sub(r'[^a-z0-9]', '', slug_tag)

    # Take first meaningful word(s) from title
    words = re.sub(r'[^a-z0-9\s]', '', title.lower()).split()
    skip = {'a', 'an', 'the', 'of', 'for', 'in', 'on', 'via', 'with', 'and',
            'to', 'from', 'using', 'through', 'based', 'towards', 'by'}
    meaningful = [w for w in words if w not in skip][:2]

    if meaningful:
        return f'{slug_tag}-{"-".join(meaningful)}'
    return slug_tag


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, '..', '_pages', 'publications.md')
    output_file = os.path.join(script_dir, 'publications.csv')

    # Load existing CSV to preserve pub_date and url_slug for known entries
    # Key by (title, url_slug_prefix) to handle duplicate titles
    existing_by_title = {}
    existing_by_slug = {}
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row['title'].strip().lower()
                existing_by_title.setdefault(key, []).append(row)
                existing_by_slug[row['url_slug']] = row

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove YAML frontmatter
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    lines = content.split('\n')

    entries = []
    current_year = None
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Year header: **2024** or **2020 and Before**
        year_match = re.match(r'^\*\*(\d{4})(?:\s+and\s+Before)?\*\*$', line)
        if year_match:
            current_year = year_match.group(1)
            i += 1
            continue

        # Entry starts with "- **[TAG] Title"
        entry_match = re.match(r'^-\s+\*\*\[([^\]]+)\]\s*(.*)', line)
        if not entry_match:
            i += 1
            continue

        tag = entry_match.group(1)
        rest = entry_match.group(2)

        # Collect continuation lines for title (multi-line titles)
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith('<br>'):
            rest += ' ' + lines[i].strip()
            i += 1

        # Parse title (ends with **) and links after it
        title_match = re.match(r'(.*?)\*\*(.*)$', rest)
        if not title_match:
            continue

        title = title_match.group(1).strip().rstrip('.')
        links_text = title_match.group(2).strip()

        # Extract links: [[PDF](...)] [[Code](...)] etc.
        paper_url = ''
        code_url = ''
        extra_links = []
        for label, url in re.findall(r'\[\[([^\]]+)\]\(([^)]+)\)\]', links_text):
            if label.upper() == 'PDF':
                paper_url = url
            elif label.lower() == 'code':
                code_url = url
            else:
                extra_links.append(f'{label}~>{url}')

        # Parse author line (first <br> line)
        authors = ''
        while i < len(lines):
            stripped = lines[i].strip()
            if stripped.startswith('<br>'):
                authors = re.sub(r'^<br>\s*', '', stripped).rstrip('.')
                i += 1
                break
            elif stripped == '':
                i += 1
                break
            else:
                i += 1

        # Parse venue line (second <br> line)
        venue = ''
        while i < len(lines):
            stripped = lines[i].strip()
            if stripped.startswith('<br>'):
                text = re.sub(r'^<br>\s*', '', stripped)
                if text.startswith('https://doi.org/'):
                    break
                venue = text
                i += 1
                break
            elif stripped == '':
                i += 1
                break
            else:
                break

        # Check for DOI line (third <br> line)
        doi = ''
        while i < len(lines):
            stripped = lines[i].strip()
            if stripped.startswith('<br>'):
                text = re.sub(r'^<br>\s*', '', stripped)
                if text.startswith('https://doi.org/'):
                    doi = text
                    i += 1
                else:
                    break
                continue
            else:
                break

        venue = venue.rstrip('.')

        # Determine the actual year (from tag if available, else section header)
        tag_year = extract_year_from_tag(tag)
        actual_year = tag_year if tag_year else current_year

        # Look up existing entry by title, disambiguating duplicates by year
        title_key = title.strip().lower()
        matches = existing_by_title.get(title_key, [])
        old = None
        if len(matches) == 1:
            old = matches[0]
        elif len(matches) > 1:
            # Disambiguate by matching entry year to existing date year
            for m in matches:
                if m['pub_date'][:4] == actual_year:
                    old = m
                    break
            if not old:
                # Try matching tag abbreviation in slug
                tag_abbr = re.sub(r"['\s@]", '', tag.lower())
                for m in matches:
                    if tag_abbr in m['url_slug'].lower():
                        old = m
                        break

        if old:
            pub_date = old['pub_date']
            url_slug = old['url_slug']
        else:
            pub_date = estimate_date(tag, venue, actual_year)
            url_slug = generate_slug(tag, title)

        entries.append({
            'pub_date': pub_date,
            'authors': authors,
            'title': title,
            'venue': venue,
            'url_slug': url_slug,
            'paper_url': paper_url,
            'tag': tag,
            'code_url': code_url,
            'extra_links': '|'.join(extra_links),
            'doi': doi,
        })

    # Sort by date descending
    entries.sort(key=lambda x: x['pub_date'], reverse=True)

    # Write CSV
    fieldnames = ['pub_date', 'authors', 'title', 'venue', 'url_slug',
                  'paper_url', 'tag', 'code_url', 'extra_links', 'doi']
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

    print(f'Wrote {len(entries)} entries to publications.csv')
    for e in entries:
        print(f"  {e['pub_date']} [{e['tag']}] {e['title'][:70]}")


if __name__ == '__main__':
    main()
