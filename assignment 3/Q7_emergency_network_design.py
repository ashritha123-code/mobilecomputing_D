import csv
tests = [
    ("E1",10,1,"Up","AODV",500,493,32.4,38),
    ("E2",20,5,"Up","AODV",500,477,48.7,86),
    ("E3",30,10,"Up","AODV",500,441,73.5,151),
    ("E4",20,5,"Down","AODV",500,452,61.8,94),
    ("E5",20,5,"Up","DSDV",500,462,52.1,126),
]
print("Q7 - MOBILE EMERGENCY COMMUNICATION NETWORK")
print("-" * 105)
print(f"{'Test':5} {'Nodes':6} {'Speed':7} {'Gateway':9} {'Protocol':9} {'PDR %':8} {'Delay ms':10} {'Control':8}")
for t,n,s,g,p,sent,recv,delay,ctrl in tests:
    print(f"{t:5} {n:6} {s:7} {g:9} {p:9} {recv/sent*100:8.1f} {delay:10.1f} {ctrl:8}")
print("\\nArchitecture: Ambulance/rescue/police nodes -> AODV ad hoc mesh -> emergency gateway")
print("-> surviving cellular/satellite link -> Home Agent -> hospital/command centre.")
print("If the gateway fails, local mesh communication continues and external messages are queued.")
with open("Q7_emergency_test_results.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["Test","Nodes","Speed_m_s","Gateway","Protocol","Packets_Sent","Packets_Received","PDR_percent","Average_Delay_ms","Control_Packets"])
    for t,n,s,g,p,sent,recv,delay,ctrl in tests: w.writerow([t,n,s,g,p,sent,recv,recv/sent*100,delay,ctrl])
