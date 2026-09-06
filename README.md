# dataset_lapd-nibrs

This repository is the starting point for a team working with **LAPD NIBRS Offenses and Victims**, two open-data tables published by the Los Angeles Police Department on the City of Los Angeles open-data portal. One table holds one row per offense charged on a police report, the other holds one row per victim named on a police report, and together they cover crime reports taken inside the City of Los Angeles, almost all of them from March 2024 to August 2026. The repository does not hold the full data. It holds the data overview document, a small ready-made sample you can code against straight away, and a script that downloads the full files for you.

**A note on accuracy.** The documents here were written with AI assistance and then checked against the linked official sources. Linked sources are authoritative. Unlinked statements, and anything marked "(unverified)", should be checked before you rely on them. Report mistakes to the professor.

## Files

- `data_overview_lapd-nibrs.md`: the data overview. Industry context, possible stakeholders and decisions (illustrative examples only), what is already well known, download instructions, the full data dictionary and the list of traps and gaps.
- `download_data.py`: downloads both full CSV files into a `data` folder next to itself.
- `sample/offenses_sample.csv` and `sample/victims_sample.csv`: a sample of both tables, drawn so that they join to each other exactly as the full files do.
- `sample/README.md`: how the sample was drawn, and what you may and may not conclude from it.
- `.gitignore`: keeps the downloaded `data` folder out of Git.

## Get the data

Run these lines one at a time.

```
cd ~/dso576
git clone https://github.com/USC-DSO-576-PS/dataset_lapd-nibrs.git
cd dataset_lapd-nibrs
uv run python download_data.py
```

Section 4 of the data overview explains what the script prints, how long it takes, and how to download the same two files by clicking links in a browser instead. If the `git clone` line fails, you do not need it: the browser route in section 4 works on its own, and it tells you where to put the files. The same goes for the script: some servers block scripted requests, so if `download_data.py` prints an error, download the two files in the browser instead.

## How to use this repository

This repository is read-only for students: read it, clone it and copy from it, but do your team's work elsewhere. It is not the team repo you create in class. Copy `data_overview_lapd-nibrs.md` into your team's `project` folder, as the Module 3 handout asks, and keep it open while each role does its investigation.
