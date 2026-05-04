#  Currency Exchange Rate ETL & Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![API](https://img.shields.io/badge/API-ExchangeRate-green)

---

##  Overview

A simple ETL pipeline that collects real-time currency exchange rates, stores historical data, and analyzes rate changes over time.

---

##  Data Source

Data is fetched from:
https://open.er-api.com/v6/latest/USD

---

##  Features

* Fetch real-time exchange rates
* Store data in SQLite
* Track only changed rates (no duplicates)
* Calculate percentage changes
* Basic alert system for rate movement

---

## 🛠️ Tech Stack

Python • Requests • SQLite • Power BI

---

##  Workflow

Extract → Transform → Load → Analyze → Visualize

---

##  Project Structure

```id="c7k2o3"
Currency-ETL-Pipeline/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analysis.py
│   └── config.py
│
├── data/
│   └── currency.db
│
├── main.py
└── README.md
```

---

## ▶️ Run

```bash id="n2kd91"
python main.py
```

---

##  Visualization

Power BI dashboard for tracking trends.

---

##  Tags

ETL • Data Engineering • Python • SQLite • API • Analytics

---
