# Habit Tracker App

## Overview
This is a simple Python backend for tracking habits. It lets you add habits (daily or weekly), mark completions, and analyze streaks. Built for IU course DLBDSOOFPP01 to practice OOP and FP.

## Features
- Add/delete habits with name and periodicity.
- Record completions with dates.
- Calculate longest streak overall and per habit (based on no gaps > period).
- Save/load data in JSON.
- Command-line menu for interaction.

## How to Run
1. Install Python 3 (no extra libraries needed).
2. Run `python main.py`.
3. Use the menu to interact.
- Example: Add "Exercise" daily, complete a few times, check streaks.

## Code Explanation
- **habit.py**: Habit class with data (name, period, dates) and streak calc (checks date gaps).
- **storage.py**: JSON save/load functions.
- **habit_tracker.py**: Manages habits list, calls storage.
- **analytics.py**: FP functions for listing, filtering, streaks.
- **main.py**: CLI loop to use the app.

## Testing
- Add habits and complete on consecutive days/weeks to see streaks increase.
- If gap >1 day (daily) or >7 days (weekly), streak resets.
- Data saves to habits.json—edit manually if needed.

## Limitations
- Single-user, no GUI.
- Streaks use unique dates, ignore multiples same day.


Created by Rusingiza Nshuti Braille, jan 2026.
