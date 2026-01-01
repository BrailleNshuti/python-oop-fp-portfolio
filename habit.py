from datetime import datetime, timedelta

# Habit class: Represents a single habit with its data and behaviors.
# Uses OOP to encapsulate everything related to one habit.
class Habit:
    # Initialize with name and periodicity ('daily' or 'weekly').
    # Sets creation time and empty completions list.
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity  # Type of habit period
        self.created_at = datetime.now()  # When habit was created
        self.completions = []  # List of datetime when completed

    # Add a completion date (default now).
    # Appends and sorts the list for streak calc.
    def add_completion(self, date=None):
        if date is None:
            date = datetime.now()
        self.completions.append(date)
        self.completions.sort()

    # Convert habit to dict for JSON saving.
    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),  # String for JSON
            "completions": [c.isoformat() for c in self.completions]
        }

    # Create habit from dict (for loading from JSON).
    @staticmethod
    def from_dict(data):
        habit = Habit(data["name"], data["periodicity"])
        habit.created_at = datetime.fromisoformat(data["created_at"])
        habit.completions = [datetime.fromisoformat(c) for c in data["completions"]]
        return habit

    # Calculate longest streak: Consecutive completions without gaps.
    # Uses unique dates, checks deltas based on periodicity.
    def get_streak(self):
        if not self.completions:
            return 0
        # Get unique sorted dates (ignore time, multiple same day count as one)
        completion_dates = sorted(set(c.date() for c in self.completions))
        streak = 1  # Start with first completion
        max_streak = 1
        for i in range(1, len(completion_dates)):
            delta = completion_dates[i] - completion_dates[i-1]
            # Continue streak if no gap: <=1 day for daily, <=7 for weekly
            if (self.periodicity == 'daily' and delta.days <= 1) or \
               (self.periodicity == 'weekly' and delta.days <= 7):
                streak += 1
            else:
                streak = 1  # Reset if gap
            max_streak = max(max_streak, streak)
        return max_streak