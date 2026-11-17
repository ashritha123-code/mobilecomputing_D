import numpy as np, csv
SEED=42
rng=np.random.default_rng(SEED)
print("Q3 - CDMA SPREADING, CORRELATION AND NEAR-FAR")
print(f"Fixed random seed={SEED}; BPSK; code lengths 8, 16, 64")
rows=[]
for L in [8,16,64]:
    pg_db=10*np.log10(L)
    H=np.array([[1]],dtype=int)
    while H.shape[0] < L:
        H=np.block([[H,H],[H,-H]])
    corr=(H @ H.T)/L
    offdiag=np.abs(corr-np.eye(L))
    max_cross=float(offdiag.max())
    rows.append([L,L,pg_db,max_cross])
    print(f"L={L:2d}: processing gain={L:2d} ({pg_db:.2f} dB), max ideal cross-correlation={max_cross:.1f}")
# Deliberate code collision to illustrate near-far sensitivity when orthogonality is lost.
L=8
target_code=np.ones(L)
interferer_code=np.ones(L)  # identical code: non-orthogonal interference case
target_bits=np.ones(5000)
interferer_bits=rng.choice([-1,1],5000)
noise=rng.normal(0,0.10,(5000,L))
print("Near-far demonstration: identical/non-orthogonal spreading codes (orthogonality lost)")
for amp in [1.0,10.0]:
    received=target_bits[:,None]*target_code + amp*interferer_bits[:,None]*interferer_code + noise
    detected=np.sign(received @ target_code)
    ber=float(np.mean(detected != target_bits))
    print(f"Interferer amplitude={amp:>4.1f}x: target BER={ber:.4f}")
with open("csv/Q3_cdma_metrics.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["spreading_length","ideal_code_channels","processing_gain_db","max_abs_cross_correlation"]); w.writerows(rows)
