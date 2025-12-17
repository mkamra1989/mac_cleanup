from pathlib import Path
from collections import Counter
import argparse

parser = argparse.ArgumentParser(
    description="Delete files by extension and show count."
)
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Preview files without deleting."
)
directory = Path ('<path>')
sufix = [".jpeg", ".pdf"]
counter = Counter()
args = parser.parse_args()
Dryrun=args.dry_run

for item in directory.glob(f"*{sufix}"):
    if item.is_file() and item.suffix.lower() in sufix:
        if Dryrun:
            print(f"these file will be deleted:{item}") 
            counter[item.suffix.lower()] += 1
        else:
            item.unlink()
            print(f"removed: {item}")
            counter[item.suffix.lower()] += 1
print("SUMMARY")
for sufix, count in counter.items():
    print(f"{sufix or '[no extension]'} : {count}")

