import math
print("TASK 5 - SCALING AND SENSITIVITY ANALYSIS")
print("Traffic forecast (0.025 Erlang per subscriber):")
for users in (1000, 10000, 20000, 100000):
    print(f"{users:>7,} subscribers -> {users*0.025:>8.2f} Erlangs")
print("\nRadius scaling for 12 km^2:")
for R in (0.5, 0.25, 0.125):
    A = (3*math.sqrt(3)/2)*R**2
    print(f"R={R:.3f} km, cell area={A:.5f} km^2, ideal cells={math.ceil(12/A)}")
print("\nN=7 ideal SIR sensitivity:")
for n in (2.5, 3.0, 3.5, 4.0):
    sir = 10*math.log10((3*7)**(n/2)/6)
    print(f"path-loss exponent n={n:.1f}: SIR={sir:.2f} dB")
print("\nTrend: smaller cells increase site density; larger N improves ideal SIR")
print("but reduces channels per cell.")
