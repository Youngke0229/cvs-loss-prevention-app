# LAPD NIBRS Offenses and Victims (City of Los Angeles open data)

Published by the Los Angeles Police Department on the City of Los Angeles open-data portal. Two tables, 471,285 offense rows and 432,047 victim rows, covering crime reports taken inside the City of Los Angeles, almost all of them from March 2024 onward, refreshed roughly every two weeks.

**How to use this document.** Copy this file into your team's `project` folder, as the Module 3 handout asks, and keep it open while you work. Sections 1 to 3 are for everyone: what the data is, who uses data like it, and what the world already knows about this subject. Role 5 (Technical path) follows section 4 to download the files and record what arrived. Role 3 (Data fit) leans on sections 5 and 6, which give every column, every code table, and an honest list of what these files do not contain. Roles 1, 2, 4 and 6 will find section 1 and section 6 the most useful.

---

## 1. Description and industry context

The Los Angeles Police Department, usually written LAPD, is the police force for the City of Los Angeles. Every time someone reports a crime to LAPD, or an officer writes up an incident, a record is created in the department's Records Management System. That system went live on 7 March 2024. It follows a federal standard called NIBRS, the National Incident-Based Reporting System, which the FBI requires police agencies across the United States to report in. Under NIBRS, one police report can carry several separate offenses, several victims and several offenders, and each one is recorded on its own line rather than collapsed into a single summary. The City of Los Angeles publishes two extracts of that system as open data: an offenses table and a victims table.

One row in the offenses table is **one offense code charged on one police report**. If a single robbery report also records a stolen car and a vandalized door, that report produces three offense rows. One row in the victims table is **one victim named on one police report**. A "victim" here is not always a person: businesses, government agencies, law enforcement officers and "society" (used for offenses with no individual victim, such as a drug possession charge) all appear as victim types. The two tables share the police report number, `CaseNo`, which is how you connect them.

The data is administrative, not survey data. Nobody was interviewed and nobody was sampled. A row exists because a person called the police, or an officer wrote a report, and a clerk coded it into a category. Everything in section 6 follows from that one fact. Coverage is the **City** of Los Angeles only, split into 21 LAPD geographic areas (Central, Hollywood, 77th Street, Topanga and so on) and 1,180 smaller reporting districts. Report dates run from 25 December 1993 to 31 August 2026, but only 289 offense rows carry a report date before 2024; those are old cases that were typed into the new system after it launched. In practice this is a March 2024 to August 2026 file. The publisher refreshes both tables roughly every two weeks, and revises existing rows in place when a case status changes.

**Who cares about these numbers, and why they argue about them.** Los Angeles is a city of about four million people inside a county of about ten million, and the two are constantly confused. The City of Los Angeles is one of 88 cities in Los Angeles County. Long Beach, Santa Monica, Pasadena, Beverly Hills and Inglewood are separate cities with their own police departments, and the Los Angeles County Sheriff's Department polices the parts of the county that are not inside any city, plus a number of small cities that pay the Sheriff to police them instead of running their own department. So this file is not "crime in LA County" and not "crime in the LA metro area". It is crime reported to one department inside one city boundary. Inside that boundary, the players are: the Mayor's office and the 15 City Council district offices, each of which controls discretionary money for things like street lighting, cleanup crews and private security patrols; LAPD itself, whose command staff run a performance meeting every two weeks, known as Compstat, where area captains answer for the numbers in their area; the Los Angeles City Attorney, who prosecutes misdemeanors (the lesser offenses), and the Los Angeles County District Attorney, who prosecutes felonies (the serious ones); business improvement districts, which are groups of property owners on a commercial corridor who tax themselves to pay for cleaning and private security; retail chains and their loss-prevention departments, the in-house teams responsible for theft and store security; property insurers and commercial real-estate investors, who price risk by location; victim-service and community organizations that run domestic violence, homelessness and hate-crime programs; and local newsrooms, above all Crosstown LA at USC Annenberg, which has published Los Angeles crime numbers for years.

The money at stake is ordinary city money, and it is decided at a small geographic scale. A council office deciding whether to fund lighting on one corridor or another, a retail chain deciding which three of its Los Angeles stores get a second guard on the evening shift, a business improvement district deciding what hours its patrol works: all of these are decisions about a few blocks and a few hundred thousand dollars, and all of them are argued with counts that come from files like this one.

**What you need to know to read this data the way an insider would.** Four things. First, **reported crime is not crime.** Property crime in particular is reported at a fraction of its true rate, and how often people call the police varies by neighborhood, by whether an insurance claim requires a police report, and by how much residents trust the police. A district with more reported burglaries may be a district where more people call. Second, **the switch to NIBRS raises the count without raising the crime.** The old federal system, called UCR (Uniform Crime Reporting), applied a "hierarchy rule" that counted only the most serious offense in an incident. NIBRS counts every offense separately. The publisher says so plainly on the portal page. Inside this very file there is a step change in January 2025, where the monthly count jumps from roughly 11,000 to 12,700 offenses to roughly 17,100 to 19,800 and stays there. That is a change in how reports are recorded, not a crime wave, and any comparison that crosses January 2025 is comparing two different regimes. Third, **"cleared" is not "convicted."** A cleared case is one LAPD considers resolved, usually by an arrest. What the prosecutors and the courts did afterwards is not in this file. Fourth, **these numbers are politically contested.** LAPD's internal Compstat counts and the open-data file do not always agree, and Crosstown LA published a comparison in June 2026 showing 909 residential burglaries in one source against 1,382 in the other for the same quarter. When you present a number from this file, be ready to say which file, which date it was downloaded, and which unit you counted.

---

## 2. Examples of stakeholders and decisions (not exhaustive or necessarily endorsed)

These are examples, written to show the range of people who use data like this. They are not assignments, none is endorsed over another, and your team may propose an audience that does not appear here.

- **A district director at Los Angeles City Council District 14, which covers downtown and Boyle Heights, must decide which one of three commercial corridors gets next year's street-lighting and cleanup money.** `RPT Dist No` puts offenses in a neighborhood-sized area, `Premise Desc` separates street and sidewalk offenses from indoor ones, and `Time OCC` says whether the problem is a night-time problem at all.
- **A loss-prevention manager for CVS Health's Southern California region must decide which Los Angeles stores get a second guard on the evening shift.** Loss prevention is the in-house team responsible for theft and store security. The shoplifting code `23C`, the robbery code `120` and the retail values in `Premise Desc` isolate store-facing offenses, and `Time OCC` in the offenses table gives a clean hour-of-day profile.
- **An operations director at the Downtown Center Business Improvement District, the group of downtown property owners that pays for cleaning crews and safety patrols, must decide which blocks the patrol walks and at what hours.** `RPT Dist No` and `Time OCC` together give a block-by-hour picture, and `Premise Desc` says whether the offenses are happening on the street or inside buildings.
- **A commercial property underwriter at Farmers Insurance, whose head office is in Woodland Hills in the San Fernando Valley, must decide how to price a policy on a warehouse near a specific intersection.** `LAT`, `LON` and `RPT Dist No` locate burglary code `220` and theft-from-vehicle code `23F` at block level, though the file carries no dollar loss, so how much each one costs has to come from somewhere else.
- **A program director at Peace Over Violence, the Los Angeles nonprofit that runs domestic violence and sexual assault services, must decide which two LAPD areas get the next two advocate positions.** The `Domestic Violence Crime` flag is filled in on every offense row, so counts by `AREA` and by month are directly available.
- **A security planner at LA Metro, the region's bus and rail agency, must decide which hours to staff two rail stations with fare inspectors.** The `Transit-related Crime` flag marks bus and rail offenses, and `AREA` plus `Time OCC` say where and when they cluster, though the file names no station or line.
- **A data reporter at Crosstown LA, the USC Annenberg newsroom that publishes Los Angeles crime numbers, must decide whether a "crime is up in 2025" story is true enough to publish.** `Date Rptd` gives the monthly series, and the January 2025 step described in section 6 is exactly the trap the story would fall into.
- **Outside an organization entirely: a first-year graduate student at USC must decide which of two neighborhoods to sign an apartment lease in.** The reporting-district counts, the premise types and the hour of day are the only evidence in the file, and section 6 explains why a raw count with no population denominator is a poor answer to that question.

---

## 3. What is already well known and demonstrated

> Your project is judged on how far it goes beyond what is listed here. Reproducing these is a fine way to
> learn the data, but it earns little credit on its own, and a build that hiring managers have seen many
> times is a weak portfolio piece. Read this list as the floor, not as a menu.

### (a) Findings people already know

These are the headline facts about crime in Los Angeles that a well-read person, or an AI assistant, can state without opening the file.

- Reported crime is heavily concentrated. A small number of LAPD areas, with the downtown Central area at the top, carry far more reported offenses than the quietest areas, and inside each area a handful of reporting districts carry most of the volume.
- The ranking of areas changes depending on whether you count crimes against persons or crimes against property. An area can be near the top on one and mid-pack on the other.
- Reported crime rises in the warmer months and falls in the winter, a seasonal pattern visible in almost every American city.
- The hour-of-day pattern, crossed with day of week, is the standard first chart on this kind of data. It shows an evening peak, an early-morning low, and artificial piles of offenses at exactly midnight and exactly noon, which are what an officer records when the time is unknown.
- Vehicle-related theft is a large share of Los Angeles property crime, and the national surge in Kia and Hyundai thefts, driven by a social-media method for starting cars that lacked engine immobilizers, is a widely reported feature of recent years.
- Clearance rates differ sharply by offense type. Offenses against persons, especially the most serious ones, are cleared at far higher rates than property offenses such as theft from a vehicle, which are cleared very rarely.
- Victims are not distributed like the city's population. Published analyses of LAPD data routinely report differences in victimization by recorded descent, by sex and by age.
- Moving from the old UCR system to NIBRS increases the number of recorded offenses, because multiple offenses in one incident are now counted separately. The publisher states this on the portal page itself.
- The best-known hot spots are the downtown core, the Hollywood entertainment corridor and a set of South Los Angeles commercial streets, and they have appeared on published crime maps for years.

### (b) Analyses and tools that already exist

- [Crosstown LA, "L.A.'s blurry crime picture" (June 2026)](https://xtown.la/2026/06/02/l-a-s-blurry-crime-picture/): a news analysis reconciling LAPD's open-data counts against its internal Compstat counts, reporting 909 residential burglaries in one and 1,382 in the other for the same quarter. It works on the same NIBRS-era numbers as the tables described here.
- [Crosstown LA products: the Crime Tracker, the Safety Map and the Neighborhood Tracker](https://products.xtown.la): live neighborhood crime maps and trend trackers for Los Angeles, updated continuously. A plain neighborhood crime map is therefore a build with an established public competitor.
- [Guardian Integrated Security, "50+ California Retail Theft Statistics (2026)"](https://www.guardianintegratedsecurity.com/retail-theft-statistics-california/): a marketing statistics page breaking retail crime down by LAPD division and premise type, built on LAPD's older UCR-format file rather than these tables.
- [Kaggle mirror: `kushsheth/los-angeles-police-department-lapd-crime-data`](https://www.kaggle.com/datasets/kushsheth/los-angeles-police-department-lapd-crime-data): a copy of LAPD's older UCR-format "Crime Data from 2020 to Present" file, hosted for easy loading.
- [Kaggle mirror: `utkarsh1093/crime-data-from-2020-to-nov2025`](https://www.kaggle.com/datasets/utkarsh1093/crime-data-from-2020-to-nov2025): another copy of the same older UCR-format series, extended to November 2025.
- Kaggle mirror `aadigupta1601/lapd-crime-data-2020-2024`: a third copy of the older UCR-format series, listed under that slug on Kaggle.
- [Kaggle notebook: `aumparmar/lapd-crime-data-analysis`](https://www.kaggle.com/code/aumparmar/lapd-crime-data-analysis): a descriptive exploration of the older UCR-format file. **This is the standard beginner project**, the exploratory data analysis that almost every tutorial on this subject performs.
- [GitHub: `NonsoOmoko/Analyzing-Crime-in-Los-Angeles`](https://github.com/NonsoOmoko/Analyzing-Crime-in-Los-Angeles): a course-style exploratory analysis of the 2020 to 2024 UCR-format file. **Standard beginner project.**
- [GitHub: `obielin/Crime-Data-Analysis`](https://github.com/obielin/Crime-Data-Analysis): another course-style exploratory analysis of the same file. **Standard beginner project.**
- [GitHub: `srishtisingh34/Crime-Severity-Prediction`](https://github.com/srishtisingh34/Crime-Severity-Prediction): a model that predicts crime severity from the 2020 to 2024 UCR-format file. **This is the standard bootcamp prediction project** built on Los Angeles crime data.
- Published blog write-ups on Medium by Maya Abapo (2025), Ronaldo Pangarego and Fabio Rodrigues: exploratory analyses of Los Angeles crime using the older UCR-format file, in the same descriptive style as the notebooks above.
- A "Los Angeles Neighborhood Analysis" write-up on Towards Data Science: a neighborhood-level descriptive analysis, again on the older UCR-format file.
- [The FBI's own NIBRS pages](https://www.fbi.gov/how-we-can-help-you/more-fbi-services-and-information/ucr/nibrs): the national offense-code definitions and the annual national NIBRS statistics that give the standard for how these codes are meant to be read.
- [The two portal pages themselves](https://data.lacity.org/d/k7nn-b2ep) carry built-in charting and filtering tools, so a simple count by area or by month is available on the website with no code at all.

Note which file each item uses. Almost every open-source item above reads LAPD's **older** UCR-format crime file, which carries different offense codes and a different unit of analysis, so its code has to be rewritten before it will run against the two tables described here.

---

## 4. How to obtain the data

**Where it lives.** The official pages are [LAPD NIBRS Offenses Dataset](https://data.lacity.org/d/k7nn-b2ep) and [LAPD NIBRS Victims Dataset](https://data.lacity.org/d/gqf2-vm2j) on the City of Los Angeles open-data portal. No account, no key, no login and no terms click-through are required.

**Licence.** The victims table is published under a Creative Commons Zero 1.0 Universal public domain dedication, which places it in the public domain; the offenses table carries no licence field on the portal, only the attribution "Los Angeles Police Department". Both are open city records, and you should credit the Los Angeles Police Department and the City of Los Angeles open-data portal wherever you use them.

**Update cadence.** Roughly every two weeks. Existing rows are revised in place when a case status changes, and there is no version column, so write down the date you downloaded your copy and put that date on every chart.

### Files to download

| File | Direct link | Format | Size | Rows | Columns |
|---|---|---|---|---|---|
| `lapd_nibrs_offenses_k7nn-b2ep.csv` | [offenses CSV export](https://data.lacity.org/api/views/k7nn-b2ep/rows.csv?accessType=DOWNLOAD) | CSV, plain ASCII text | 143.4 MB | 471,285 | 31 |
| `lapd_nibrs_victims_gqf2-vm2j.csv` | [victims CSV export](https://data.lacity.org/api/views/gqf2-vm2j/rows.csv?accessType=DOWNLOAD) | CSV, plain ASCII text | 85.6 MB | 432,047 | 17 |

Sizes and row counts are from a download on 4 September 2026. A later copy will be a little larger.

This is a read-only dataset repository, not the team repo you create in class. Clone it alongside your `project` folder and do your team's work in `project`.

### Route A, browser

1. Get a copy of this repository onto your computer and make a folder named `data` inside it. Run these lines one at a time. If you already cloned the repository, skip the first two lines.

```
cd ~/dso576
git clone https://github.com/USC-DSO-576-PS/dataset_lapd-nibrs.git
cd dataset_lapd-nibrs
mkdir data
```

   If the `git clone` line fails, you do not need it. Make a folder for the data instead, run these lines one at a time, and continue at step 2. The file paths in the code below then start with `lapd_` instead of `data/lapd_`.

```
cd ~/dso576
mkdir lapd-data
cd lapd-data
```

2. Click the [offenses CSV export](https://data.lacity.org/api/views/k7nn-b2ep/rows.csv?accessType=DOWNLOAD) link. The download starts immediately. Your browser will name the file `LAPD_NIBRS_Offenses_Dataset.csv`.
3. Click the [victims CSV export](https://data.lacity.org/api/views/gqf2-vm2j/rows.csv?accessType=DOWNLOAD) link. Your browser will name that file `LAPD_NIBRS_Victims_Dataset.csv`.
4. Move both files from your Downloads folder into the `data` folder, and rename them to `lapd_nibrs_offenses_k7nn-b2ep.csv` and `lapd_nibrs_victims_gqf2-vm2j.csv` so that the code snippets below work unchanged.

The two downloads together are about 230 MB and finish in under a minute or two on a normal home connection. Allow 250 MB of free disk space for them. There is no bot wall, no rate limit and no waiting page.

If a click does nothing, or your browser opens a wall of text instead of saving a file, use the portal page instead: open [the offenses page](https://data.lacity.org/d/k7nn-b2ep), click the **Export** button near the top right, choose **Download**, choose **CSV**, and the same file is produced. Repeat on [the victims page](https://data.lacity.org/d/gqf2-vm2j). If your browser saves the file with a `.txt` ending, rename it so it ends in `.csv`.

### Route B, script

This repository contains a small Python script that does the whole download for you. Run these lines one at a time.

```
cd ~/dso576
git clone https://github.com/USC-DSO-576-PS/dataset_lapd-nibrs.git
cd dataset_lapd-nibrs
uv run python download_data.py
```

The script creates a `data` folder next to itself, downloads both CSV files into it with the correct names, and prints one line per file with the size in megabytes and the seconds it took, then a summary line such as `2 of 2 files ready.` It also checks each finished file against a recorded fingerprint and prints either `checksum ok` or `checksum differs (the publisher may have updated the file)`. The second message is not an error: it simply means the publisher has refreshed the table since 4 September 2026, which is expected. Running the script again skips any file that is already downloaded at the expected size. Expect the whole run to take one to three minutes.

To confirm the two links are alive without spending 230 MB, run this instead. It reads only the first megabyte of each file.

```
uv run python download_data.py --check
```

### Opening the files

Both files are plain comma-separated text with one header row, no preamble line and no unusual characters, so pandas opens them with no encoding argument. What you must do is stop pandas from guessing types, because four columns are text that only looks numeric and pandas silently strips their leading zeros.

Save the lines below in a file called `look.py`, in the folder that contains your `data` folder, then run `uv run --with pandas python look.py`. Plain `uv run python look.py` will not work, because it does not install pandas. Each of the three blocks below runs on its own, so put one block in `look.py` at a time.

Offenses:

```python
import pandas as pd

as_text = {"CaseNo": str, "Time OCC": str, "AREA": str, "RPT Dist No": str,
           "Premise Cd": str, "Weapon Used Cd": str, "Status": str}
offenses = pd.read_csv("data/lapd_nibrs_offenses_k7nn-b2ep.csv", dtype=as_text)
offenses["AREA NAME"] = offenses["AREA NAME"].str.strip()
offenses["Date Rptd"] = pd.to_datetime(
    offenses["Date Rptd"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce")
print(offenses.shape)
print(offenses["Crime Against"].value_counts().head(3))
```

Expected output: `(471285, 31)`, then `Property 249718`, `Person 140801`, `Society 46841`.

Victims:

```python
import pandas as pd

as_text = {"CaseNo": str, "Time OCC": str, "AREA": str, "RPT Dist No": str,
           "Status": str}
victims = pd.read_csv("data/lapd_nibrs_victims_gqf2-vm2j.csv", dtype=as_text)
victims["Time OCC"] = victims["Time OCC"].str.zfill(4)
victims["AREA"] = victims["AREA"].str.zfill(2)
victims["RPT Dist No"] = victims["RPT Dist No"].str.zfill(4)
print(victims.shape)
print(victims["AREA"].nunique(), victims["RPT Dist No"].nunique())
```

Expected output: `(432047, 17)`, then `21 1170`. The three `zfill` lines are essential. Without them the victims table reports 30 areas and 1,636 reporting districts, because the same area is written both as `1` and as `01`. Section 6 explains this trap in full.

Reading the whole offenses file takes about five to fifteen seconds and uses under half a gigabyte of memory, so it fits on any laptop. If yours struggles anyway, read only the columns you need by adding `usecols=[...]` to `read_csv`, as the join example below does, or work on the sample files first.

Joining the two tables on `CaseNo` fans out, because one report can carry several offenses and several victims. Aggregate one side before you merge. This example attaches the mean age of the people recorded as victims on each report to every offense row of that report. It reads only the five columns it needs, with `usecols`, so it runs in about 200 MB of memory:

```python
import pandas as pd

as_text = {"CaseNo": str}
offenses = pd.read_csv("data/lapd_nibrs_offenses_k7nn-b2ep.csv", dtype=as_text,
                       usecols=["CaseNo", "NIBR Code", "Crime Against"])
victims = pd.read_csv("data/lapd_nibrs_victims_gqf2-vm2j.csv", dtype=as_text,
                      usecols=["CaseNo", "Victim Type", "Vict Age"])
people = victims[victims["Victim Type"] == "Person"]
age_by_case = people.groupby("CaseNo")["Vict Age"].mean()
joined = offenses.join(age_by_case, on="CaseNo")
print(joined.shape)
print(joined.groupby("Crime Against")["Vict Age"].mean().round(1))
```

Expected output: `(471285, 4)`, then mean ages of 39.5 for `Person`, 42.8 for `Property`, 42.8 for `Society` and 43.1 for the combined `Person, Property, Society` value.

The `sample/` folder in this repository holds a smaller ready-made copy of both tables, drawn so that they join to each other exactly as the full files do, so your team can start writing code immediately while the full download runs. Read `sample/README.md` before you quote any number from it.

Do not commit the downloaded data to your team repository. The Module 3 handout says so, GitHub rejects single files above 100 MB and the offenses export is 143 MB. The `data` folder in this repository is already listed in `.gitignore`.

---

## 5. Data dictionary

### 5.1 Summary

| File | Rows | Columns | Size | What one row is |
|---|---|---|---|---|
| `lapd_nibrs_offenses_k7nn-b2ep.csv` | 471,285 | 31 | 143.4 MB | One offense code charged on one police report |
| `lapd_nibrs_victims_gqf2-vm2j.csv` | 432,047 | 17 | 85.6 MB | One victim named on one police report |

**How they join.** Both tables carry `CaseNo`, the police report number. It is not unique in either table, so the join is many to many and it fans out: joining the raw offenses table to the raw victims table on `CaseNo` produces 494,242 rows, more than either input. Each table also has its own unique row key, `UniqueNIBRNo` in offenses and `UniqueVictimNo` in victims. There is **no key that links a specific victim to a specific offense**. The victims table instead carries `VictimOfsList`, a comma-joined list of the charge labels attached to that victim, which is text, not a key.

**Row counts behind the join.** The offenses table covers 423,245 distinct report numbers; 380,407 reports carry one offense row, 38,685 carry two, 3,410 carry three, and the tail reaches 13. The victims table covers 391,256 distinct report numbers; 359,841 reports carry one victim, 25,695 carry two, and the tail reaches 44. 32,001 reports have offense rows and no victim row; 12 have a victim row and no offense row.

**Coverage.** City of Los Angeles only, 21 LAPD geographic areas and 1,180 reporting districts. `Date Rptd` runs 25 December 1993 to 31 August 2026 but holds only 289 offense rows before 2024: 97,221 rows were reported in 2024, 221,914 in 2025 and 144,445 in 2026 through 31 August. Those four groups plus the 7,416 rows with no report date account for all 471,285 offense rows. `Date OCC`, the date the offense is believed to have happened, runs from 6 January 1800, which is a data-entry error, to 22 August 2026. Latitude runs 33.3426 to 34.7609 and longitude runs -118.8276 to -117.698 on rows with usable coordinates.

**The columns most projects turn on.** `Date Rptd` (when the report was taken), `Time OCC` (hour of the offense), `NIBR Code` with `Crime Against` (what kind of offense), `Premise Desc` (what kind of place), `AREA` and `RPT Dist No` (where, at two scales), `LAT` and `LON` (block-level point), `Status Desc` (whether LAPD considers the case cleared), the flags `Transit-related Crime`, `Hate Crime` and `Domestic Violence Crime`, and on the victim side `Vict Age`, `Vict Sex` and `Victim Type`.

Meanings marked "publisher" below come from the portal's own column descriptions. Percentages and distinct counts were computed from the files described in section 4.

### 5.2 Offenses table, 471,285 rows by 31 columns, in file order

| Column | Type as pandas reads it | Filled % | Distinct | Example values | Meaning |
|---|---|---|---|---|---|
| `CaseNo` | text | 100.0 | 423,245 | `24025639`, `201515681`, `000200784` | Police report number, publisher's "Case number". The join key to the victims table. Not unique. Mostly a year prefix plus a serial, but nine-digit legacy numbers appear on backfilled old cases, and one row carries the literal string `RFC CITATION` instead of a number. |
| `UniqueNIBRNo` | text | 100.0 | 471,285 | `24080577_520_0`, `24081233_23C_0` | Publisher: "Unique identifier created by combining CaseNo, NIBR Code, and offense sequence number." Unique on every row; this is the row key. |
| `Date Rptd` | text | 98.4 | 409,748 | `11/04/2024 11:21:37 AM` | Publisher: "Date reported". Month-first, with a real clock time on 462,841 rows. Blank on 7,416 rows. Build every time series on this column, not on `Date OCC`. |
| `Date OCC` | text | 100.0 | 201,915 | `06/18/2024 07:00:00 PM` | Publisher: "Date occurred". Carries a time on 456,651 rows, and that time is always identical to `Time OCC`. Has a long tail of implausible dates back to 1800. |
| `Time OCC` | integer if you let pandas guess; read as text | 100.0 | 1,440 | `0050`, `2015` | Publisher: "Time occurred". Four-character 24-hour local time, zero-padded on every row of this table. Redundant with the time inside `Date OCC`. Reading it as a number destroys the leading zeros. |
| `AREA` | integer if you let pandas guess; read as text | 100.0 | 21 | `01`, `18`, `21` | Publisher: "Geographic areas occurred (numerical)". LAPD area number, always two characters with a leading zero in this table. |
| `AREA NAME` | text | 100.0 | 21 | `Pacific             `, `77th Street         ` | Publisher: "Geographic areas occurred (textual)". Padded with trailing spaces to a fixed width in this table. Strip before grouping, and before joining to the victims table where it is not padded. |
| `RPT Dist No` | integer if you let pandas guess; read as text | 100.0 | 1,180 | `1136`, `1434` | Publisher: "Reporting district number". LAPD's smallest published geography, roughly a neighborhood. Four characters on 470,727 rows and two characters on 558 rows. The first two digits are the area. |
| `TotalOffenseCount` | integer | 100.0 | 11 | `1`, `2`, `13` | Publisher: "Total number of offenses involved". A report-level count repeated on every row of the report. It matches the actual number of offense rows on all but 43 reports. |
| `Group` | text | 97.0 | 2 | `A`, `B` | Publisher: "Group A or B in NIBR". FBI Group A offenses are reported in full incident detail; Group B are lesser offenses reported only on arrest. 404,179 rows are A, 52,886 are B, 14,220 are blank. The blanks concentrate on identity theft, code `26F`. |
| `NIBR Code` | text | 99.9 | 58 | `13B`, `290`, `23F` | Publisher: "NIBR offense code". The FBI three-character offense code. 58 distinct codes appear; 557 rows have none. Full code table in section 5.4. |
| `NIBR Description` | text | 100.0 | 2,365 | `211 - PC - F - Robbery - 120` | Publisher: "NIBR offense description". This is not a clean NIBRS label. It is the California statute, the code body, a felony or misdemeanor letter, an LAPD charge description and then the NIBRS code, joined by dashes. 2,365 distinct strings map onto 58 NIBRS codes. Group on `NIBR Code` for anything statistical, and read this string only when you need the specific statute. |
| `Crime Against` | text | 99.6 | 4 | `Property`, `Person`, `Society` | Publisher: "Crime against person, property, or society". The FBI's top-level category. 249,718 Property, 140,801 Person, 46,841 Society, and 32,226 rows carrying the combined string `Person, Property, Society`. |
| `Premise Cd` | text | 95.3 | 91 | `22`, `36`, `GA` | Publisher: "Type of structure, vehicle, or location (numerical)". Mixed numeric and alphabetic codes. Blank on 21,999 rows. Not one to one with the description: code `22` carries 8 different descriptions, code `46` carries 30, code `01` carries 98. Do not group on this column. |
| `Premise Desc` | text | 100.0 | 401 | `Street/Parkway`, `Hospital` | Publisher: "Premise code definition (textual)". The usable location-type field. 401 distinct values; blank on 48 rows. Top values in section 5.4. |
| `Weapon Used Cd` | text | 29.5 | 299 | `08`, `02`, `OD`, `OE, OA` | Publisher: "Type of weapon used in the crime". Present only where a weapon was recorded, which is under a third of rows. Multi-valued: a comma-joined list when more than one weapon was used, which is why 299 distinct strings sit on a much smaller underlying code list. |
| `Weapon Desc` | text | 29.5 | 677 | `Handgun`, `Bodily Force - Personal Weapons (hands, feet, teeth, etc.)` | Publisher: "Weapon used description". Same 29.5 percent coverage as the code. Also multi-valued: 87,579 rows contain a comma-joined combination. Split on the comma before counting weapon types. A blank means no weapon was recorded, which is not the same as no weapon being used. |
| `Status` | float if you let pandas guess; read as text | 99.9 | 12 | `40`, `10`, `1` | Publisher: "Status of the case". Investigation status code. Not one to one with the description: code `10` carries two descriptions and code `20` carries two. |
| `Status Desc` | text | 99.9 | 14 | `Investigation Continued`, `Cleared by Arrest` | Publisher: "Status code definition". The usable clearance field. Full table in section 5.4. This is the status at the moment the file was exported, not a status at a fixed number of days after the report. |
| `TotalVictimCount` | integer | 100.0 | 27 | `0`, `1`, `44` | Publisher: "Total number of victims involved". Report-level count repeated on every offense row. It is `0` on 37,395 rows, which are the reports that have no victim record at all. |
| `Victim Shot` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, "whether this was a victim(s) shot crime". `Yes` on 1,987 offense rows. |
| `Domestic Violence Crime` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, domestic violence related. `Yes` on 44,798 rows. |
| `Hate Crime` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, hate related. `Yes` on 1,757 rows, 0.37 percent. |
| `Gang-related Crime` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, gang related. `Yes` on 6,729 rows. This is an investigator's judgment, not a verified fact. |
| `Transit-related Crime` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, "transit related crime (bus or rail)". `Yes` on 14,950 rows, concentrated in Central area with 5,075. No station or line identifier is given, only the flag. |
| `Homeless-Victim Crime` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, victim is homeless. `Yes` on 13,432 rows. |
| `Homeless-Suspect Crime` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, suspect is homeless. `Yes` on 19,684 rows. |
| `Homeless-Arrestee Crime` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, arrestee is homeless. `Yes` on 30,192 rows. See the note in section 6: this flag and the suspect flag overlap on only 464 rows. |
| `LOCATION` | text | 100.0 | 84,395 | `5600 Denny Ave`, `Zoo Dr & Western Heritage Way` | Publisher: "Street address of crime incident rounded to the nearest hundred block to maintain anonymity". Free text. Some values are intersections. No unit or exact house number. |
| `LAT` | float | 99.97 | 5,134 | `34.1721` | Publisher: "Latitude" of the hundred block. Four decimal places, so it locates a block, not an address. 132 rows are blank and a further 547 rows carry a `0` that means unknown. |
| `LON` | float | 99.97 | 4,625 | `-118.3332` | Publisher: "Longitude" of the hundred block. The same blanks and the same `0` for unknown as `LAT`. Only 47,498 distinct coordinate pairs cover all 471,285 rows, because the rounding collapses addresses onto block centers. |

### 5.3 Victims table, 432,047 rows by 17 columns, in file order

| Column | Type as pandas reads it | Filled % | Distinct | Example values | Meaning |
|---|---|---|---|---|---|
| `CaseNo` | text | 100.0 | 391,256 | `160106255`, `25025432` | Publisher: "Case number". The same police report number as in the offenses table; this is the join key. One row carries the literal `RFC CITATION`. |
| `UniqueVictimNo` | text | 100.0 | 432,047 | `25025432_1`, `25025698_0` | Publisher: "Unique identifier created by combining CaseNo and victim sequence number." Unique on every row; the row key. |
| `Date Rptd` | text | 98.8 | 1,205 | `11/22/2020 12:00:00 AM` | Publisher: "Date reported". Date only. Unlike the offenses table, the clock part is always midnight, so there is no report time here. Blank on 5,367 rows. Range 11 December 1998 to 31 August 2026. |
| `Date OCC` | text | 100.0 | 3,151 | `06/15/2024 12:00:00 AM` | Publisher: "Date occurred". Date only, clock always midnight. Range 6 January 1800 to 22 August 2026. |
| `Time OCC` | integer if you let pandas guess; read as text | 100.0 | 2,000 | `1400`, `200`, `100` | Publisher: "Time occurred". 24-hour local time but **not zero-padded here**: 313,787 rows have four characters, 94,898 have three, 8,198 have two, 15,164 have one. `200` means 02:00. Pad to four characters before extracting an hour, or you will read `200` as hour 20. |
| `AREA` | integer if you let pandas guess; read as text | 100.0 | 30 raw, 21 real | `19`, `8`, `01` | Publisher: "Geographic areas occurred (numerical)". **Inconsistently padded**: area 1 appears as `1` on 32,388 rows and as `01` on 2,947 rows. There are 21 real areas. Pad to two characters before grouping or joining. |
| `AREA NAME` | text | 100.0 | 21 | `Central`, `Devonshire` | Publisher: "Geographic areas occurred (textual)". Not space-padded in this table, unlike the offenses table. |
| `RPT Dist No` | integer if you let pandas guess; read as text | 100.0 | 1,636 raw, 1,170 real | `1863`, `0101`, `999` | Publisher: "Reporting district number". Same padding problem: 252,045 rows have four characters, 179,422 have three, 267 have two, 313 have one. After padding to four characters there are 1,170 districts. |
| `TotalVictimCount` | integer | 100.0 | 26 | `1`, `2`, `44` | Publisher: "Total number of victims involved per CaseNo". Report-level count repeated on every victim row of the report. Matches the actual victim row count on all but 27 reports. |
| `VictimOfsList` | text | 100.0 | 7,134 | `487(D)(1) - PC - F - Grand Theft Auto - GTA  - 240` | Publisher: "The offenses associated with the victim, as reported in the incident." A comma-joined list of the same long charge strings used in `NIBR Description`. Up to 512 characters. Because both the separator and the strings contain commas and dashes, splitting it reliably needs the trailing three-character NIBRS code as the anchor. This is the only link between a victim and a specific offense, and it is text, not a key. |
| `Vict Age` | float | 78.6 | 93 | `32`, `43`, `48` | Publisher: "Victim age" in years. Blank on 92,368 rows. **The minimum value in the entire file is 18.** No victim is recorded as a minor, so the blanks are not comparable to the filled values. At the top end 125 appears 9 times and single rows show 120, 124 and 143, which are errors. |
| `Vict Sex` | text | 83.0 | 6 | `M`, `F`, `U` | Publisher: "Victim sex". 188,312 `M`, 167,744 `F`, 1,759 `U` for unknown, 484 `TFBM` and 86 `TMBF` which denote transgender victims, and 280 `N`, which the publisher does not define. Blank on 73,382 rows, largely the business and government victims. |
| `Vict Descent` | text | 83.1 | 31 | `Hispanic`, `White/Caucasian`, `H - Hispanic` | Publisher: "Victim descent". LAPD's race and ethnicity coding, assigned by the reporting officer, not self-reported. Two vocabularies are mixed in the same column: a plain form used on almost every row and a legacy code-prefixed form such as `H - Hispanic` on a few hundred backfilled rows. `White` and `White/Caucasian` are the same thing, as are `Black` and `Black/African American`. Normalize before counting. Blank on 72,923 rows. |
| `Victim Type` | text | 100.0 | 13 | `Person`, `Business`, `I - Person` | The publisher lists the intended values: Business, Financial Institution, Government, Health Facility, Law Enforcement Officer, Other, Person, Religious Organization, Society (Public), Unknown. The file also contains the legacy forms `I - Person`, `B - Business` and `Individual` on 725 rows, which are duplicates of `Person` and `Business`. |
| `Victim Shot` | text | 100.0 | 2 | `Yes`, `No` | Publisher: yes or no, victim shot. `Yes` on 1,870 victim rows. |
| `Status` | float if you let pandas guess; read as text | 99.9 | 12 | `40`, `16`, `13` | Publisher: "Status of the case". The same code list as the offenses table, carried at report level. |
| `Status Desc` | text | 99.9 | 14 | `Open`, `Cleared by Arrest - DA Filed` | Publisher: "Status code definition". The same list as the offenses table. |

**What a victim row is.** 355,688 victim rows are people, 58,484 are businesses, 5,624 are the general public recorded as society, 5,482 are government and 2,855 are law enforcement officers.

### 5.4 Code tables

#### 5.4a NIBRS offense codes present, with the most common LAPD charge behind each

All 58 codes, ordered by offense count. The second column is the label the FBI uses for that code; the third is the LAPD charge string that appears most often under it in this file.

| Code | Offenses | FBI offense name | Most common LAPD charge under it |
|---|---|---|---|
| 13B | 70,140 | Simple assault | `243(A) - PC - M - Battery On Person - Simple` |
| 290 | 53,091 | Destruction, damage, vandalism of property | `594(B)(1) - PC - F - Vandalism ($400 Or More) - Felony` |
| 13A | 36,759 | Aggravated assault | `245(A)(1) - PC - F - ADW w/Deadly Weapon` |
| 23H | 36,406 | All other larceny | `484(A) - PC - M - Petty Theft - All Other Larceny` |
| 23F | 34,871 | Theft from motor vehicle | `459 - PC - F - Burglary From Motor Vehicle` |
| 90Z | 32,269 | All other offenses | `978.5 - PC - M - Bench Warrant/Failure To Appear` |
| 240 | 31,794 | Motor vehicle theft | `487(D)(1) - PC - F - Grand Theft Auto` |
| 220 | 26,936 | Burglary, breaking and entering | `459 - PC - F - Burglary - Residential` |
| 23C | 18,291 | Shoplifting | `459.5(A) - PC - M - Petty Theft - Shoplifting` |
| 120 | 17,507 | Robbery | `211 - PC - F - Robbery` |
| 26F | 14,080 | Identity theft | `530.5(A) - PC - F - Identity Theft` |
| 13C | 11,757 | Intimidation | `422(A) - PC - F - Criminal Threats` |
| 90J | 10,600 | Trespass of real property | `369I(B)(1) - PC - M - Trespass Rail Transit Property` |
| 35A | 10,427 | Drug, narcotic violations | `11377(A) - HS - M - Possess Controlled Substance` |
| 23G | 8,328 | Theft of motor vehicle parts or accessories | `484(A) - PC - M - Theft Of Motor Vehicle Parts` |
| 520 | 7,859 | Weapon law violations | `29800(A)(1) - PC - F - Felon/Addict Possess Firearm` |
| 90D | 5,787 | Driving under the influence | `23152(A) - VC - M - DUI Alcohol` |
| 26A | 5,210 | False pretenses, swindle, confidence game | `532(A) - PC - F - Obtain Money By False Pretenses` |
| 90C | 4,717 | Disorderly conduct | `653M(A) - PC - M - Annoying Telephone Call` |
| 35B | 3,966 | Drug equipment violations | `11364(A) - HS - M - Possess Unlawful Paraphernalia` |
| 11D | 3,152 | Fondling | `243.4(E)(1) - PC - M - Sexual Battery` |
| 11A | 2,932 | Rape | `261(A)(2) - PC - F - Rape By Force/Fear` |
| 40A | 2,648 | Prostitution | `647(B)(1) - PC - M - Solicit/Engage Prostitution` |
| 250 | 2,331 | Counterfeiting, forgery | `470(A) - PC - F - Forgery` |
| 280 | 2,191 | Stolen property offenses | `10851(A) - VC - F - Take Vehicle Without Owner's Consent` |
| 23D | 2,174 | Theft from building | `484(A) - PC - M - Petty Theft - Theft From Building` |
| 23A | 2,173 | Pocket-picking | `487(C) - PC - F - Grand Theft From Person` |
| 270 | 1,973 | Embezzlement | `487(D)(1) - PC - F - Embezzlement-Vehicle` |
| 210 | 1,281 | Extortion, blackmail | `518(A) - PC - F - Extortion` |
| 100 | 1,249 | Kidnapping, abduction | `207(A) - PC - F - Kidnapping` |
| 200 | 1,214 | Arson | `451(D) - PC - F - Arson Property` |
| 90F | 688 | Family offenses, nonviolent | `278.5(A) - PC - M - Violation Custody Decree` |
| 11B | 665 | Sodomy | `287(C)(2)(A) - PC - F - Oral Copulation By Force` |
| 23B | 659 | Purse-snatching | `487(C) - PC - F - Grand Theft From Person - Purse-Snatching` |
| (blank) | 557 | no code recorded | `510 - VEHICLE - STOLEN` |
| 09A | 550 | Murder and nonnegligent manslaughter | `187(A) - PC - F - Murder` |
| 11C | 466 | Sexual assault with an object | `289(A)(1)(A) - PC - F - Sexual Penetration W/Object` |
| 36B | 410 | Statutory rape | `261.5(B) - PC - M - Unlawful Sex With Minor` |
| 40C | 405 | Purchasing prostitution | `647(B)(1) - PC - M - Solicit/Engage Prostitution` |
| 64A | 343 | Human trafficking, commercial sex acts | `236.1(C) - PC - F - Human Trafficking Minor Commercial Sex Act` |
| 26B | 305 | Credit card, automated teller machine fraud | `484G - PC - F - Theft By Use Of Access Card Information` |
| 720 | 300 | Animal cruelty | `597(A) - PC - F - Intentional Cruelty To Animal` |
| 40B | 277 | Assisting or promoting prostitution | `653.23(A)(1) - PC - M - Supervise Prostitution Activities` |
| 370 | 259 | Pornography, obscene material | `311.11(A) - PC - F - Possess Obscene Matter Of Minor` |
| 90G | 233 | Liquor law violations | `25658(A) - BP - M - Sell Liquor To Minor` |
| 90B | 225 | Curfew, loitering, vagrancy | `647(H) - PC - M - Loiter On Private Property` |
| 26C | 221 | Impersonation | `10153.1 - BP - M - Identity Fraud - Impersonation` |
| 26G | 195 | Hacking, computer invasion | `502(C)(1)(A) - PC - M - Access Computer/Alter Data` |
| 09B | 162 | Negligent manslaughter | `192(C)(2) - PC - M - Vehicle Manslaughter` |
| 64B | 133 | Human trafficking, involuntary servitude | `236.1(A) - PC - F - Human Trafficking Forced Labor` |
| 39B | 52 | Operating, promoting or assisting gambling | `330 - PC - M - Gambling` |
| 39A | 27 | Betting, wagering | `330 - PC - M - Gambling` |
| 23E | 16 | Theft from coin-operated machine or device | `484(A) - PC - M - Petty Theft From Coin-Operated Machine` |
| 09C | 8 | Justifiable homicide | `197 - PC - F - Justifiable Homicide` |
| 39C | 7 | Gambling equipment violations | `330.1(A) - PC - M - Manufacture/Sell/Possess Gaming Device` |
| 510 | 4 | Bribery | `18 500 - US - F - Fraud - Postal Money Order` |
| 26E | 2 | Wire fraud | `502(C)(14) - PC - M - Wire Fraud` |
| 36A | 2 | Incest | `285 - PC - F - Incest` |
| 26D | 1 | Welfare fraud | `10980(C)(2) - WI - F - Fraud To Obtain Aid` |

In the charge strings, `PC` is the California Penal Code, `VC` the Vehicle Code, `HS` the Health and Safety Code, `BP` the Business and Professions Code and `WI` the Welfare and Institutions Code. `F` marks a felony, the serious class of offense, and `M` a misdemeanor, the lesser class.

The FBI names above are the standard meanings of the codes; the codes themselves are applied by LAPD's own mapping from California statutes, and that mapping is not always faithful. Code `510` is bribery in the FBI list, but its four LAPD rows are postal money-order fraud, and `39A`, `39B` and `39C` all carry the same generic gambling charge. Before you build a headline number on one code, read the `NIBR Description` values behind it.

#### 5.4b Case status

| Code | Description | Offenses |
|---|---|---|
| 40 | Investigation Continued | 258,296 |
| 1 | Open | 73,832 |
| 10 | Cleared by Arrest | 46,608 |
| 20 | Cleared Other | 27,279 |
| 10 | Cleared by Arrest - DA Filed | 13,283 |
| 60 | City Attorney Review | 12,696 |
| 14 | Cleared by Arrest - CA Filed | 11,954 |
| 12 | Cleared Other - CA Reject | 8,853 |
| 11 | Cleared Other - DA Reject | 5,678 |
| 20 | Cleared Other - Exceptional | 5,478 |
| 16 | District Attorney Review | 2,718 |
| 13 | Cleared by Arrest - CA Hearing | 2,417 |
| 50 | Non-Crime/Other | 1,062 |
| 30 | Unfounded | 659 |
| (blank) | (blank) | 470 |
| (blank) | Cleared by Arrest | 2 |

The fifteen description values above, blank included, cover all 471,285 offense rows. Two rows carry the description `Cleared by Arrest` with no status code, which is why `Cleared by Arrest` appears twice.

"DA" is the District Attorney, the county prosecutor who files felony charges. "CA" is the City Attorney, who files misdemeanor charges. A cleared case is a case LAPD considers resolved, which is not the same as a conviction.

#### 5.4c Crime against

| Value | Offenses |
|---|---|
| Property | 249,718 |
| Person | 140,801 |
| Society | 46,841 |
| Person, Property, Society | 32,226 |
| (blank) | 1,699 |

The fourth value is a coding artifact on catch-all offenses, not a fourth real category.

#### 5.4d LAPD areas

| Code | Name | Offenses | Code | Name | Offenses |
|---|---|---|---|---|---|
| 01 | Central | 38,993 | 12 | 77th Street | 26,442 |
| 02 | Rampart | 26,185 | 13 | Newton | 22,998 |
| 03 | Southwest | 26,171 | 14 | Pacific | 23,670 |
| 04 | Hollenbeck | 17,820 | 15 | N Hollywood | 25,329 |
| 05 | Harbor | 17,756 | 16 | Foothill | 14,418 |
| 06 | Hollywood | 25,167 | 17 | Devonshire | 19,049 |
| 07 | Wilshire | 20,897 | 18 | Southeast | 21,521 |
| 08 | West LA | 17,304 | 19 | Mission | 19,354 |
| 09 | Van Nuys | 21,278 | 20 | Olympic | 25,891 |
| 10 | West Valley | 20,376 | 21 | Topanga | 19,932 |
| 11 | Northeast | 20,734 | | | |

These are LAPD's own operational areas, often called divisions. They are not city council districts, not neighborhoods and not ZIP codes.

#### 5.4e Premise description, top 20 of 401

| Premise | Offenses | Premise | Offenses |
|---|---|---|---|
| Street/Parkway | 105,767 | Vehicle, Passenger/Truck | 6,491 |
| Residence / Home / Driveway | 53,540 | Department / Discount Store | 6,420 |
| Parking Lot / Garage / Drop Lot | 32,004 | Restaurant | 5,454 |
| Apartment/Condominium/Townhouse | 26,171 | Clothing Store | 4,904 |
| Sidewalk | 24,859 | Convenience Store | 4,333 |
| Victim's Residence | 22,835 | Park / Playground | 4,257 |
| Other Business | 17,572 | Air / Bus / Train Terminal | 3,794 |
| Highway / Road / Alley / Street | 15,137 | Alley | 3,531 |
| Single Family Home | 11,417 | Grocery/Supermarket | 3,503 |
| Apartment/Condo Common Laundry Room | 11,177 | Commercial / Office Building / Other Commerical | 3,470 |

The left column holds ranks 1 to 10 and the right column ranks 11 to 20. `Other Commerical` is misspelled in the data itself; leave it as it is when you filter.

This list is not a clean taxonomy. `Residence / Home / Driveway`, `Victim's Residence`, `Single Family Home`, `Other Residence`, `Shared Residence`, `Offender's Residence` and `Apartment/Condominium/Townhouse` all describe homes and are separate values. Build your own grouping before you compare premise types.

#### 5.4f Weapon description, top 10 of 677

| Weapon | Offenses |
|---|---|
| (blank, no weapon recorded) | 332,339 |
| Bodily Force - Personal Weapons (hands, feet, teeth, etc.) | 75,402 |
| Handgun | 14,336 |
| Other | 9,998 |
| Knife or other cutting or stabbing instrument | 3,228 |
| Unknown | 3,142 |
| Firearm (unknown whether handgun, rifle, or shotgun) | 2,814 |
| Knife W/ Blade 6 inches or less | 2,238 |
| Pepper Spray | 1,998 |
| Kitchen Knife | 1,810 |

Single-weapon knife entries alone are split across five distinct values, and firearms are split across handgun, shotgun, rifle, other firearm and unknown firearm. Group before you count.

#### 5.4g Victim demographics

| Victim Type | Rows | | Vict Sex | Rows | | Vict Descent, top 8 | Rows |
|---|---|---|---|---|---|---|---|
| Person | 355,688 | | M | 188,312 | | Hispanic | 160,024 |
| Business | 58,484 | | F | 167,744 | | (blank) | 72,923 |
| Society (Public) | 5,624 | | (blank) | 73,382 | | White/Caucasian | 72,403 |
| Government | 5,482 | | U | 1,759 | | Black/African American | 51,124 |
| Law Enforcement Officer | 2,855 | | TFBM | 484 | | Other | 13,600 |
| Other | 2,161 | | N | 280 | | White | 12,919 |
| I - Person (legacy) | 571 | | TMBF | 86 | | Black | 11,429 |
| Religious Organization | 450 | | | | | Other Asian | 10,850 |
| Unknown | 251 | | | | | | |
| Health Facility | 200 | | | | | | |
| Financial Institution | 127 | | | | | | |
| Individual (legacy) | 82 | | | | | | |
| B - Business (legacy) | 72 | | | | | | |

---

## 6. Notes

### Watch out for

- **The padding mismatch between the two tables.** This is the single most likely silent error in this dataset. `AREA`, `RPT Dist No` and `Time OCC` are zero-padded in the offenses table and inconsistently padded in the victims table. Area 1 appears as both `1` and `01`, district `0101` appears as both `101` and `0101`, time `0200` appears as `200`. Any group-by or join on those columns without fixing it splits every category in two and nothing warns you. Fix: read all three as text and pad them, as the snippets in section 4 do.
- **`AREA NAME` has trailing spaces in the offenses table and none in the victims table.** Joining the two on the name returns nothing at all, silently. Fix: apply `.str.strip()` to the offenses column, or join on `CaseNo` instead.
- **Pandas guesses the wrong types.** With a plain read, `Time OCC`, `AREA` and `RPT Dist No` come back as integers and lose their leading zeros, and `Status` comes back as a decimal number. Fix: pass the `dtype` dictionary shown in section 4.
- **Dates are month-first text, not dates.** Sorting or taking a minimum on the raw string gives nonsense, because `12/31/2025` sorts above `09/01/2026`. Fix: parse with `pd.to_datetime(..., format="%m/%d/%Y %I:%M:%S %p")` before comparing.
- **`Date OCC` contains impossible values.** The earliest is 6 January 1800, and single rows sit in 1826, 1900, 1920, 1925, 1930 and 1950. On 202 rows the report date is earlier than the occurrence date. Fix: filter to a plausible window before charting.
- **`Date Rptd` is blank on 7,416 offense rows and 5,367 victim rows.** Those rows vanish from any time series without a message. Fix: count them, and say so.
- **Two reporting regimes in one file.** March to May 2024 is a ramp-up while the new system rolled out. June to December 2024 sits near 11,000 to 12,700 offenses a month. From January 2025 the file sits near 17,100 to 19,800 a month. That step is a reporting change, not a crime wave. Fix: treat 2025 onward as the stable series and flag any year-over-year comparison that crosses January 2025.
- **The most recent weeks are incomplete.** August 2026 holds 13,488 offenses against the roughly 19,000 a month the file has been running at, because the file was pulled a few days after the month closed. Fix: drop or shade the trailing six to eight weeks of whatever copy you download.
- **Offenses are not incidents.** 471,285 offense rows sit on 423,245 reports. Decide whether your unit is the offense, the report or the victim, and state it on every chart.
- **The join fans out.** Offenses joined to victims on `CaseNo` gives 494,242 rows. 37,415 offense rows belong to reports with no victim row in the victims file, twenty more than the 37,395 rows where the publisher's own `TotalVictimCount` is `0`. The two disagree, which is itself worth knowing. Fix: aggregate one side before merging, as section 4 shows.
- **`Premise Cd` is not a key for `Premise Desc`.** Code `01` appears with 98 different descriptions, code `46` with 30, code `22` with 8, and the code is blank on 21,999 rows. Fix: group on `Premise Desc` and build your own categories.
- **Weapon fields are multi-valued and mostly blank.** They are filled on 29.5 percent of rows, and 87,579 of those contain a comma-joined combination such as `Bodily Force ..., Handgun`. Blank does not mean unarmed; it means nothing was recorded. Fix: split on commas before counting, and never treat blank as "no weapon".
- **`NIBR Description` is a compound string, not a label.** 2,365 distinct values sit on 58 codes, and the string contains both commas and dashes, so naive splitting fails. Fix: group on `NIBR Code`.
- **`Crime Against` has a fourth value that is not a category.** 32,226 rows carry `Person, Property, Society`, concentrated on catch-all offenses. Fix: decide explicitly whether to keep, drop or relabel them.
- **The homeless flags do not nest.** `Homeless-Arrestee Crime` is `Yes` on 30,192 rows, more than `Homeless-Suspect Crime` at 19,684, and the two overlap on only 464 rows. Fix: do not add them together and do not treat one as a subset of the other.
- **Fake coordinates that mean "unknown".** 132 rows have blank `LAT` and `LON`, and a further 547 carry a `0` that stands for unknown rather than a real place; the point at latitude 0, longitude 0 is in the Atlantic Ocean. Fix: filter both out before mapping.
- **Legacy vocabularies in the victims table.** `Victim Type` carries `I - Person`, `B - Business` and `Individual` alongside the current `Person` and `Business` on 725 rows, and `Vict Descent` mixes `H - Hispanic` with `Hispanic` and `White` with `White/Caucasian`. Fix: normalize these values before counting.
- **`Status` codes are not unique to a description.** Code `10` maps to both `Cleared by Arrest` and `Cleared by Arrest - DA Filed`, and code `20` maps to two descriptions as well. Fix: group on `Status Desc`.
- **One case number that is not a number.** The string `RFC CITATION` appears as a `CaseNo` in both tables, on one row each.
- **The file is revised in place.** A case that was open in one refresh can be cleared in the next, and old rows can gain corrected values. There is no version or as-of column. Fix: record the date you downloaded your copy and keep that copy.
- **File mechanics.** Pure ASCII, LF line endings, comma-delimited, standard double quoting, no preamble line, no byte-order mark. Times are local Los Angeles time with no time-zone marker and no daylight-saving handling. The offenses export at 143 MB is above GitHub's 100 MB single-file limit, so it must never be committed.

### What the data does not contain

- **No denominator of any kind.** No resident population, no daytime population, no foot traffic, no store count, no vehicle registrations. A reporting district with more offenses may simply hold more people or more shops. Population counts by small area come from the national census agency's American Community Survey and can be attached through the coordinates; foot traffic is sold commercially and is not published.
- **No dollar loss and no property value.** No amount stolen, no damage estimate, no recovered value. The national NIBRS standard collects a property segment, but this extract does not publish it, so the value of what was stolen or damaged cannot be computed from these files. Retailers call that lost value **shrink**; it is not in this data.
- **No offender or arrestee record.** There is no offender table, no suspect age, sex or descent, no arrest identifier and no way to link repeat offenders. The two homeless flags are the only offender-side information here. A police department's separate arrests release would be the kind of outside source that carries this.
- **No outcome after LAPD.** No charge filed, no plea, no conviction, no sentence. `Status Desc` stops at LAPD's own view. Court outcomes would have to come from a court system's own records.
- **No victim under 18, ever.** The minimum in `Vict Age` across 432,047 rows is 18, because juvenile ages are withheld by policy. Any question about crimes against minors is unanswerable here, and the 92,368 blank ages cannot be treated as randomly missing.
- **No exact location.** Addresses are rounded to the hundred block and coordinates to four decimal places, giving only 47,498 distinct points for 471,285 offenses. You cannot tell which of two neighboring storefronts was hit.
- **No narrative, motive or relationship.** No free-text description, no bias-motivation code behind the hate-crime flag, no relationship between victim and offender, no circumstance code. A domestic violence monitor can count flagged offenses but cannot say who the parties were to each other.
- **No transit line, station or vehicle.** `Transit-related Crime` is a yes or no with nothing behind it. Attaching an offense to a station means joining an outside list of stop locations by distance, and that is an assumption, not a fact in the data.
- **No unreported crime.** Only what someone reported to LAPD is here. There is no correction factor in the file. National victimization surveys are the kind of outside source that estimates the gap, and only at a coarse level.
- **Almost no history before March 2024.** Only 289 offense rows carry a report date before 2024. Anything needing a five-year trend or a pre-pandemic baseline has to use a different, older police file with different codes, which cannot simply be stacked on top of this one.
- **No agency other than LAPD and no geography outside the city.** Sheriff, transit police, airport police, school police and university police records are absent, so a chain comparing a Los Angeles site with a Long Beach or Santa Monica site has nothing to compare it with in this file.
- **No revision history.** Rows are updated in place between refreshes and no version column exists, so you cannot reconstruct what the file said last month unless you saved a copy yourself.

### Association, not cause

These files support comparisons across places, times, premise types and offense types, and they support before-and-after descriptions around a date. They do not support causal claims, for two reasons. First, the thing counted is reports, not crime, so anything that changes reporting behavior moves the counts without moving the underlying crime; the January 2025 step in this very file is a clean example. Second, nothing is randomized and there is no comparison group: a district that got more patrol got it because it had more crime, so comparing it with a quieter district mixes the effect of patrol with the reason for the patrol. You can honestly write "reported theft from vehicles in this district ran 40 percent above the city median over the last twelve months". You cannot write "the new lighting reduced crime" from these columns alone.
