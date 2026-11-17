import math
print("TASK 2 - GOVERNING DESIGN PARAMETERS")
params = [
 ("Fixed cluster reuse", "N (cluster size)", "Q=sqrt(3N), channels/cell=floor(336/N)"),
 ("Sectorised reuse", "Effective co-channel interferers", "Sector count, beamwidth, antenna discrimination"),
 ("Macro-micro deployment", "Cell radius R and active small cells", "Cell density is proportional to 1/R^2"),
]
for strategy, parameter, effect in params:
    print(f"\n{strategy}\n  Governing parameter: {parameter}\n  Effect: {effect}")
print("\nPlanning constants:")
print("Area=12 km^2 | Spectrum=336 duplex channels | Traffic=0.025 Erlang/user")
print("Blocking target <=2% | Baseline N=7 | Macro radius=0.5 km")
print(f"Hexagonal area at R=0.5 km: {(3*math.sqrt(3)/2)*0.5**2:.4f} km^2")
