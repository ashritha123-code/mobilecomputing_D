"""
B1 - Instrumented background-work scheduler simulation
Models WorkManager-like constraint checks; this is a Python simulation,
not an Android APK or a physical-device measurement.
"""
from dataclasses import dataclass

@dataclass
class WorkItem:
    item_id: str
    priority: int
    encrypted: bool = True

def run_scheduler(items, battery, network, doze, permission, priority_mode=False):
    queue = list(items)
    if priority_mode:
        queue.sort(key=lambda item: (-item.priority, item.item_id))

    result = {
        "enqueued": len(queue), "deferred_cancelled": 0,
        "successful": 0, "peak_workers": 1, "details": []
    }

    for item in queue:
        if not permission:
            status = "CANCELLED - permission revoked"
            result["deferred_cancelled"] += 1
        elif not item.encrypted:
            status = "DEFERRED - encryption required"
            result["deferred_cancelled"] += 1
        elif doze or not network or (battery < 20 and item.priority < 5):
            status = "DEFERRED - device constraint"
            result["deferred_cancelled"] += 1
        else:
            status = "UPLOADED"
            result["successful"] += 1
        result["details"].append((item.item_id, status))

    return result

def show(title, stats):
    print(f"\n{title}")
    print("-" * len(title))
    print(f"Work items enqueued       : {stats['enqueued']}")
    print(f"Deferred / cancelled      : {stats['deferred_cancelled']}")
    print(f"Successful executions     : {stats['successful']}")
    print(f"Peak concurrent workers   : {stats['peak_workers']}")
    for item_id, status in stats["details"]:
        print(f"  {item_id}: {status}")

if __name__ == "__main__":
    items = [
        WorkItem("R1", 2), WorkItem("R2", 5), WorkItem("R3", 1),
        WorkItem("R4", 4), WorkItem("R5", 3, encrypted=False)
    ]
    show("B1 TEST 1 - GOOD CONNECTIVITY", run_scheduler(items, 75, True, False, True))
    show("B1 TEST 2 - LOW BATTERY / DOZE", run_scheduler(items, 12, True, True, True))
    show("B1 TEST 3 - PERMISSION REVOKED", run_scheduler(items, 75, True, False, False))
    show("B1 FIFO ORDER", run_scheduler(items, 75, True, False, True, False))
    show("B1 PRIORITY ORDER", run_scheduler(items, 75, True, False, True, True))
