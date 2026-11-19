"""
B2 - Two equal-size workloads with different constraint behaviour.
All values are deterministic simulation inputs.
"""
from dataclasses import dataclass

@dataclass
class Record:
    name: str
    priority: int
    encrypted: bool = True

def execute_workload(records, battery, network, doze):
    processed = successful = deferred = 0
    log = []
    for r in records:
        processed += 1
        if not r.encrypted:
            deferred += 1
            status = "DEFERRED: encryption missing"
        elif doze or not network or (battery < 20 and r.priority < 5):
            deferred += 1
            status = "DEFERRED: device/network constraint"
        else:
            successful += 1
            status = "DELIVERED"
        log.append((r.name, status))
    return processed, deferred, successful, log

if __name__ == "__main__":
    workload_a = [
        Record("A1", 5), Record("A2", 4), Record("A3", 3),
        Record("A4", 2), Record("A5", 1)
    ]
    workload_b = [
        Record("B1", 5), Record("B2", 4), Record("B3", 3, False),
        Record("B4", 2), Record("B5", 1)
    ]

    for title, records, battery, network, doze in [
        ("WORKLOAD A - EASY", workload_a, 80, True, False),
        ("WORKLOAD B - ADVERSARIAL", workload_b, 15, False, True)
    ]:
        processed, deferred, successful, log = execute_workload(
            records, battery, network, doze
        )
        print(f"\n{title}")
        print("=" * len(title))
        print(f"Records processed : {processed}")
        print(f"Deferrals         : {deferred}")
        print(f"Successful        : {successful}")
        for name, status in log:
            print(f"  {name}: {status}")
