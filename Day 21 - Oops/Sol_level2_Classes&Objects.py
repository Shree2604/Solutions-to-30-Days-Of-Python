# Level 2
# Create a class called PersonAccount.
# It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info,
# add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def total_income(self):
        return sum(item['amount'] for item in self.incomes)

    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)

    def account_info(self):
        info = f"Account Information for {self.firstname} {self.lastname}:\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expenses: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}"
        return info

    def add_income(self, income, description):
        self.incomes.append({'amount': income, 'description': description})

    def add_expense(self, expense, description):
        self.expenses.append({'amount': expense, 'description': description})

    def account_balance(self):
        return self.total_income() - self.total_expense()


# Example usage:
person = PersonAccount("John", "Doe")
person.add_income(1000, "Salary")
person.add_income(500, "Bonus")
person.add_expense(300, "Groceries")
person.add_expense(200, "Utilities")

print(person.account_info())
