def add_time(start_time, hours_to_add, minutes_to_add, day=None):
   
    start_hours, start_minutes = map(int, start_time.split(':'))

    
    total_hours = start_hours + hours_to_add
    total_minutes = start_minutes + minutes_to_add

    
    new_hours = (total_hours + total_minutes // 60) % 12
    new_minutes = total_minutes % 60

    
    period = "AM" if total_hours < 12 else "PM"

    
    new_time = f"{new_hours or 12}:{new_minutes:02d} {period}"

    
    days_passed = (total_hours + total_minutes // 60) // 12
    if day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = (days_of_week.index(day.capitalize()) + days_passed) % 7
        new_day = days_of_week[day_index]
        new_time += f", {new_day}"

    
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time

# Example usage
start_time = "3:30 PM"
hours_to_add = 5
minutes_to_add = 45
day = "Monday"
new_time = add_time(start_time, hours_to_add, minutes_to_add, day)
print(new_time)
