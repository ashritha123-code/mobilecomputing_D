import math
CASES=[("Charging + Wi-Fi",95,"wifi","moving","normal"),("80% battery + LTE",80,"lte","moving","normal"),("20%, stationary, LTE",20,"lte","still","normal"),("Low-power mode",14,"wifi","moving","normal"),("No connectivity",55,"offline","moving","normal"),("Device hot",65,"lte","moving","hot")]
def policy(b,n,m,t):
 if t=="hot": return 180,"defer except critical",.08
 if b<=15: return 300,"defer until charging/Wi-Fi",.05
 if n=="offline": return 60,"queue; sync when online",.10
 if m=="still" and b<=25: return 120,"defer until charging/Wi-Fi",.07
 if n=="wifi" and b>50: return 15,"batch upload now",.18
 return 30,"authenticated batched upload",.13
def main():
 print("TASK 6 - BATTERY-AWARE SECURE TRACKING SIMULATION")
 total=0
 for i,(name,b,n,m,t) in enumerate(CASES,1):
  interval,upload,energy=policy(b,n,m,t); total+=energy
  print(f"\\nCondition {i}: {name}\\n Sampling={interval}s | Upload={upload}")
  print(f" Estimated energy={energy:.2f} MODEL UNITS")
  print(" Protection rule: encrypt before queue; authenticated TLS for upload (design requirement).")
 print(f"\\nSix-cycle estimated total={total:.2f} model units")
 print("\\n3-CASE VALIDATION VS ALWAYS-ON (assumed 5s interval)")
 for i,c in enumerate(CASES[:3],1):
  interval=policy(*c[1:])[0]
  print(f"Case {i}: policy={interval}s ({3600/interval:.1f} samples/hour) | baseline=5s (720 samples/hour)")
 print("\\nFLEET SCALE")
 for devices in [1,5,10,20]:
  evaluations=devices*len(CASES)
  wakeups=devices*sum(math.ceil(3600/policy(*c[1:])[0]) for c in CASES)
  print(f"Devices={devices} | evaluations={evaluations} | modeled wake-ups/hour={wakeups} | queued records={devices*24}")
 print("\\nSync rules: unique UUID + sequence; server idempotent upsert; resume from acknowledged sequence; retain unacknowledged records.")
 print("LIMITATION: energy is estimated model units, not mAh; no GPS, radio, Keystore, encryption or server was accessed.")
if __name__=="__main__": main()
