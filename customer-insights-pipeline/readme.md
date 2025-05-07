# 📊 Customer Purchase Insights Pipeline

This project demonstrates an end-to-end ETL pipeline that integrates customer transactions from multiple sources: JSON-based online orders, CSV-based in-store transactions, and customer profile data from a CRM export. The result is a unified FactOrders table ready for analytics or dashboarding.

---

## 🚀 Objective

Retail companies often struggle to unify online and in-store sales data alongside CRM records. This project solves that by creating a repeatable, modular pipeline using Python and Pandas that:

- Ingests structured (CSV) and semi-structured (JSON) data
- Cleans and transforms it
- Merges it into a clean star-schema-style model
- Outputs a fact table ready for BI tools

---

## 🗂 Project Structure

```
customer-insights-pipeline/
├── data/
│   ├── mock_customers.csv
│   ├── mock_store_sales.csv
│   └── mock_online_orders.json
├── outputs/
│   └── fact_orders.csv
├── scripts/
│   └── etl_pipeline.py
├── requirements.txt
└── .devcontainer/
    └── devcontainer.json
```

---

## 🔧 Tech Stack

- Python 3.10
- Pandas
- JSON & CSV handling
- GitHub Codespaces (DevContainer)

---

## ⚙️ ETL Flow

1. **Extract**
   - Load CRM customer info from CSV
   - Load POS transactions from CSV
   - Load online transactions from JSON logs

2. **Transform**
   - Flatten nested JSON structures
   - Normalize column names and formats
   - Compute `total_value` for each order line
   - Join with customer profiles

3. **Load**
   - Save combined, enriched dataset to `fact_orders.csv` for reporting

---

## 🧪 Output Sample: `fact_orders.csv`

| order_id | customer_id | product_id | quantity | price | timestamp | total_value | region     | customer_segment |
|----------|-------------|------------|----------|--------|-----------|-------------|------------|------------------|
| O2000    | C1001       | P101       | 2        | 59.99  | ...       | 119.98      | East Coast | Silver           |

---

## 🧰 How to Run in Codespaces

1. Launch your GitHub Codespace
2. Navigate to the project root
3. Run:
```bash
cd scripts
python etl_pipeline.py
```
4. Output will be saved in `/outputs/fact_orders.csv`

---

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 💻 Dev Environment

Supports GitHub Codespaces with pre-configured Python environment:
```
.devcontainer/devcontainer.json
```

---

## ✍️ Author

**Bita Ashoori**  
_Data Engineer & Data Automation Specialist_  
📎 [GitHub](https://github.com/bashoori) | [LinkedIn](https://www.linkedin.com/in/bashoori)

---

## ⭐️ Show Your Support

If you found this useful, feel free to star the repo or share feedback!




