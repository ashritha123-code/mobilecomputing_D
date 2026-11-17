import csv
trace = [
    (1,"S","Needs destination D","No valid route","UNKNOWN"),
    (2,"S","Broadcast RREQ","Forward to neighbours","DISCOVERY"),
    (3,"A","Receives RREQ","Record reverse route to S","DISCOVERY"),
    (4,"D","Receives RREQ","Generate RREP","REPLY"),
    (5,"A","Forwards RREP","Install next hop toward D","VALID"),
    (6,"S","Receives RREP","Install route S-A-D","VALID"),
    (7,"S","Sends data","Forward to A","ACTIVE"),
    (8,"A","Link to D fails","Send RERR to S","INVALID"),
    (9,"S","Receives RERR","Start route discovery again","REPAIR"),
]
print("Q6 - AODV REACTIVE ROUTING TRACE")
print("-" * 100)
print(f"{'Step':4} {'Node':6} {'Message/Event':24} {'Decision':32} {'State':10}")
for row in trace:
    print(f"{row[0]:4} {row[1]:6} {row[2]:24} {row[3]:32} {row[4]:10}")
print("\\nConclusion: AODV discovers routes on demand using RREQ/RREP and repairs broken routes using RERR.")
with open("Q6_aodv_trace.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["Step","Node","Message_or_Event","Decision","Route_State"]); w.writerows(trace)
