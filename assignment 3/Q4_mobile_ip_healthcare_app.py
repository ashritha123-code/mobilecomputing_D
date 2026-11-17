import csv
# Illustrative emergency-healthcare application requirements and sample evaluation
requirements = [
    ("Emergency alert", "High", 100, "Priority queue"),
    ("Patient vital signs", "High", 250, "Reliable delivery + timestamp"),
    ("Ambulance location", "Medium", 1000, "Periodic location update"),
    ("Routine report", "Low", 5000, "Store-and-forward"),
]
observed = [
    ("Emergency alert", 72, 99.8),
    ("Patient vital signs", 184, 99.2),
    ("Ambulance location", 420, 98.5),
    ("Routine report", 2100, 97.0),
]
print("Q4 - MOBILE IP APPLICATION: EMERGENCY HEALTHCARE")
print("-" * 86)
print(f"{'Service':24} {'Priority':10} {'Target ms':>10} {'Observed ms':>13} {'Delivery %':>12}")
for req, obs in zip(requirements, observed):
    name, priority, target, handling = req
    _, delay, delivery = obs
    print(f"{name:24} {priority:10} {target:10} {delay:13} {delivery:12.1f}")
    print("  Handling:", handling)
print("\\nResult: All illustrative delay values meet the stated target.")
with open("Q4_healthcare_requirements.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["Service","Priority","Target_Delay_ms","Observed_Delay_ms","Delivery_percent","Handling"])
    for req,obs in zip(requirements,observed):
        w.writerow([req[0],req[1],req[2],obs[1],obs[2],req[3]])
