import random, csv
SEED = 42
random.seed(SEED)
TOTAL = 100
print("Q1 - MOBILE COMPUTING: OFFLINE METER READINGS")
print(f"Seed={SEED}, updates per trial={TOTAL}")
print("Availability | Immediate delivered | Immediate lost | Store-forward delivered | Delayed | Mean delay")
for p in [0.90, 0.60, 0.30]:
    # Analytical expected-count model used in the assignment brief
    delivered = round(TOTAL * p)
    lost = TOTAL - delivered
    queued = lost
    sf_delivered = delivered + queued
    mean_delay = queued / TOTAL
    print(f"{p:>11.0%} | {delivered:>18} | {lost:>14} | {sf_delivered:>23} | {queued:>7} | {mean_delay:>10.2f}")
with open("csv/Q1_offline_readings.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["availability","immediate_delivered","immediate_lost","store_forward_delivered","delayed","mean_delay_intervals"])
    for p in [0.90,0.60,0.30]:
        d=round(TOTAL*p); q=TOTAL-d
        w.writerow([p,d,q,TOTAL,q,q/TOTAL])
print("\nConclusion: store-and-forward retains all 100 updates if connectivity returns.")
