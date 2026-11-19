TECH=[("Baseline polling",120,36,1,"Frequent CPU/radio wake-ups"),("DVFS/efficiency cores",120,36,1,"Lowers compute cost; wake-up count unchanged"),("Doze/app standby",18,12,8,"Defers background work; latency increases"),("Batching + short wakelock",12,8,10,"Coalesces work and releases wakelock promptly"),("Held partial wakelock",120,36,1,"Can prevent deep-idle benefit")]
def main():
 print("TASK 5 - POWER MANAGEMENT MODEL")
 print("Synthetic 8-hour scenario counters; NOT physical measurements or mAh.")
 for name,wake,radio,lat,note in TECH:
  print(f"\\n{name}: wake-ups={wake}, radio-active={radio} min, delivery latency={lat} min")
  print(" ",note)
 reduction=(1-TECH[3][1]/TECH[0][1])*100
 print(f"\\nModeled batching wake-up reduction vs baseline: {reduction:.1f}%")
 print("Conclusion: DVFS targets CPU cost; Doze defers background work; batching reduces repeated radio wake-ups.")
 print("Conflict: held partial wakelock may defeat idle savings.")
 print("LIMITATION: collect real batterystats/Battery Historian/energy profiler data on device.")
if __name__=="__main__": main()
