import csv
weights={"Capacity":0.25,"Robustness":0.20,"Mobility":0.20,"Traffic flexibility":0.20,"Cost/simplicity":0.15}
ratings={
"SDMA":[5,3,4,4,2],
"TDMA":[3,3,4,3,4],
"FDMA":[2,3,4,2,4],
"CDMA":[4,4,4,4,3],
"OFDMA":[5,4,4,5,3],
}
print("Q6 - WEIGHTED MULTIPLE-ACCESS SELECTION")
print("Weights: capacity 25%, robustness 20%, mobility 20%, flexibility 20%, cost 15%")
print("Technique | Weighted score / 5")
results=[]
for tech,vals in ratings.items():
    score=sum(w*v for w,v in zip(weights.values(),vals))
    results.append([tech,score])
    print(f"{tech:10s} | {score:.2f}")
with open("csv/Q6_weighted_scores.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["technique","weighted_score_out_of_5"]); w.writerows(results)
print(f"\nHighest score: {max(results,key=lambda x:x[1])[0]}")
print("Deployment choices: TDMA/FDMA voice; CDMA tactical link; OFDMA stadium downlink; scheduled packet access for sensors.")
