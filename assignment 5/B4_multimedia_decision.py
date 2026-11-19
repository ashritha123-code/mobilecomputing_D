"""
B4 - Practical video encoding and upload heuristic simulation.
Estimates are qualitative policy outputs, not measured device benchmarks.
"""
def choose_settings(device, network, battery):
    if network == "strong" and device == "high" and battery >= 40:
        return "1080p", "5 Mbps", "UPLOAD NOW"
    elif network in ("strong", "moderate") and battery >= 25:
        return "720p", "2.5 Mbps", "UPLOAD WHEN STABLE"
    else:
        return "480p", "1 Mbps", "DEFER UNTIL SUITABLE CONDITIONS"

if __name__ == "__main__":
    devices = [
        ("High-end phone", "high", "strong", 78),
        ("Mid-range phone", "mid", "moderate", 42),
        ("Entry-level phone", "low", "weak", 18),
        ("Urgent low-battery case", "high", "strong", 22),
    ]
    print("B4.1 - HEURISTIC VIDEO SETTINGS")
    print(f"{'Device':27} {'Network':10} {'Battery':8} {'Resolution':12} {'Bitrate':10} Decision")
    print("-" * 105)
    for name, device, network, battery in devices:
        resolution, bitrate, decision = choose_settings(device, network, battery)
        print(f"{name:27} {network:10} {str(battery)+'%':8} "
              f"{resolution:12} {bitrate:10} {decision}")

    print("\nB4.2 - CHALLENGE CASE")
    print("The urgent low-battery device is deferred by the fixed threshold.")
    print("A user-priority-aware policy could choose 720p at a reduced bitrate "
          "and upload immediately.")
