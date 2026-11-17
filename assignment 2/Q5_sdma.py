import numpy as np, csv
print("Q5 - SDMA UNIFORM LINEAR ARRAY")
print("Half-wavelength spacing; broadside steering; illustrative 10 dB SIR threshold")
rows=[]
for N in [2,4,8,16]:
    # broadside half-power beamwidth approximation from assignment
    bw_deg=np.degrees(1.772/N)
    # Compute normalized array response for steering at broadside (theta0=0)
    angles=np.linspace(-90,90,3601)
    psi=np.pi*np.sin(np.radians(angles))
    den=N*np.sin(psi/2)
    with np.errstate(divide="ignore",invalid="ignore"):
        af=np.abs(np.sin(N*psi/2)/(den))
    af[np.isnan(af)]=1.0
    # SIR for unit desired response at broadside vs interferer response
    sir_db=-20*np.log10(np.maximum(af,1e-12))
    eligible=angles[(angles>0)&(sir_db>=10)]
    min_sep=float(eligible.min()) if len(eligible) else float("nan")
    rows.append([N,bw_deg,min_sep])
    print(f"N={N:2d}: approximate HPBW={bw_deg:6.2f} degrees; first +angle meeting 10 dB SIR={min_sep:.2f} degrees")
with open("csv/Q5_sdma_beamwidth.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["array_elements","approx_half_power_beamwidth_deg","first_positive_angle_for_10dB_sir"]); w.writerows(rows)
print("Note: the angle result is an ideal array-factor illustration, not a universal deployment limit.")
