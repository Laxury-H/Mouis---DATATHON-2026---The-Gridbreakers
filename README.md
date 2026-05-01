<div align="center">
  <h1>🏆 Mouis - DATATHON 2026: The Gridbreakers</h1>
  <p><strong>Giải pháp Dự báo Doanh thu & Tối ưu hoá Lợi nhuận (664k MAE Champion Pipeline)</strong></p>
</div>

---

## 📌 Thông tin định danh
- **Tên dự án**: Mouis - DATATHON 2026 - The Gridbreakers
- **Tên đội**: Mouis
- **Thành viên**: Lã Huy Gia Huy, Tạ Nhật Mai

---

## 💡 Tổng quan Giải pháp
Giải pháp của đội Mouis tập trung vào việc dự báo doanh thu và tối ưu hóa lợi nhuận thông qua một hệ thống học máy toàn diện và kiến trúc Ensemble phức hợp. Giải pháp xuất sắc đạt kết quả **664k MAE** trên tập kiểm thử thông qua các phương pháp cốt lõi:

1. **Ensemble Đa tầng (Multi-layer Stacking - V18 & V25)**: 
   Sử dụng kết hợp các thuật toán Gradient Boosting mạnh mẽ (XGBoost, LightGBM, CatBoost) để tối ưu hóa hàm suy hao Tweedie, nhằm nắm bắt chuẩn xác phân phối doanh thu bán lẻ. Hệ thống dự báo song song ở cả mức giá trị tuyệt đối (Level) và sự biến thiên (Diff), kết hợp qua TimeSeriesSplit Stacking.
2. **Kiến trúc One-Shot (V28)**: 
   Củng cố dự báo dài hạn, đảm bảo tính ổn định của chuỗi thời gian khi đối mặt với các nhiễu động bất ngờ.
3. **Time-Decay Blending**: 
   Kỹ thuật kết hợp linh hoạt dự báo tĩnh và động. Áp dụng tỷ trọng thay đổi theo thời gian (từ 10% đến 50%) nhằm làm mượt kết quả dự báo, tối ưu khả năng nắm bắt xu hướng thị trường thay đổi trong tương lai.
4. **Cầu dao tự động (Automated Circuit Breaker) & Sync COGS**: 
   Kiểm soát rủi ro thông qua việc đồng bộ nội suy tỷ lệ chi phí vốn (COGS/Revenue) từ mô hình V18 DL Stack, tự động cảnh báo giảm thiểu thất thoát khi các chiến dịch giảm giá gây ảnh hưởng tiêu cực tới biên lợi nhuận.

---

## 📂 Cấu trúc Repository

```text
Mouis---DATATHON-2026---The-Gridbreakers/
├── data/                         # Thư mục chứa toàn bộ dữ liệu đầu vào (cần tải về trước khi chạy)
│   ├── customers.csv
│   ├── order_items.csv
│   ├── orders.csv
│   ├── products.csv
│   ├── promotions.csv
│   ├── sales.csv
│   ├── web_traffic.csv
│   └── sample_submission.csv
├── notebooks/                    # Môi trường nghiên cứu và phát triển thử nghiệm
│   ├── baseline.ipynb            # Notebook phân tích EDA và baseline model ban đầu
│   └── mouis-part-3.ipynb        # Phân tích chuyên sâu 
├── src/                          # Mã nguồn lõi của các thành phần dự báo (Core scripts)
│   ├── data_prep.py              # Xử lý, làm sạch và Feature Engineering
│   ├── model_v18_dl_stack.py     # Base model V18: DL Stacking
│   ├── model_v25_components.py   # Kiến trúc V25 và hàm đệ quy (Recursive Components)
│   ├── model_v28_oneshot_components.py # Mô hình V28: One-Shot Forecasting
│   ├── blend_v25_sweep.py        # Tinh chỉnh tỷ trọng blend nội bộ V25
│   └── blend_time_decay.py       # Tập lệnh Blending theo Time-Decay và xuất file cuối cùng
├── pipeline.py                   # Script điều phối (Orchestrator) toàn bộ luồng thực thi
├── Mouis_Technical_Report.pdf    # Báo cáo kỹ thuật chi tiết theo chuẩn NeurIPS
└── README.md                     # Tài liệu hướng dẫn sử dụng (bạn đang đọc file này)
```

---

## ⚙️ Yêu cầu Môi trường (Dependencies)
Dự án yêu cầu **Python 3.10+**. Khuyến nghị sử dụng môi trường ảo (Virtual Environment hoặc Conda) để tránh xung đột thư viện.

Cài đặt các gói phụ thuộc cần thiết:
```bash
pip install pandas numpy scikit-learn xgboost lightgbm catboost
```

*(Lưu ý: Môi trường có hỗ trợ GPU sẽ giúp quá trình huấn luyện các mô hình CatBoost và XGBoost diễn ra nhanh hơn)*

---

## 🚀 Hướng dẫn Thực thi (Reproduction Pipeline)
Hệ thống đã được thiết kế hoàn toàn tự động hoá. Để chạy toàn bộ quá trình xử lý từ dữ liệu thô, huấn luyện mô hình, thực hiện blended predictions và xuất kết quả file `final_submission.csv`:

### Bước 1: Chuẩn bị Dữ liệu
Đảm bảo bạn đã đặt toàn bộ dữ liệu gốc của Datathon 2026 vào thư mục `data/` đúng với cấu trúc như phần mô tả bên trên.

### Bước 2: Kích hoạt Pipeline
Tại thư mục gốc của repository, mở Terminal/Command Prompt và chạy file `pipeline.py`:
```bash
python pipeline.py
```

### Bước 3: Luồng Xử lý của Hệ thống
Script `pipeline.py` sẽ thực thi lần lượt qua 5 giai đoạn:
1. **Huấn luyện V18 DL Stack** (`src/model_v18_dl_stack.py`)
2. **Huấn luyện V25 Components** (`src/model_v25_components.py`) và tạo điểm neo Base Sweep (`src/blend_v25_sweep.py`).
3. **Chạy V28 One-Shot** (`src/model_v28_oneshot_components.py`) làm bộ phận ổn định xu hướng.
4. **Time-Decay Blending & Đồng bộ hóa COGS Ratio** (`src/blend_time_decay.py`). Kết hợp 3 nhánh mô hình trên bằng ma trận tỷ trọng tăng dần theo trục thời gian.
5. **Dọn dẹp (Cleanup)**: Toàn bộ folder lưu trữ trung gian `results/` sẽ được xoá tự động để tiết kiệm bộ nhớ, chỉ giữ lại file kết quả cuối cùng.

### Bước 4: Nhận Kết quả
Sau khi luồng xử lý kết thúc thành công (thông báo `All models executed successfully`), bạn sẽ nhận được file dự báo cuối cùng:
📍 **`final_submission.csv`** (Được xuất ra trực tiếp ở thư mục gốc).

Đây chính là file sẵn sàng để nộp (Submit) lên hệ thống đánh giá Kaggle.

---

## 🔬 Báo cáo Kỹ thuật (Technical Report)
Chi tiết về toán học, phân tích Feature Importance, cơ chế rò rỉ dữ liệu (Data Leakage Control), và tính hiệu quả phân phối mô hình được diễn giải cặn kẽ trong file:
**📄 `Mouis_Technical_Report.pdf`** (Báo cáo đáp ứng các tiêu chuẩn nghiêm ngặt về học thuật).

---

> Chúc ban giám khảo và hội đồng chuyên môn có một trải nghiệm tốt nhất với kiến trúc dự báo của **Mouis**.
