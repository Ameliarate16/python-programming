worker_type = "part_time"
hours_worked = 25
weekly_wage = 0

if worker_type == "full_time":
    #check for overtime
    if hours_worked > 40:
        #if overtime, they worked full hours plus extra
        weekly_wage = 50 * 40 + 60 * (hours_worked - 40)
    else:
        #if no overtime, they may not have worked full hours
        weekly_wage = 50 * hours_worked

elif worker_type == "part_time":
    #check for overtime
    if hours_worked > 20:
        #if overtime, they worked full hours plus extra
        weekly_wage = 65 * 20 + 70 * (hours_worked - 20)
    else:
        #if no overtime, they may not have worked full hours
        weekly_wage = 65 * hours_worked

elif worker_type == "contract":
    #no overtime, just reduce total wage by 25%
    weekly_wage = hours_worked * 120 * 0.75

print(f"weekly wage = ${weekly_wage}")