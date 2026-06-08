# 🏋️‍♂️ Advanced Gym, Workout Planner & Nutrition Tracker API

A production-grade, highly scalable Backend API engineered with **Django REST Framework (DRF)** and **PostgreSQL**. This system is architected to handle complex relational fitness data structures (workout splits, exercises) alongside a dynamic macro-tracking nutrition system. The entire platform is secured using stateless **JWT Authentication (SimpleJWT)**.

---

## 🚀 Architectural Overview & Engineering Highlights

The platform is divided into two core operational pillars backed by advanced database logic and strict token-based authorization:

### 1. The Workout & Exercise Engine 🧠
* Relational multi-layer hierarchy: **Workout System** (e.g., *Arnold Split, PPL*) ➡️ **Workout Day** (e.g., *Day 1: Chest & Back*) ➡️ **Exercise Components** (Sets, Reps, target muscle groups).
* Uses high-performance **Nested Serializers** to safely aggregate and return entire workout regimes in a single optimized HTTP request.

### 2. Dynamic Nutrition & Macro-Tracking Ecosystem 🍎
* Engineered with dynamic programmatic formulas inside the Database models to calculate intake logic.
* **Food Database (`FoodItem`)**: Stores exact structural macro metrics per 100g (Calories, Proteins, Carbs, Fats).
* **Meal Logs (`Meal` & `MealItem`)**: Tracks user daily logs (Breakfast, Lunch, etc.).
* **Automated Mathematical Pipeline:** Built-in model properties that automatically execute macro weight distribution calculations:
  $$\text{Total Protein} = \left(\frac{\text{protein\_per\_100g}}{100}\right) \times \text{weight\_in\_g}$$

### 3. Bulletproof Security with SimpleJWT 🔒
* Secure authentication pipeline separating open routes from protected resource endpoints.
* Implements Stateless **Bearer Token Verification** utilizing Access and Refresh tokens to protect user workout profiles and personal daily nutrition logs from unauthorized access.

---

## 🛠️ Tech Stack & Middleware

* **Framework:** Python, Django, Django REST Framework (DRF)
* **Authentication:** SimpleJWT (JSON Web Tokens)
* **Database:** PostgreSQL (Production relational mapping)
* **DevOps & Integrity:** Custom CLI Management Commands, Git, Environment isolation

---

## 📂 System File Architecture

```text
Gym-Project/
│
├── src/
│   ├── project/                  # Global configuration & routing middleware
│   │   ├── settings.py           # SimpleJWT settings & DB configurations
│   │   └── urls.py               # Root API router
│   │
│   ├── workouts/                 # Workout management module
│   │   ├── management/commands/
│   │   │   └── seed_workouts.py  # Automation script for exercise data seeding
│   │   ├── models.py             # System, Day, Exercise schemas
│   │   └── serializers.py        # Nested Workout Serializers
│   │
│   └── nutrition/                # Nutrition tracking module
│       ├── models.py             # FoodItem, Meal, MealItem schemas with auto-macro calculation
│       ├── serializers.py        # Macro aggregators
│       └── views.py              # Protected nutrition endpoints
│
├── .gitignore
└── README.md
