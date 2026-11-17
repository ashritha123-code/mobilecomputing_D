import numpy as np, csv
SEED=42
rng=np.random.default_rng(SEED)
U,K,N=8,64,1000
print("Q4 - OFDMA SUBCARRIER ALLOCATION")
print(f"Users={U}, subcarriers={K}, fading realisations={N}, seed={SEED}")
sum_rates={"Fixed contiguous":[],"Interleaved round-robin":[],"Channel-aware best":[]}
fairness={k:[] for k in sum_rates}
for _ in range(N):
    snr=rng.exponential(scale=8.0,size=(U,K)) # illustrative frequency-selective SNR
    rates=np.log2(1+snr)
    allocations={k:[[] for _ in range(U)] for k in sum_rates}
    # 8 contiguous subcarriers per user
    for u in range(U): allocations["Fixed contiguous"][u]=list(range(u*8,(u+1)*8))
    # cyclic round-robin: each user receives every 8th carrier
    for k in range(K): allocations["Interleaved round-robin"][k%U].append(k)
    # best user on each carrier; per-user throughput can be unequal
    best_owner=np.argmax(snr,axis=0)
    for k,u in enumerate(best_owner): allocations["Channel-aware best"][u].append(k)
    for name, alloc in allocations.items():
        user_rates=np.array([sum(rates[u,idx]) if idx else 0.0 for u,idx in enumerate(alloc)])
        total=user_rates.sum()
        j=(total**2)/(U*np.sum(user_rates**2)) if np.sum(user_rates**2)>0 else 0
        sum_rates[name].append(total); fairness[name].append(j)
with open("csv/Q4_ofdma_results.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["allocation","mean_sum_rate_proxy","mean_jains_fairness"])
    for name in sum_rates:
        sr=float(np.mean(sum_rates[name])); jf=float(np.mean(fairness[name]))
        w.writerow([name,sr,jf]); print(f"{name:25s}: mean sum-rate={sr:.3f}, mean Jain fairness={jf:.3f}")
print("Rate proxy: R = log2(1 + SNR). Results are illustrative for the stated channel model.")
