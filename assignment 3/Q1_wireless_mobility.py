import csv
import matplotlib.pyplot as plt

# Illustrative mobility model based on Assignment 3 Q1 scenarios
scenarios = [
    ("Stationary", 0, 0, 100, 99, 18.4),
    ("Slow", 2, 1, 100, 97, 24.7),
    ("Moderate", 5, 2, 100, 94, 32.6),
    ("Fast", 10, 4, 100, 88, 48.9),
    ("Temporary outage", 5, 2, 100, 81, 76.3),
]
print("Q1 - WIRELESS MOBILITY ANALYSIS")
print("-" * 72)
print(f"{'Scenario':20} {'Speed':>7} {'Handoffs':>9} {'PDR %':>8} {'Delay ms':>10}")
for name, speed, handoffs, sent, received, delay in scenarios:
    pdr = received / sent * 100
    print(f"{name:20} {speed:7.1f} {handoffs:9d} {pdr:8.1f} {delay:10.1f}")
with open("Q1_mobility_results.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Scenario","Speed_m_s","Handoffs","Packets_Sent","Packets_Received","PDR_percent","Average_Delay_ms"])
    for row in scenarios:
        name,speed,h,sent,recv,delay=row
        w.writerow([name,speed,h,sent,recv,recv/sent*100,delay])
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot([x[0] for x in scenarios], [x[4] for x in scenarios], marker="o", label="PDR (%)")
ax.set_ylabel("Packet Delivery Ratio (%)"); ax.set_title("Q1 - Mobility versus Packet Delivery")
ax.set_ylim(70, 102); ax.grid(True); ax.tick_params(axis="x", rotation=15)
ax2 = ax.twinx(); ax2.plot([x[0] for x in scenarios], [x[5] for x in scenarios], marker="s", label="Delay (ms)")
ax2.set_ylabel("Average delay (ms)")
fig.tight_layout(); fig.savefig("Q1_output.png", dpi=150); plt.close(fig)
