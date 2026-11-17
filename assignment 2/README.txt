MOBILE COMPUTING — ASSIGNMENT 2 (CO2)
Coding package for Questions 1–7

CONTENTS
- One standalone Python source file per question.
- screenshots/: console-style output screenshots for Q1–Q7.
- csv/: raw data/results produced by the scripts.
- plots/: selected result graphs.
- README.txt

REQUIREMENTS
- Python 3.10+
- NumPy and pandas are not needed to run Q1, Q2 and Q6.
- NumPy is needed for Q3, Q4, Q5 and Q7.
- Install NumPy if needed: python -m pip install numpy

HOW TO RUN
Open Command Prompt in this folder and run:
    python Q1_mobile_computing.py
    python Q2_fdma_tdma.py
    ...
    python Q7_shared_scheduler.py

The scripts write CSV files into the csv/ folder. Run them from this package folder so relative output paths work.

IMPORTANT ACADEMIC NOTE
The assignment PDF explicitly says that illustrative/analytical outputs must be independently verified and replaced with measured outputs where required. These scripts implement transparent example models based on the assumptions in the supplied assignment. They are suitable as a reproducible starting point, not proof of real network measurements. In particular, Q5 uses an ideal array-factor approximation, and Q7 uses a simplified queue/pool model. Explain the assumptions and limitations in your viva.
