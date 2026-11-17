import math
attendees, traffic_each, zone_area = 25000, 0.05, 1.0
event_traffic=attendees*traffic_each
normal_traffic=100000*0.025
print("TASK 12 - DAY-4 STADIUM EVENT DESIGN")
print(f"Attendees                       : {attendees:,}")
print(f"Traffic per attendee            : {traffic_each:.3f} Erlang")
print(f"Event offered traffic           : {event_traffic:,.1f} Erlangs")
print(f"Event traffic density           : {event_traffic/zone_area:,.1f} Erlangs/km^2")
print(f"Township normal traffic (100k)  : {normal_traffic:,.1f} Erlangs")
print(f"Township average density        : {normal_traffic/12:.2f} Erlangs/km^2")
print(f"Event / normal average density  : {(event_traffic/zone_area)/(normal_traffic/12):.2f} times")
print("\nDecision: temporarily MODIFY the macro design for the four-hour event.")
print("Deploy temporary cells/small cells, directional sectors, temporary backhaul,")
print("coordinated channels, power control, live monitoring and rollback.")
print("\nExact event blocking cannot be calculated without allocated channels,")
print("sector count, call-arrival profile and neighbouring-cell spare capacity.")
