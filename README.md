# TeenyTinyML 🧠

*A tiny machine learning library built from scratch to understand how machine learning frameworks actually work.*

---

## Overview

**TeenyTinyML** is an educational machine learning library written in pure Python and NumPy that recreates the core ideas behind modern machine learning frameworks such as [scikit-learn](https://scikit-learn.org?utm_source=chatgpt.com).

The goal of this project is not to compete with production-grade libraries, but to provide a clean, readable, and minimal implementation of the fundamental building blocks of machine learning systems.

Instead of treating machine learning as a black box, TeenyTinyML exposes the internal mechanics of:

* Data preprocessing
* Feature engineering
* Model training
* Optimization
* Evaluation metrics
* Pipelines
* Model selection

Every component is implemented from first principles with a strong emphasis on readability, maintainability, and learning.

---

# Why TeenyTinyML?

Most machine learning engineers learn to use frameworks before understanding how they are built.

A simple line like:

```python
model.fit(X, y)
```

hides a significant amount of complexity:

* Data validation
* Parameter initialization
* Optimization
* Mathematical transformations
* State management
* Prediction logic

TeenyTinyML removes that abstraction layer and allows you to see exactly what happens under the hood.

By building and using this library, you will gain a deeper understanding of:

* Linear Algebra
* Optimization
* Statistical Learning
* Object-Oriented Design
* Machine Learning System Architecture
* API Design Patterns

---

# Project Goals

### Educational First

Every implementation should prioritize clarity over performance.

### Minimal Dependencies

Only lightweight scientific libraries should be required.

```text
numpy
```

Optional:

```text
pandas
matplotlib
```

### Consistent API

Every estimator follows the same interface:

```python
fit(X, y)

predict(X)
```

Every transformer follows:

```python
fit(X)

transform(X)

fit_transform(X)
```

This mirrors the design philosophy used by modern ML libraries.

### Built From Scratch

Algorithms should be implemented manually whenever possible rather than wrapping existing machine learning libraries.

---

# Features

## Data Preprocessing

Transform raw data into model-ready features.

### Scalers

* StandardScaler
* MinMaxScaler

### Encoders

* OneHotEncoder

### Imputers

* SimpleImputer

---

## Feature Engineering

Create more informative representations of data.

### Polynomial Features

Generate interaction and polynomial terms.

Example:

```text
Input

[a, b]

Degree = 2

Output

[a, b, a², ab, b²]
```

### Feature Selection

* VarianceThreshold

---

## Machine Learning Algorithms

### Linear Models

#### Linear Regression

Implemented using:

* Normal Equation
* Gradient Descent (future)

#### Logistic Regression

Implemented using:

* Binary Cross Entropy
* Gradient Descent

---

### Nearest Neighbors

#### K-Nearest Neighbors

Supports:

* Classification
* Euclidean Distance

---

### Tree-Based Models

#### Decision Tree

Implemented using:

* Information Gain
* Entropy
* Recursive Splitting

Future extensions:

* Random Forest
* Gradient Boosting

---

## Evaluation Metrics

### Regression Metrics

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Error (MAE)
* R² Score

### Classification Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## Model Selection

### Train-Test Split

```python
from teenytinyml.model_selection import train_test_split
```

### Cross Validation

```python
from teenytinyml.model_selection import cross_val_score
```

---

## Pipelines

Chain preprocessing and modeling steps together.

```python
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", LinearRegression())
])
```

Then:

```python
pipe.fit(X_train, y_train)

predictions = pipe.predict(X_test)
```

---

# Architecture

```text
                ┌─────────────┐
                │   Dataset   │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │Transformer  │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │Feature Eng. │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │ Estimator   │
                └──────┬──────┘
                       │
                       ▼
                ┌─────────────┐
                │  Metrics    │
                └─────────────┘
```

A shared base API allows all components to work together seamlessly.

---

# Project Structure

```text
teenytinyml/

├── base/
│   ├── estimator.py
│   ├── transformer.py
│   └── mixins.py
│
├── preprocessing/
│   ├── scaler.py
│   ├── encoder.py
│   └── imputer.py
│
├── feature_engineering/
│   ├── polynomial.py
│   └── feature_selection.py
│
├── linear_model/
│   ├── linear_regression.py
│   └── logistic_regression.py
│
├── neighbors/
│   └── knn.py
│
├── tree/
│   └── decision_tree.py
│
├── metrics/
│   ├── regression.py
│   └── classification.py
│
├── model_selection/
│   ├── train_test_split.py
│   └── cross_validation.py
│
├── pipeline/
│   └── pipeline.py
│
├── utils/
│   ├── validation.py
│   └── math.py
│
└── tests/
```

---

# Example Usage

## Regression

```python
import numpy as np

from teenytinyml.preprocessing import StandardScaler
from teenytinyml.linear_model import LinearRegression
from teenytinyml.pipeline import Pipeline

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([2, 4, 6, 8, 10])

model = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

model.fit(X, y)

predictions = model.predict(X)

print(predictions)
```

---

## Classification

```python
from teenytinyml.linear_model import LogisticRegression

clf = LogisticRegression(
    lr=0.01,
    n_iters=1000
)

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
```

---

# Learning Outcomes

Building TeenyTinyML will help you understand:

* How machine learning estimators are structured
* How pipelines work internally
* How gradient descent optimizes models
* How decision trees find splits
* How preprocessing transforms data
* How evaluation metrics are computed
* How frameworks like Scikit-Learn achieve API consistency

---

# Non-Goals

TeenyTinyML is intentionally **not** designed to be:

* Faster than Scikit-Learn
* Production ready
* GPU accelerated
* Distributed
* Feature complete

The focus is learning and experimentation.

---

# Roadmap

## Version 0.1

* [ ] BaseEstimator
* [ ] Transformer API
* [ ] StandardScaler
* [ ] LinearRegression
* [ ] LogisticRegression
* [ ] Metrics
* [ ] Train-Test Split
* [ ] Pipeline

## Version 0.2

* [ ] OneHotEncoder
* [ ] SimpleImputer
* [ ] KNN
* [ ] Cross Validation

## Version 0.3

* [ ] Decision Tree
* [ ] Feature Selection
* [ ] Polynomial Features

## Version 0.4

* [ ] Random Forest
* [ ] Gradient Boosting

---

# Philosophy

> "The best way to understand a machine learning library is to build one."

TeenyTinyML is a hands-on exploration of machine learning systems, algorithms, and software design. Every line of code is written with the goal of making machine learning less magical and more understandable.
