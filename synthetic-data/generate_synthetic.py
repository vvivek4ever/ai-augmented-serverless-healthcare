import csv, random, datetime as dt, math, os

# Reproducible randomness
random.seed(42)

# Tunables (keep small for quick CI and reviewer download)
N_SITES = 8
N_EMPLOYEES = 1200
N_DAYS = 60

sites = [f"S{i:03d}" for i in range(1, N_SITES + 1)]
employees = [f"E{i:05d}" for i in range(1, N_EMPLOYEES + 1)]
start = dt.date.today() - dt.timedelta(days=N_DAYS)

os.makedirs("synthetic-data/out", exist_ok=True)

# ---------- health_events.csv ----------
with open("synthetic-data/out/health_events.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date","site_id","employee_id","test_result","vaccinated","exposure_score"])
    for d in range(N_DAYS):
        day = start + dt.timedelta(days=d)
        # simple seasonality so forecasting has signal
        base = 0.04 + 0.03 * math.sin(2 * math.pi * d / 14)
        # sample a subset per day to keep file size modest
        for _ in range(N_EMPLOYEES // 3):
            emp = random.choice(employees)
            site = random.choice(sites)
            vaccinated = random.choices([0, 1], weights=[0.35, 0.65])[0]
            exposure_score = max(0.0, min(1.0, random.gauss(0.35 if vaccinated else 0.5, 0.15)))
            pos_prob = max(0.01, min(0.4, base + 0.4 * exposure_score - 0.15 * vaccinated))
            test_result = int(random.random() < pos_prob)
            w.writerow([
                day.isoformat(),
                site,
                emp,
                test_result,
                vaccinated,
                round(exposure_score, 3)
            ])

# ---------- contact_edges.csv ----------
with open("synthetic-data/out/contact_edges.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["src_employee","dst_employee","weight"])
    for _ in range(3000):
        a, b = random.sample(employees, 2)
        w.writerow([a, b, round(random.uniform(0.1, 1.0), 2)])

print("Wrote: synthetic-data/out/health_events.csv and contact_edges.csv")
