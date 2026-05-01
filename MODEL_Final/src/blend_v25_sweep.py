import pandas as pd
from pathlib import Path

# Paths
base_dir = Path(__file__).resolve().parent.parent
v25_path = base_dir / "results" / "submissions" / "submission_v25_comp_stack_raw.csv"
v18_path = base_dir / "results" / "submissions" / "v18" / "submission_v18_dl_stack_anchor_a22.csv"
out_dir = base_dir / "results" / "submissions" / "v25_sweeps"
out_dir.mkdir(parents=True, exist_ok=True)

if not v25_path.exists() or not v18_path.exists():
    print("Files not found. Check paths.")
else:
    v25 = pd.read_csv(v25_path)
    v18 = pd.read_csv(v18_path)
    
    alpha = 0.3 # 30% V25, 70% V18
    print(f" [V25 SWEEP] Creating blend of V18 and V25 (Alpha={alpha})...")
    
    out = v25.copy()
    out["Revenue"] = (1 - alpha) * v18["Revenue"] + alpha * v25["Revenue"]
    out["COGS"] = (1 - alpha) * v18["COGS"] + alpha * v25["COGS"]
    
    name = f"submission_v25_blend_v18_a30.csv"
    out_path = out_dir / name
    out.to_csv(out_path, index=False)
    print(f" Đã tạo: {name}")
        
    print(f"\\n All files saved at: {out_dir}")
