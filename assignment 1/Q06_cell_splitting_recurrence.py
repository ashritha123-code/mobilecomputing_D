import math
M0, R0, P0, n = 22, 0.5, 1.0, 3.5
print("TASK 6 - RECURRENCE FOR REPEATED CELL SPLITTING")
print("Uniform splitting: M_k=4*M_(k-1), R_k=R_(k-1)/2")
print("Power model: P_k=P_0/2^(n*k)")
print(f"Initial cells M0={M0}, radius R0={R0} km, normalised power P0={P0}")
print(f"{'Round k':<10}{'Cells':<12}{'Radius km':<15}{'Relative power':<18}{'Area/cell km2'}")
for k in range(5):
    cells = M0*4**k
    radius = R0/(2**k)
    power = P0/(2**(n*k))
    area = (3*math.sqrt(3)/2)*radius**2
    print(f"{k:<10}{cells:<12}{radius:<15.5f}{power:<18.6f}{area:.6f}")
f=0.25
print(f"\nSelective splitting with f={f}: M_k=M0*(1+3f)^k")
for k in range(5):
    print(f"k={k}: cells={M0*(1+3*f)**k:.2f}")
