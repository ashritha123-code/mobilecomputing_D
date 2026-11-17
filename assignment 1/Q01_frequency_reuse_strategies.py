import math
S, R = 336, 0.5
print("TASK 1 - ALTERNATIVE FREQUENCY-PLANNING STRATEGIES")
print("Strategy comparison using S=336 channels and R=0.5 km")
print("-"*66)
print(f"{'Cluster N':<12}{'Channels/cell':<18}{'Reuse ratio Q':<17}{'Distance D (km)':<18}")
for N in (3, 4, 7, 12):
    C = S // N
    Q = math.sqrt(3*N)
    D = Q*R
    print(f"{N:<12}{C:<18}{Q:<17.3f}{D:<18.3f}")
print("\nStrategy 1: Fixed reuse - predictable channel groups.")
print("Strategy 2: 3-sector reuse - directional interference reduction.")
print("Strategy 3: Macro-micro + dynamic assignment - hotspot capacity.")
print("Baseline recommendation: N=7 with sectorisation and selective microcells.")
