# 🚗 Interactive Autonomy

<p align="center">
  <b>Learn autonomous driving algorithms through clean, reproducible, and safe implementations.</b>
</p>

---

## 🎯 Purpose

This repository is designed for **educational purposes only**.  
It aims to help users understand autonomous system algorithms through:

- Conceptual understanding  
- Mathematical formulation  
- Clean implementation  
- Visualization  

---

## 📊 Data Usage Policy

### ✅ Allowed Data

This repository should only use:

- Open-source datasets  
- Publicly available data  
- Synthetic or simulated data  
- Self-generated experimental data  

---

### ❌ Prohibited Data

The following must **NOT** be used, uploaded, or shared:

- Company or organizational data  
- Proprietary datasets  
- Confidential or restricted information  
- Internal logs, telemetry, or production data  
- Any data obtained under NDA  

---

## 🔒 Restrictions on Content

This repository must **NOT** include:

- Company-specific implementations  
- Internal workflows or pipelines  
- Proprietary system designs  
- Reverse-engineered confidential systems  
- Any code derived from private repositories  

---

## ⚠️ Ethical and Legal Responsibility

By using or contributing to this repository, you agree:

- To respect data privacy and confidentiality  
- To follow ethical engineering practices  
- To avoid sharing restricted or sensitive information  

If unsure whether something is safe to include:

DO NOT ADD IT.

---

## 🎯 Scope

This repository focuses on:

- Algorithm understanding  
- Simulation-based learning  
- Open implementations  

It is **not intended for production use**.

---

## 🚫 Disclaimer

Maintainers are not responsible for misuse of this repository.

Users are responsible for ensuring:
- Legal compliance  
- No exposure of confidential data  

---

## 🤝 Contribution Guidelines

- Use only safe, open-source data  
- Avoid company-specific logic  
- Keep implementations generic and educational  

---

## ⭐ Summary

✔ Educational  
✔ Open-source friendly  
✔ Safe for public sharing  

✘ No company data  
✘ No confidential workflows  
✘ No proprietary systems  

---

> Keep it clean. Keep it open. Keep it ethical.


# 🚗🚗🚗🚗🚗🚗 Interactive Autonomy 🚗🚗🚗🚗🚗🚗🚗

<p align="center">
  <b>Build and understand autonomous driving systems through code, simulations, and mathematical insights
                                        (only learning purpose).</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue"/>
  <img src="https://img.shields.io/badge/Streamlit-App-red"/>
  <img src="https://img.shields.io/badge/Status-Active-success"/>
</p>

---


## 📚 Documentation


👉 **Local Docs:**
```
docs/build/html/index.html
```

---

## 🧠 Core Concept (Particle Filter)

The belief update follows:

```
p(x_t | z_{1:t}) ∝ p(z_t | x_t) * p(x_t | x_{t-1})
```

Where:
- `p(x_t | x_{t-1})` → motion model  
- `p(z_t | x_t)` → sensor likelihood  

---

## 🚀 Features

- Real-time particle visualization  
- Adaptive particle filtering  
- Noise tuning (motion + sensor)  
- Uncertainty estimation  

---

## 📁 Project Structure

```
Interactive-Autonomy/
│
├── algorithms/
│   ├── particle_filter_app/
│   │   ├── core/
│   │   ├── utils/
│   │   ├── app.py
│   │   └── config.py
│   │
│   ├── kalman_filter_app/
│
├── docs/
├── env/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone

```
git clone <your-repo-url>
cd Interactive-Autonomy
```

### 2. Create Environment

```
python3 -m venv env
```

### 3. Activate

```
source env/bin/activate
```

### 4. Install

```
pip install -r requirements.txt
```

---

## ▶️ Run App

```
PYTHONPATH=. streamlit run algorithms/particle_filter_app/app.py
```

Open:
http://localhost:8501

---

## 📚 Generate Docs

```
cd docs
make html
```

---

## 🛣️ Roadmap

- [x] Particle Filter  
- [ ] Kalman Filter  
- [ ] EKF / UKF  
- [ ] A* Planning  
- [ ] PID Control  
- [ ] Lane Detection  

---

## ⚠️ Notes

- Always run from project root  
- Use `PYTHONPATH=.` for imports  
- Designed for learning (from scratch implementations)

---

## 🤝 Contributing

PRs and ideas welcome 🚀

---

## ⭐ Star this repo if you found it useful!
