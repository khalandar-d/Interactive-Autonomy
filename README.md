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

## 🎥 Demo

> Add your GIF here (recommended)

```markdown
![Demo](assets/particle_filter.gif)
```

---

## 📚 Documentation

👉 **View Full Documentation (after hosting):**  
https://your-username.github.io/interactive-autonomy/

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


View full documentation:

👉 [Open Docs](docs/build/html/index.html)