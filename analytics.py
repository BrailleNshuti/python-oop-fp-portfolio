# Analytics: Pure FP functions, take habits list, return results.
# No changes to input.

# Return list of habit names.
def list_habits(habits):
    return [h.name for h in habits]

# Filter habits by periodicity.
def filter_by_periodicity(habits, periodicity):
    return [h for h in habits if h.periodicity == periodicity]

# Longest streak across all habits.
def longest_streak_all(habits):
    if not habits:
        return 0
    return max(h.get_streak() for h in habits)  # Max of each habit's max streak

# Dict of longest streak per habit.
def longest_streak_per_habit(habits):
    return {h.name: h.get_streak() for h in habits}