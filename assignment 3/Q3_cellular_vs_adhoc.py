import csv
tests = [
    ("Cellular - normal", "Cellular", 10, "Available", 10, 22.5, 98.0),
    ("Cellular - BS outage", "Cellular", 10, "Partial", 6, 61.2, 86.0),
    ("Ad hoc mesh", "Ad hoc", 10, "Unavailable", 9, 38.4, 94.0),
    ("Ad hoc - relay failure", "Ad hoc", 10, "Unavailable", 7, 52.7, 89.0),
    ("Ad hoc - alternate route", "Ad hoc", 10, "Unavailable", 9, 44.1, 93.0),
]
print("Q3 - CELLULAR VERSUS AD HOC NETWORKS")
print("-" * 86)
print(f"{'Test':27} {'Network':10} {'Paths':>7} {'Delay(ms)':>11} {'PDR(%)':>9}")
for name,net,nodes,infra,paths,delay,pdr in tests:
    print(f"{name:27} {net:10} {paths:7d} {delay:11.1f} {pdr:9.1f}")
print("\\nDecision: For disaster areas without fixed infrastructure, use an ad hoc mesh;")
print("use a surviving cellular/satellite gateway when available.")
with open("Q3_network_comparison.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["Test","Network","Nodes","Infrastructure","Successful_Paths","Delay_ms","PDR_percent"]); w.writerows(tests)
