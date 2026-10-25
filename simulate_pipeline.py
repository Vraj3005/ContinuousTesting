"""
Interactive CI/CD Continuous Testing Pipeline Runner
Simulates Jenkins / GitHub Actions pipeline execution stages for Practical 9
"""
import sys
import os
import time
import subprocess

DIR = os.path.dirname(os.path.abspath(__file__))

def print_banner(text):
    print("=" * 65)
    print(f"   {text}")
    print("=" * 65)

def run_stage(stage_name, command, shell=True):
    print(f"\n[Pipeline] Entering stage: {stage_name}")
    start = time.time()
    try:
        proc = subprocess.run(command, cwd=DIR, shell=shell, capture_output=True, text=True)
        elapsed = time.time() - start
        if proc.stdout:
            print(proc.stdout.strip())
        if proc.stderr and proc.returncode != 0:
            print(proc.stderr.strip())
        if proc.returncode == 0:
            print(f"[Pipeline] Stage '{stage_name}' COMPLETED in {elapsed:.2f}s (SUCCESS)")
            return True
        else:
            print(f"[Pipeline] Stage '{stage_name}' FAILED with exit code {proc.returncode} in {elapsed:.2f}s")
            return False
    except Exception as e:
        print(f"[Pipeline] Stage '{stage_name}' ERROR: {e}")
        return False

def run_pipeline(build_number=1, scenario_name="Standard Build"):
    print_banner(f"Jenkins / CI Pipeline: Build #{build_number} ({scenario_name})")
    
    # Stage 1: Checkout
    s1 = run_stage("Checkout", "git status --short", shell=True)
    if not s1:
        print("\n[Pipeline] Build #{} Finished: FAILURE".format(build_number))
        return False

    # Stage 2: Install Dependencies
    s2 = run_stage("Install Dependencies", "python -m pip install pytest", shell=True)
    if not s2:
        print("\n[Pipeline] Build #{} Finished: FAILURE".format(build_number))
        return False

    # Stage 3: Run Automated Tests
    s3 = run_stage("Run Automated Tests", "python -m pytest -v", shell=True)
    if not s3:
        print("\n" + "=" * 65)
        print(f" [Pipeline] POST-BUILD: FAILURE")
        print(f" Pipeline failed! Automated test assertion failure detected.")
        print(f" Finished: FAILURE (Build #{build_number})")
        print("=" * 65)
        return False

    print("\n" + "=" * 65)
    print(f" [Pipeline] POST-BUILD: SUCCESS")
    print(f" All 5 automated tests passed successfully!")
    print(f" Finished: SUCCESS (Build #{build_number})")
    print("=" * 65)
    return True

def introduce_bug():
    calc_path = os.path.join(DIR, "calculator.py")
    with open(calc_path, "r") as f:
        content = f.read()
    # Introduce bug: return a - b instead of a + b
    buggy = content.replace("return a + b", "return a - b  # INTRODUCED BUG")
    with open(calc_path, "w") as f:
        f.write(buggy)
    print("\n[DEMO] Introduced intentional bug in calculator.py (add returned a - b).")

def restore_bug():
    calc_path = os.path.join(DIR, "calculator.py")
    with open(calc_path, "r") as f:
        content = f.read()
    fixed = content.replace("return a - b  # INTRODUCED BUG", "return a + b")
    with open(calc_path, "w") as f:
        f.write(fixed)
    print("\n[DEMO] Fixed bug in calculator.py (add returned a + b restored).")

def main():
    while True:
        print("\n" + "#" * 65)
        print("   STQA Practical 9: Continuous Testing Pipeline Simulator")
        print("#" * 65)
        print(" 1. Run Pipeline Build (Expected: SUCCESS - All 5 Tests Pass)")
        print(" 2. Introduce Bug in Code & Run Pipeline (Expected: FAILURE)")
        print(" 3. Fix Bug in Code & Run Pipeline (Expected: SUCCESS Restored)")
        print(" 4. Exit")
        choice = input("\n Enter your choice [1-4] (default 1): ").strip() or "1"

        if choice == "1":
            restore_bug()
            run_pipeline(build_number=1, scenario_name="Normal Pass")
        elif choice == "2":
            introduce_bug()
            run_pipeline(build_number=2, scenario_name="Bug Introduced - Failure Demo")
        elif choice == "3":
            restore_bug()
            run_pipeline(build_number=3, scenario_name="Bug Fixed - Success Restored")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please select 1-4.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        run_pipeline(1, "Automated Pass")
    else:
        main()
