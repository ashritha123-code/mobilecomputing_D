# ITA03-MP Assignment 4 – Part II (CO4), Python package

## Files
Six individual programs correspond to Tasks 1–6. `test_inputs/` contains JSON scenario descriptions; `outputs/` contains captured stdout; `screenshots/` contains PNG images rendered from each program's actual captured output.

## Run
Python 3.9+; no third-party packages required.
```powershell
python Task1_OS_Architecture_Evidence.py
python Task2_Single_vs_Multithread_Benchmark.py
python Task3_Runtime_Benchmark.py
python Task4_Mobile_Security_Audit.py
python Task5_Power_Management_Model.py
python Task6_Battery_Aware_Tracker.py
```

## Evidence limitations (important)
The assignment's Part II (pages 14–29) requests Android/iOS device or emulator evidence, profiler traces, ART compilation/GC/heap observations and power instrumentation. This environment cannot access your phone/emulator.
- Task 1: Android commands are attempted only if `adb` and a connected device are available when you run it. iOS live evidence is not collected.
- Task 2: timing is measured on the computer running Python; CPython's GIL affects CPU-bound threads. It is not an Android SoC/Perfetto measurement.
- Task 3: Python workloads and tracemalloc are proxies, not ART launch, compilation, GC or heap measurements.
- Task 4: rule-based sample audit only; edit the CONFIG in the script to match your own application. No APK or traffic was scanned.
- Task 5: counters are synthetic model values, not real battery readings or mAh.
- Task 6: policy is simulated; energy is estimated model units. Encryption, Keystore and TLS are design requirements, not cryptographic operations performed by this simulation.

Do not submit simulated values as physical-device measurements. Run the relevant Android commands and capture actual logs/profiler evidence for the final report.
