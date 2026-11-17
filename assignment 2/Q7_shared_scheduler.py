import numpy as np, csv
SEED=42
rng=np.random.default_rng(SEED)
DEVICES=5000
DUTY=0.10
REPORT_BYTES=200
FRAMES=60
# Each device generates one report with probability duty per frame; illustrative load model.
arrivals=rng.random((FRAMES,DEVICES)) < DUTY
dedicated_reserved=DEVICES
dedicated_busy=int(arrivals.sum())
dedicated_util=dedicated_busy/(FRAMES*DEVICES)
# Shared pool is sized to average concurrent report demand, rounded up; one grant handles one report.
pool=max(1,int(np.ceil(DEVICES*DUTY)))
queue=0; delivered=0; delays=[]; max_queue=0
for frame in range(FRAMES):
    new=int(arrivals[frame].sum())
    queue += new
    served=min(queue,pool)
    queue -= served
    delivered += served
    delays.extend([0 if served==new else 1] * served)
    max_queue=max(max_queue,queue)
shared_util=delivered/(FRAMES*pool)
with open("csv/Q7_scheduler_comparison.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["metric","dedicated_allocation","shared_scheduled_pool"])
    w.writerow(["devices",DEVICES,DEVICES])
    w.writerow(["reserved_resource_units",dedicated_reserved,pool])
    w.writerow(["generated_reports",int(arrivals.sum()),int(arrivals.sum())])
    w.writerow(["delivered_reports",int(arrivals.sum()),delivered])
    w.writerow(["resource_utilisation",dedicated_util,shared_util])
    w.writerow(["maximum_queued_reports","not_applicable",max_queue])
print("Q7 - SHARED SCHEDULED TELEMETRY CHANNEL")
print(f"Seed={SEED}, devices={DEVICES}, frames={FRAMES}, duty probability={DUTY:.0%}, report={REPORT_BYTES} bytes")
print(f"Generated reports={int(arrivals.sum())}")
print(f"Dedicated: reserved resources={dedicated_reserved}, approximate busy fraction={dedicated_util:.3%}")
print(f"Shared pool: reserved resources={pool}, delivered={delivered}, utilisation={shared_util:.3%}, max queue={max_queue}")
print("Interpretation: shared scheduling greatly reduces reserved resources; queueing/delay depends on burst load and pool size.")
