# Personal Finance Manager

A personal finance management system that helps users track their income, expenses, and savings goals. The system allows users to add, view, update, and delete financial transactions, categorize them, and generate reports to understand their spending patterns.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Bootstrap (HTML, CSS, JavaScript)
- **Database**: SQLite (for simplicity, can be replaced with any other relational database)
- **Authentication**: Django's built-in authentication system
- **Icons**: Font Awesome

## Features

### User Management
- User Registration and Login
- Profile Management

### Transaction Management
- Add, View, Update, and Delete Financial Transactions
- Categorize Transactions (e.g., Food, Rent, Entertainment)
- Filter Transactions by Date and Category

### Category Management
- Add Custom Categories for Transactions
- View and Manage Categories

### Savings Goals
- Set Savings Goals with Target Amount and Target Date
- Track Progress Towards Savings Goals
- Display Live Goals with Progress Percentage of the goals based on the
user’s transactions.
- Display Past Goals with Status (Completed or Failed)

  #### Savings  and Savings goals progress calculation algorithm
    **To calculate the savings:**

    $$
    \text{savings} = \left( \frac{\text{net income of the month}}{\text{number of days in the current month}} - \frac{\text{total debited amount of the current month}}{\text{current day}} \right) \times \text{current day}
    $$

    **To calculate the savings goal progress percentage:**

    $$
    \text{savings goal progress percentage} =  \left( \frac{\text{savings}}{\text{goal target amount}} \right) \times 100
    $$


### Reports
- Generate Monthly and Yearly Reports Showing Income, Expenses, and Savings
- Visual Representations: Pie Charts of Spending Categories

## Setup

### Prerequisites

- Python 3.10
- Django 4.2.14

### Steps to Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ehsonmiraz/finance_management.git
    cd finance_management
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `./.venv/Scripts/activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. **Open your browser and navigate to**:
    ```sh
    http://127.0.0.1:8000/
    ```
