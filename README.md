# Datathon 2026 - Mouis Team: Giải pháp Dự báo Doanh thu & Tối ưu hoá

## 📌 Thông tin định danh
- **Tên dự án**: Mouis - DATATHON 2026 - The Gridbreakers
- **Tên đội**: Mouis
- **Danh sách thành viên**: Lã Huy Gia Huy, Tạ Nhật Mai

## 💡 Tóm tắt giải pháp
Giải pháp của đội Mouis tập trung vào việc dự báo doanh thu và tối ưu hóa lợi nhuận thông qua một hệ thống học máy toàn diện. Phương pháp tiếp cận cốt lõi bao gồm:
1. **Ensemble Đa tầng (Multi-layer Stacking)**: Sử dụng kết hợp XGBoost, LightGBM, và CatBoost tối ưu hóa hàm suy hao Tweedie để nắm bắt phân phối doanh thu bán lẻ. Hệ thống dự báo song song cả mức giá trị tuyệt đối (Level) và sự thay đổi (Diff) của doanh thu, kết hợp qua TimeSeriesSplit Stacking bằng Linear Regression.
2. **Cầu dao tự động (Automated Circuit Breaker)**: Thông qua hàm đệ quy `recursive_predict_ratio`, hệ thống nội suy tỷ lệ chi phí vốn (COGS/Revenue). Khi tỷ lệ dự báo vượt ngưỡng rủi ro, hệ thống tự động cảnh báo (ngắt cầu dao) nhằm dừng ngay các chiến dịch giảm giá sâu đang ăn mòn biên lợi nhuận.

## 📂 Mô tả cấu trúc thư mục
- `README.md`: File hướng dẫn chạy dự án này.
- `pipeline.py`: File code chính đóng vai trò orchestrator, gọi các mô hình và ghép nối toàn bộ quá trình xử lý từ dữ liệu đến đầu ra.
- `src/`: Thư mục chứa toàn bộ mã nguồn của các base models, hàm feature engineering, chiến lược stacking và time-decay blending.
- `data/`: Thư mục chứa toàn bộ dữ liệu đầu vào (cần đặt các file `sales.csv`, `promotions.csv`, `customers.csv`, `sample_submission.csv` vào đây).
- `results/`: (Sẽ tự động sinh ra) Nơi lưu các kết quả dự đoán trung gian.
- `Báo cáo`: Báo cáo kỹ thuật định dạng NeurIPS và các file hình ảnh/pdf kết quả được đặt chung trong thư mục `MODEL_Final` để Ban Tổ Chức tiện theo dõi.

## ⚙️ Yêu cầu môi trường (Dependencies)
Bạn cần cài đặt Python 3.10+ cùng các thư viện sau (khuyến nghị sử dụng môi trường ảo):
```bash
pip install pandas numpy scikit-learn xgboost lightgbm catboost
```

## 🚀 Hướng dẫn thực thi (Step-by-step)
Để chạy toàn bộ quá trình xử lý, huấn luyện và kết xuất dự báo khớp 100% với Kaggle Leaderboard:

1. Đảm bảo bạn đang đứng tại thư mục `MODEL_Final`:
```bash
cd MODEL_Final
```

2. Cấp quyền thực thi và chạy file pipeline:
```bash
python pipeline.py
```

3. **Kết quả**: Sau khi chạy xong, thư mục trung gian sẽ tự động dọn dẹp. File kết quả cuối cùng là `final_submission.csv` sẽ được sinh ra ở cùng cấp thư mục với `pipeline.py`. Đây chính là file nộp lên hệ thống Kaggle.
