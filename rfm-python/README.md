# rfm-python

This script performs RFM (Recency, Frequency, Monetary) analysis on customer transaction data using Pandas. It processes a CSV file (transactions.csv) containing customer purchase history and calculates:

1. **Recency**: Days since last transaction.
2. **Frequency**: Number of transactions.
3. **Monetary**: Total amount spent.

The result is a customer-level DataFrame (rfm) useful for segmentation and marketing analytics.

---

## Getting Started

1. Install pandas:
    ```bash
    pip install pandas
    ```

2. Run main.py:
    ```bash
    python .\main.py
    ```
