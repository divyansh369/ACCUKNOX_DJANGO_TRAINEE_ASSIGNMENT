# Accuknox Django Trainee Assignment

## Overview

This project contains solutions for:

1. Django Signals behavior analysis
2. Custom iterable Rectangle class in Python

The project experimentally demonstrates:

- Whether Django signals execute synchronously or asynchronously
- Whether Django signals run in the same thread as the caller
- Whether Django signals run in the same database transaction as the caller

---

# Project Structure

```text
accuknox_django/
│
├── core/
├── signals_demo/
├── rectangle_app/
├── manage.py
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository_url>
cd accuknox_django
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

---

# Django Signals Questions

## Question 1

### Are Django signals synchronous or asynchronous by default?

### Conclusion

Django signals execute synchronously by default.

### Proof

A `time.sleep(5)` delay was added inside the signal handler.

The request execution waited until the signal completed execution.

### Observed Output

```text
Total Time Taken: 5.01 seconds
```

This proves that the caller waits for the signal execution to complete.

---

## Question 2

### Do Django signals run in the same thread as the caller?

### Conclusion

Yes, Django signals run in the same thread as the caller by default.

### Proof

Thread IDs were printed from:
- the caller
- the signal handler

### Observed Output

```text
Caller Thread ID: 18356
Signal Thread ID: 18356
```

Both thread IDs were identical.

---

## Question 3

### Do Django signals run in the same database transaction as the caller?

### Conclusion

Yes, Django signals run in the same database transaction as the caller by default.

### Proof

Inside the signal handler:
- a database record was created
- an exception was raised intentionally

The caller operation was wrapped inside `transaction.atomic()`.

Even though both database operations executed before the exception, both records were rolled back.

### Final Database State

```text
<QuerySet []>
<QuerySet []>
```

This confirms that both operations were part of the same database transaction.

---

# Rectangle Iterator Problem

## Requirement

The Rectangle class:
- accepts length and width during initialization
- supports iteration
- returns:
  - `{'length': value}`
  - `{'width': value}`

## Implementation

The iterator protocol was implemented using the `__iter__()` method and `yield`.

## Example

```python
rect = Rectangle(10, 5)

for item in rect:
    print(item)
```

### Output

```text
{'length': 10}
{'width': 5}
```

---

# Running Tests

```bash
python manage.py test
```

---

# Technologies Used

- Python 3.13
- Django 5.x
- SQLite