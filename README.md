# Final Project: Test and Behavior Driven Development

This project is a simple Flask-based RESTful API and BDD-tested web service for managing a collection of products.

## 📁 Project Structure

```
final_project/
│
├── service/
│   └── routes.py
│
├── tests/
│   ├── factories.py
│   ├── test_models.py
│   └── test_routes.py
│
├── features/
│   ├── products.feature
│   └── steps/
│       ├── load_steps.py
│       └── web_steps.py
│
├── requirements.txt
└── README.md
```

## 🧪 Features & Functionalities

- ✅ Create, Read, Update, Delete (CRUD) Products
- 🔍 Search Products by:
  - Name
  - Category
  - Availability
- 📋 List all products
- ✅ BDD Scenarios tested with `behave`

## 🧰 Technologies Used

- Flask
- Behave (BDD)
- Factory Boy (test data generation)
- Unittest (unit testing)

## 🚀 Setup Instructions

1. Clone the repository or extract the ZIP.
2. Navigate to the project root directory:

```bash
cd final_project
```

3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the App

To run the app:

```bash
export FLASK_APP=service/routes.py
flask run
```

## 🧪 Running Tests

### Unit Tests:
```bash
pytest
```

### BDD Tests:
```bash
behave
```

---

## 👨‍💻 Author

Final Project submission for peer-reviewed assignment.