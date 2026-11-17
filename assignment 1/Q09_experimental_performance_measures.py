import math, random, statistics
random.seed(2026)
N,R,n=7,0.5,3.5
D=R*math.sqrt(3*N)
samples=[]
for _ in range(5000):
    rs=random.uniform(0.1*R,R)
    ds=[D*random.uniform(0.85,1.15) for _ in range(6)]
    interf=sum(x**(-n) for x in ds)
    samples.append(10*math.log10(rs**(-n)/interf))
samples.sort()
threshold=12.0
outage=sum(x<threshold for x in samples)/len(samples)
print("TASK 9 - EXPERIMENTAL PERFORMANCE MEASURES")
print("Illustrative fixed-seed SIR sample; 5,000 mobiles")
print(f"Mean SIR                 : {statistics.mean(samples):.2f} dB")
print(f"5th percentile SIR       : {samples[int(.05*len(samples))]:.2f} dB")
print(f"Outage probability <{threshold:.0f} dB : {100*outage:.2f}%")
print("\nOther metrics to collect in a full network simulation:")
print("- Erlang-B call blocking by cell and network")
print("- Channels per cell, site count and handoff rate")
print("- Borrowing frequency, cost, run-time and energy use")
print("\nThese SIR values are illustrative simulation outputs, not measured field results.")
