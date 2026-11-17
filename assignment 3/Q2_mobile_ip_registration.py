import csv
home_address = "10.1.0.25"
home_agent = "10.1.0.1"
care_of_address = "172.16.4.20"
binding = {}

print("Q2 - MOBILE IP REGISTRATION AND TUNNELLING")
print("-" * 60)
print("1. Mobile Node enters visited network.")
print(f"2. Care-of Address obtained: {care_of_address}")
print(f"3. Registration request: {home_address} -> Home Agent {home_agent}")
binding[home_address] = care_of_address
print(f"4. Home Agent accepts registration: {home_address} -> {binding[home_address]}")
packet = {"source": "203.0.113.8", "destination": home_address, "data": "Patient status"}
print(f"5. Correspondent Node sends packet to home address: {packet['destination']}")
if packet["destination"] in binding:
    outer_destination = binding[packet["destination"]]
    print(f"6. Home Agent tunnels packet to CoA: {outer_destination}")
    print(f"7. Mobile Node decapsulates and receives: {packet['data']}")
    status = "DELIVERED"
else:
    status = "FAILED"
print("Registration result:", "ACCEPTED")
print("Packet delivery result:", status)
with open("Q2_mobile_ip_trace.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["Step","Event","State"])
    w.writerows([[1,"Visited network detected","MN moved"],[2,"CoA obtained",care_of_address],[3,"Registration request",home_agent],[4,"Binding updated",f"{home_address}->{care_of_address}"],[5,"CN sends packet",home_address],[6,"HA tunnels packet",care_of_address],[7,"Decapsulation","Delivered"]])
