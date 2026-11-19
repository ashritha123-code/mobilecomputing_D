"""
B3 - Exact versus adaptive UI/graphics optimisation simulation.
Cost = 2 * frame_drops + estimated_energy.
"""
from itertools import product

def cost(quality, cache, target):
    # Simple deterministic illustrative model.
    drops = max(0, target["base_drops"] - cache * 2 - quality)
    energy = quality * 3 + cache * 2
    return 2 * drops + energy

def exact_search(target):
    candidates = []
    for quality, cache in product([1, 2, 3], [1, 2, 3]):
        candidates.append((cost(quality, cache, target), quality, cache))
    return min(candidates)

def adaptive(target):
    # Heuristic begins at medium quality/cache and responds to observed frame time.
    quality, cache = 2, 2
    frame_time = target["frame_time"]
    if frame_time > 16:
        quality = max(1, quality - 1)
        cache = max(1, cache - 1)
    elif frame_time < 12 and target["battery"] > 40:
        quality = min(3, quality + 1)
    return cost(quality, cache, target), quality, cache

if __name__ == "__main__":
    tests = [
        {"name": "Instance 1", "base_drops": 7, "frame_time": 18, "battery": 65},
        {"name": "Instance 2", "base_drops": 2, "frame_time": 10, "battery": 70},
        {"name": "Instance 3", "base_drops": 9, "frame_time": 20, "battery": 25},
    ]
    print("B3.1 - SMALL INSTANCE COMPARISON")
    for t in tests:
        exact = exact_search(t)
        approx = adaptive(t)
        print(f"{t['name']}: exact={exact[0]} (q={exact[1]}, cache={exact[2]}), "
              f"adaptive={approx[0]} (q={approx[1]}, cache={approx[2]}), "
              f"match={'YES' if exact[0] == approx[0] else 'NO'}")

    print("\nB3.2 - COUNTER-EXAMPLE TRACE")
    counter = {"base_drops": 2, "frame_time": 10, "battery": 70}
    print("Adaptive starts at q=2, cache=2; low frame time increases q to 3.")
    print("Exact search:", exact_search(counter))
    print("Adaptive    :", adaptive(counter))
    print("The heuristic changes one parameter locally and may miss a better combination.")

    print("\nB3.3 - SEARCH-SIZE OPERATION COUNTS")
    for q, c in [(3, 3), (5, 6), (8, 10)]:
        print(f"{q} quality levels x {c} cache sizes -> exact evaluations: {q*c}; "
              "adaptive adjustments per window: at most 1")
