import math
def erlang_b(m, A):
    b = 1.0
    for c in range(1, m+1):
        b = A*b/(c + A*b)
    return b
def inverse_erlang_b(m, target=0.02):
    lo, hi = 0.0, float(m)*3
    for _ in range(100):
        mid = (lo+hi)/2
        if erlang_b(m, mid) > target: hi = mid
        else: lo = mid
    return (lo+hi)/2
print("TASK 3 - HEXAGONAL GEOMETRY, ERLANG-B AND SIR")
R, area, S = 0.5, 12.0, 336
cell_area = (3*math.sqrt(3)/2)*R**2
print(f"Hexagonal cell area = {cell_area:.4f} km^2")
print(f"Ideal geometric cells = ceil({area}/{cell_area:.4f}) = {math.ceil(area/cell_area)}")
print("\nCluster calculations:")
for N in (3,4,7,12):
    C = S//N
    Q = math.sqrt(3*N)
    D = R*Q
    print(f"N={N:2d}: channels/cell={C:3d}, Q={Q:.3f}, D={D:.3f} km, 2% Erlang capacity={inverse_erlang_b(C):.2f} Erlangs")
print("\nSIR for N=7:")
for n in (2.5, 3.5, 4.0):
    sir = 10*math.log10((3*7)**(n/2)/6)
    print(f"n={n:.1f}: omnidirectional SIR={sir:.2f} dB")
print(f"n=4, 3-sector idealised (2 interferers): {10*math.log10(21**2/2):.2f} dB")
