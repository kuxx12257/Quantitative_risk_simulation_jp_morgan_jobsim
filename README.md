# Quantitative_risk_simulation
Credit Risk Modeling &amp; Quantization – ML models for loan/mortgage PD prediction, FICO score bucketing via MSE &amp; log‑likelihood, ensemble methods, and expected loss estimation. End‑to‑end framework for risk analytics and capital provisioning.
# Credit Risk Modeling & Quantization 

This repository contains a complete simulation project focused on **credit risk modeling, expected loss estimation, and FICO score quantization**. It integrates classical machine learning, deep learning, and dynamic programming to provide a robust framework for retail loan and mortgage risk management.
##  Project Overview
### Task 1 — Future Graph of Expected Loss
- Baseline **Logistic Regression** model for Probability of Default (PD).
- Computation of **Expected Loss (EL)** as `PD × LGD × EAD`.
- Visualization of borrower‑level EL distribution (the “future graph”).

### Task 2 — Gradient Boosting & Portfolio EL
- **Gradient Boosting Classifier (GBM)** trained on loan data.
- Evaluation using **AUC** and **Brier Score**.
- Calculation of **portfolio‑level expected loss**.

### Task 3 — CNN‑Gating & Ensemble Modeling
- Custom **CNN‑Gating neural network** for PD prediction.
- Integration with **Logistic Regression** and **GBM** into an **ensemble model**.
- Outputs borrower‑level PDs and aggregate portfolio EL.

### Task 4 — FICO Score Quantization
- **Dynamic programming algorithm** for optimal quantization of FICO scores.
- Log‑likelihood maximization to determine bucket boundaries.
- Mapping of continuous FICO scores into discrete **risk ratings**.
##  Data Files

The project uses three datasets:
1. **Simulation Data** — for Task 1 plotting of future expected loss.
2. **Loan Data** — retail loan portfolio with borrower features and default labels.
3. **Mortgage Data** — mortgage portfolio with FICO scores and default labels.


##  Technologies Used
- **Python** (pandas, numpy, scikit‑learn, matplotlib)
- **PyTorch** (for CNN‑Gating model)
- **Dynamic Programming** (for FICO quantization)


##  Outputs
- Borrower‑level **future graph** of expected loss.
- **Portfolio expected loss** summary for loans.
- **PD predictions** from ensemble models.
- **Optimal FICO buckets** and mapped ratings.

- <img width="1024" height="1536" alt="A flowchart style vi" src="https://github.com/user-attachments/assets/dc88f2ca-8240-433e-8230-b3502b655690" />


---
