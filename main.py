def show_menu():
    print("\n=== Expense Tracker ===")
    print("1.(Add Expense)")
    print("2.(View All Expenses)")
    print("3.(Total Spent)")
    print("4.(Exit)")


def expense_tracker():
    expenses = []

    while True:
        show_menu()
        choice = input("enter your option (1-4): ").strip()

        if choice == "1":
            category = input("category enter now (example: Food, Travel, Books):  ").strip()
            if not category:
                category = "General"

            try:
                amount = float(input("total (Amount) enter now: "))
                if amount <= 0:
                    print("total 0 or higher number entered!\n")
                    continue
            except ValueError:
                print("please enter correct number!\n")
                continue

            note = input("small note (Optional): ").strip()
            expenses.append({
                "category": category,
                "amount": amount,
                "note": note
            })
            print(f"add successfully: {category} - {amount:.2f}")

        elif choice == "2":
            if not expenses:
                print("\n no add other money spend.")
            else:
                print("\n--- spend money---")
                for idx, item in enumerate(expenses, start=1):
                    note_part = f" ({item['note']})" if item["note"] else ""
                    print(f"{idx}. [{item['category']}] {item['amount']:.2f}{note_part}")

        elif choice == "3":
            total = sum(item["amount"] for item in expenses)
            print(f"\n(Total Spent): {total:.2f}")

        elif choice == "4":
            print("program finish. well done!")
            break

        else:
            print("wrong option! 1 to 4 middle entered.")


if __name__ == "__main__":
    expense_tracker()
