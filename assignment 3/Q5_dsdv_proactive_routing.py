import csv
# Simplified DSDV destination sequence-number route table demonstration
routes = {
    "A": {"next_hop":"A", "hops":0, "seq":10},
    "B": {"next_hop":"B", "hops":1, "seq":8},
    "C": {"next_hop":"B", "hops":2, "seq":6},
}
print("Q5 - DSDV PROACTIVE ROUTING")
print("-" * 65)
print("Initial route table at node A")
print(f"{'Destination':15} {'Next hop':12} {'Hop count':12} {'Sequence':10}")
for dest, r in routes.items():
    print(f"{dest:15} {r['next_hop']:12} {r['hops']:12} {r['seq']:10}")
print("\\nTopology change: link A-B fails; a fresh update arrives through node D.")
routes["B"]={"next_hop":"D","hops":2,"seq":10}
routes["C"]={"next_hop":"D","hops":3,"seq":8}
print("\\nUpdated route table at node A")
for dest, r in routes.items():
    print(f"{dest:15} {r['next_hop']:12} {r['hops']:12} {r['seq']:10}")
with open("Q5_dsdv_route_table.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["Destination","Next_Hop","Hop_Count","Sequence_Number"])
    for d,r in routes.items(): w.writerow([d,r["next_hop"],r["hops"],r["seq"]])
