# rfm-python

This repository demonstrates Upselling and Cross-Selling techniques using Python and Pandas with simple machine learning and rule-based logic.

1. **Upselling**: Uses purchase history and user features (like income) to predict whether a customer should be recommended a higher-end product using a Decision Tree Classifier.
2. **Cross-Selling**: Analyzes historical purchases to recommend complementary items often bought together and uses co-occurrence logic for pairwise item recommendation (like a simple association rule engine).

Includes two dummy CSV datasets for both use-cases.

---

## Getting Started

1. Install pandas:
    ```bash
    pip install pandas scikit-learn
    ```

2. Run Upselling Model:
    ```bash
    python .\upselling.py
    ```

3. Run Cross-Selling Logic:
    ```bash
    python .\cross-selling.py
    ```