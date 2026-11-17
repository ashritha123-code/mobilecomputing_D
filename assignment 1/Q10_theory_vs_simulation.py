import math, random, statistics
random.seed(10)
N,n,R=7,4.0,0.5
theory=10*math.log10((3*N)**(n/2)/6)
D=R*math.sqrt(3*N)
vals=[]
for _ in range(10000):
    r=R*random.uniform(.75,1.0)
    ds=[D*random.uniform(.9,1.1) for _ in range(6)]
    vals.append(10*math.log10(r**(-n)/sum(x**(-n) for x in ds)))
print("TASK 10 - THEORY VERSUS SIMULATION")
print(f"Analytical six-interferer SIR (N=7,n=4): {theory:.2f} dB")
print(f"Illustrative Monte Carlo mean SIR         : {statistics.mean(vals):.2f} dB")
print(f"Illustrative Monte Carlo 5th percentile   : {sorted(vals)[499]:.2f} dB")
print("\nReasons for differences:")
print("1. Sampled mobile/interferer distances are unequal.")
print("2. Shadowing and antenna patterns change received powers.")
print("3. Finite network boundaries alter the number of interferers.")
print("4. Erlang-B assumes Poisson arrivals and a loss system.")
print("Simulation is a model; it does not replace field measurements.")
