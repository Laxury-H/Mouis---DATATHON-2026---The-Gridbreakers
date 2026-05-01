import os
import subprocess
from pathlib import Path

def run_script(script_path, cwd):
    print(f"Running {script_path}...")
    # Run and stream output directly to console
    result = subprocess.run(["python", script_path], cwd=cwd)
    if result.returncode != 0:
        print(f"Error in {script_path}")
        exit(1)
    else:
        print(f"Finished {script_path}\n")

def main():
    # Base directory for this specific reproduction
    base_dir = Path(__file__).resolve().parent
    project_root = base_dir.parent
    
    print("=====================================================")
    print("Executing Time-Decay Blend Pipeline")
    print("=====================================================")
    
    # Create necessary output folders inside LaHuy
    (base_dir / "results").mkdir(exist_ok=True)
    (base_dir / "results" / "submissions").mkdir(exist_ok=True)
    (base_dir / "results" / "submissions" / "v25_sweeps").mkdir(exist_ok=True)
    (base_dir / "results" / "final_sweeps").mkdir(exist_ok=True)
    
    src_dir = Path("src")
    
    # 1. Run V18 Deep Learning Stack
    run_script(src_dir / "model_v18_dl_stack.py", cwd=base_dir)
    
    # 2. Run V25 Components Stack (uses V18 as anchor)
    run_script(src_dir / "model_v25_components.py", cwd=base_dir)
    
    # 2.1 Run V25 Sweep to get the Base a30 blend
    run_script(src_dir / "blend_v25_sweep.py", cwd=base_dir)
    
    # 3. Run V28 One-Shot Components
    run_script(src_dir / "model_v28_oneshot_components.py", cwd=base_dir)
    
    # 4. Run Time-Decay Blending (10% to 50% shift)
    run_script(src_dir / "blend_time_decay.py", cwd=base_dir)
    
    # 5. CLEANUP: Xóa sạch các file trung gian để chỉ còn lại đúng 1 file duy nhất
    print("Cleaning up intermediate files...")
    import shutil
    try:
        shutil.rmtree(base_dir / "results")
    except Exception as e:
        print(f"Could not remove results folder: {e}")

    print("All models executed successfully.")
    print("=====================================================")
    print(f"FINAL SUBMISSION: {base_dir}/final_submission.csv")
    print("=====================================================")

if __name__ == "__main__":
    main()
