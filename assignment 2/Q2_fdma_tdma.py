import csv
print("Q2 - FDMA VS TDMA")
bandwidth_khz = 2000
fdma_channel_khz = 25
fdma_nominal = bandwidth_khz // fdma_channel_khz
fdma_usable = int(fdma_nominal * 0.95)
tdma_carriers = bandwidth_khz // 200
tdma_slots_per_carrier = 8
tdma_nominal = tdma_carriers * tdma_slots_per_carrier
tdma_usable = tdma_carriers * 7
print(f"FDMA: {bandwidth_khz}/{fdma_channel_khz} = {fdma_nominal} nominal channels")
print(f"FDMA usable channels after 5% overhead = floor({fdma_nominal}*0.95) = {fdma_usable}")
print(f"TDMA: {tdma_carriers} carriers x {tdma_slots_per_carrier} slots = {tdma_nominal} nominal slots")
print(f"TDMA usable traffic slots (1 control slot/carrier) = {tdma_carriers} x 7 = {tdma_usable}")
rows = [
    ["A - Continuous voice",60,1.0,60,1.0],
    ["B - Bursty telemetry",80,0.10,80,0.10],
    ["C - Synchronized reports",70,0.05,70,0.05],
]
with open("csv/Q2_traffic_scenarios.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["scenario","devices","duty_cycle","fdma_dedicated_resources","tdma_duty_cycle"]); w.writerows(rows)
print("\nTraffic scenarios:")
for r in rows: print(f"{r[0]}: {r[1]} devices, duty cycle={r[2]:.0%}")
print("\nDecision: shared scheduled packet access is preferable for small, intermittent telemetry.")
