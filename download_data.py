"""Download the two LAPD NIBRS CSV files into a data/ folder next to this script.

Usage:

    uv run python download_data.py

Check the links without downloading 230 MB (reads only the first megabyte of
each file and reports whether the server answered):

    uv run python download_data.py --check

Standard library only. Python 3.11 compatible.
"""

import hashlib
import pathlib
import sys
import time
import urllib.request

# A browser User-Agent string. The City of Los Angeles portal answers plain
# Python requests, but sending a normal browser string avoids any filtering.
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/151.0 Safari/537.36"
)

# The portal serves each dataset as one CSV export. The string in the URL
# (k7nn-b2ep) is the portal's permanent id for that dataset.
# expected_bytes and sha256 describe the copy downloaded on 4 September 2026,
# which the server reported as last modified on 1 September 2026. The portal
# does not publish a refresh schedule, so a later download will usually be
# larger and will have a different checksum. That is normal.
FILES = [
    {
        "name": "lapd_nibrs_offenses_k7nn-b2ep.csv",
        "url": "https://data.lacity.org/api/views/k7nn-b2ep/rows.csv?accessType=DOWNLOAD",
        "expected_bytes": 143447698,
        "sha256": "78a6b1b8321d7ffc9f349b0a65fba4bdb2998c4946872d2e4b50f3f4f2aa1918",
    },
    {
        "name": "lapd_nibrs_victims_gqf2-vm2j.csv",
        "url": "https://data.lacity.org/api/views/gqf2-vm2j/rows.csv?accessType=DOWNLOAD",
        "expected_bytes": 85619110,
        "sha256": "45f6bbc86b694ae1ee5cd569cd28149f056ed89a2765fd5283ea1cc36ef2eb15",
    },
]

CHUNK = 1024 * 1024  # one megabyte per read


def open_url(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(request, timeout=180)


def check_one(item):
    """Read the first megabyte only and report the status and the header row."""
    started = time.time()
    try:
        response = open_url(item["url"])
    except Exception as error:  # any network or HTTP problem
        print("  FAILED " + item["name"] + ": " + str(error))
        return False
    first = response.read(CHUNK)
    status = response.getcode()
    response.close()
    header = first.split(b"\n")[0].decode("ascii", "replace")
    columns = len(header.split(","))
    seconds = round(time.time() - started, 1)
    print("  " + item["name"])
    print("    HTTP status " + str(status))
    print("    first line has " + str(columns) + " column names")
    print("    read " + str(len(first)) + " bytes in " + str(seconds) + " s")
    return status == 200


def sha256_of(path):
    digest = hashlib.sha256()
    handle = open(path, "rb")
    while True:
        block = handle.read(CHUNK)
        if not block:
            break
        digest.update(block)
    handle.close()
    return digest.hexdigest()


def download_one(item, folder):
    target = folder / item["name"]
    if target.exists() and target.stat().st_size == item["expected_bytes"]:
        print("  " + item["name"] + ": already downloaded, skipping")
        return True
    started = time.time()
    try:
        response = open_url(item["url"])
    except Exception as error:
        print("  FAILED " + item["name"] + ": " + str(error))
        return False
    total = 0
    handle = open(target, "wb")
    while True:
        block = response.read(CHUNK)
        if not block:
            break
        handle.write(block)
        total = total + len(block)
    handle.close()
    response.close()
    seconds = round(time.time() - started, 1)
    megabytes = round(total / 1000000.0, 1)
    print("  " + item["name"] + ": " + str(megabytes) + " MB in " + str(seconds) + " s")
    if item["sha256"]:
        if sha256_of(target) == item["sha256"]:
            print("    checksum ok")
        else:
            print("    checksum differs (the publisher may have updated the file)")
    return True


def main():
    check_only = "--check" in sys.argv
    folder = pathlib.Path(__file__).resolve().parent / "data"
    if check_only:
        print("Checking " + str(len(FILES)) + " links (no full download).")
    else:
        folder.mkdir(exist_ok=True)
        print("Downloading " + str(len(FILES)) + " files into " + str(folder))
    good = 0
    for item in FILES:
        if check_only:
            ok = check_one(item)
        else:
            ok = download_one(item, folder)
        if ok:
            good = good + 1
    print(str(good) + " of " + str(len(FILES)) + " files ready.")
    if good < len(FILES):
        sys.exit(1)


if __name__ == "__main__":
    main()
