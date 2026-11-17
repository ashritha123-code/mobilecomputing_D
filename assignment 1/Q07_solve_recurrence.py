import math
M0, C0, demand = 22, 10.0, 2500.0
print("TASK 7 - SOLVING THE CELL-SPLITTING RECURRENCE")
print("Uniform: M_k=M0*4^k and C_k=C0*4^k")
k = max(0, math.ceil(math.log(demand/C0, 4))) if demand>C0 else 0
print(f"Initial cells M0={M0}")
print(f"Illustrative initial capacity C0={C0:.1f} Erlangs; target demand={demand:.1f} Erlangs")
print(f"Minimum ideal splitting rounds = ceil(log_4(D/C0)) = {k}")
print(f"Cells after {k} rounds = {M0*4**k}")
print(f"Ideal aggregate capacity after {k} rounds = {C0*4**k:.1f} Erlangs")
f=0.25
ks=math.ceil(math.log(demand/C0, 1+3*f)) if demand>C0 else 0
print(f"\nSelective splitting fraction f={f:.2f}")
print(f"Minimum ideal rounds = {ks}")
print(f"Selective cell count = {M0*(1+3*f)**ks:.2f}")
print("These are ideal lower-bound estimates; interference, site limits and handoffs are omitted.")
