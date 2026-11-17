import math, random, statistics
random.seed(42)
N, R, n, samples = 7, 0.5, 3.5, 10000
D = R*math.sqrt(3*N)
values = []
# Simplified location-dependent model: serving distance varies from 0.08R to R;
# six first-tier interferers are placed at D with small independent distance variation.
for _ in range(samples):
    r_serv = random.uniform(0.08*R, R)
    interference = sum((D*random.uniform(0.90,1.10))**(-n) for _ in range(6))
    sir = (r_serv**(-n))/interference
    values.append(10*math.log10(sir))
values.sort()
print("TASK 4 - BEST, AVERAGE AND WORST-CASE SIR")
print(f"Illustrative Monte Carlo samples={samples}, seed=42, N={N}, R={R} km, n={n}")
print(f"Best sampled SIR       : {values[-1]:.2f} dB")
print(f"Mean sampled SIR       : {statistics.mean(values):.2f} dB")
print(f"5th percentile SIR     : {values[int(0.05*samples)]:.2f} dB")
print(f"Worst sampled SIR      : {values[0]:.2f} dB")
print("\nNote: illustrative model; not a field measurement or full hexagonal-site simulator.")
