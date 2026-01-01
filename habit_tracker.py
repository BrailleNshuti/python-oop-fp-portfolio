from habit import Habit
import storage

# HabitTracker: Main class to manage multiple habits.
# Loads on init, saves after changes.
class HabitTracker:
    def __init__(self):
        self.habits = []
        self.load()  # Load from file on start

    # Add new habit if name unique.
    def add_habit(self, name, periodicity):
        if any(h.name == name for h in self.habits):
            print("Habit already exists.")  # Avoid duplicates
            return
        self.habits.append(Habit(name, periodicity))
        self.save()

    # Delete by name.
    def delete_habit(self, name):
        self.habits = [h for h in self.habits if h.name != name]
        self.save()

    # Complete a habit by name, optional date.
    def complete_habit(self, name, date=None):
        for habit in self.habits:
            if habit.name == name:
                habit.add_completion(date)
                self.save()
                return
        print("Habit not found.")  # Error if missing

    # Save all habits as dicts.
    def save(self):
        storage.save([h.to_dict() for h in self.habits])

    # Load and convert dicts to Habit objects.
    def load(self):
        data = storage.load()
        self.habits = [Habit.from_dict(h) for h in data]