import traceback

try:
    from habit_tracker import HabitTracker
    import analytics

    # Load tracker
    tracker = HabitTracker()

    # Simple CLI loop
    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add habit")
        print("2. Complete habit")
        print("3. Delete habit")
        print("4. Show all habits")
        print("5. Filter by periodicity")
        print("6. Longest streak overall")
        print("7. Longest streak per habit")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Habit name: ")
            periodicity = input("Periodicity (daily/weekly): ").lower()
            if periodicity in ['daily', 'weekly']:
                tracker.add_habit(name, periodicity)
                print("Habit added.")
            else:
                print("Invalid periodicity.")

        elif choice == "2":
            name = input("Habit name: ")
            tracker.complete_habit(name)
            print("Completion added.")

        elif choice == "3":
            name = input("Habit name: ")
            tracker.delete_habit(name)
            print("Habit deleted.")

        elif choice == "4":
            print("All habits:", analytics.list_habits(tracker.habits))

        elif choice == "5":
            periodicity = input("Periodicity (daily/weekly): ").lower()
            filtered = analytics.filter_by_periodicity(tracker.habits, periodicity)
            print(f"{periodicity.capitalize()} habits:", [h.name for h in filtered])

        elif choice == "6":
            print("Longest streak overall:", analytics.longest_streak_all(tracker.habits))

        elif choice == "7":
            print("Longest streak per habit:", analytics.longest_streak_per_habit(tracker.habits))

        elif choice == "8":
            break

        else:
            print("Invalid choice.")

except Exception as e:
    print("Error occurred:")
    traceback.print_exc()
    input("Press Enter to exit...")
