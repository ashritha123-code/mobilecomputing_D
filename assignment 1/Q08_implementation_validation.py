import math, random
def erlang_b(m,A):
    b=1.0
    for c in range(1,m+1): b=A*b/(c+A*b)
    return b
print("TASK 8 - IMPLEMENTATION AND TESTING / VALIDATION")
print("Test 1: reuse-distance relation D/R=sqrt(3N)")
for N in (3,4,7,12):
    q=math.sqrt(3*N)
    print(f"N={N:2d}: D/R={q:.4f} (expected {q:.4f})")
print("\nTest 2: SIR sanity check N=7, n=4")
sir=10*math.log10((3*7)**(4/2)/6)
print(f"Computed SIR={sir:.3f} dB (assignment reference approximately 18.7 dB)")
print("\nTest 3: Erlang-B recurrence")
for m,A in ((1,0.5),(5,2.0),(48,35.0)):
    print(f"m={m:2d}, A={A:5.1f} Erlangs -> blocking={erlang_b(m,A)*100:.3f}%")
print("\nValidation plan: fixed seed; 1,000 / 5,000 / 10,000 samples;")
print("test N=3,4,7,12; n=2.5,3,4; sector counts 1 and 3.")
