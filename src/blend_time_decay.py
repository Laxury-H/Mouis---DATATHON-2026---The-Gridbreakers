import pandas as pd
import numpy as np
from pathlib import Path

def main():
    base_dir = Path(__file__).resolve().parent.parent
    results_dir = base_dir / "results"
    
    # Base: 70% V25 (Recursive) + 30% V18 (Deep Learning)
    base_path = results_dir / "submissions" / "v25_sweeps" / "submission_v25_blend_v18_a30.csv"
    # Anchor: V28 (One-Shot Components, 683k MAE)
    v28_path = results_dir / "submissions" / "submission_v28_oneshot_comp_raw.csv"
    
    # V18 Deep Learning Path to extract Dynamic COGS Ratio
    v18_path = results_dir / "submissions" / "v18" / "submission_v18_dl_stack_anchor_a22.csv"
    
    out_dir = results_dir / "final_sweeps"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    print(" Starting Time-Decay Blending + Sync COGS...")
    
    base = pd.read_csv(base_path)
    v28 = pd.read_csv(v28_path)
    v18 = pd.read_csv(v18_path)
    
    # Tính V18 Dynamic COGS Ratio
    v18_ratio = v18["COGS"] / v18["Revenue"]
    
    n_days = len(base)
    # Tỉ trọng của V28 sẽ tăng dần từ start_w đến end_w
    
    start_w, end_w = (0.10, 0.50) # The 664k MAE Champion config
    blend = base.copy()
    
    # Tạo mảng trọng số tuyến tính tăng dần cho V28
    w_v28 = np.linspace(start_w, end_w, n_days)
    w_base = 1.0 - w_v28
    
    # Chỉ blend Revenue
    blend["Revenue"] = w_base * base["Revenue"] + w_v28 * v28["Revenue"]
    
    # Sync COGS bằng V18 DL Ratio
    blend["COGS"] = blend["Revenue"] * v18_ratio
    
    # Xuất ra file duy nhất tại thư mục gốc của MODEL_Final
    final_output = base_dir / "final_submission.csv"
    blend.to_csv(final_output, index=False)
    print(f"Final submission saved to: {final_output}")
    print(f"Mean Revenue: {blend['Revenue'].mean():,.0f}")

if __name__ == "__main__":
    main()
