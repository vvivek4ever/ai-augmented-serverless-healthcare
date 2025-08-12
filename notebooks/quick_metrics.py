import csv, collections

events = list(csv.DictReader(open("synthetic-data/out/health_events.csv", newline="")))
n = len(events)
positives = sum(int(r["test_result"]) for r in events)
rate = positives / n if n else 0

by_site = collections.defaultdict(lambda: [0,0])  # [rows, positives]
for r in events:
    by_site[r["site_id"]][0] += 1
    by_site[r["site_id"]][1] += int(r["test_result"])

print(f"Rows: {n}")
print(f"Positives: {positives}")
print(f"Overall positivity rate: {rate:.3%}")
print("\nPer-site positivity:")
for site, (rows, pos) in sorted(by_site.items()):
    pct = (pos/rows) if rows else 0
    print(f"  {site}: {pos}/{rows} ({pct:.2%})")