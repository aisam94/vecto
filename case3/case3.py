
def calculate_overtime_wages(years_of_service, overtime_hours, hourly_rate):
    overtime_wages = 0
    seniority_multiplier = 0

    # determine seniority multiplier
    if years_of_service <= 1:
        seniority_multiplier = 1
    elif years_of_service <= 3:
        seniority_multiplier = 1.1
    elif years_of_service <= 5:
        seniority_multiplier = 1.2
    else:
        seniority_multiplier = 1.7
        
    # calculate wages by overtime hours
    if overtime_hours <= 1:
        overtime_wages = overtime_hours * 2 * seniority_multiplier * hourly_rate
    elif overtime_hours <= 3:
        overtime_wages = (1 * 2 * seniority_multiplier * hourly_rate) + ((overtime_hours - 1) * 2.1 * seniority_multiplier * hourly_rate) 
    else:
        overtime_wages = (1 * 2 * seniority_multiplier * hourly_rate) + (3 * 2.1 * seniority_multiplier * hourly_rate)  + ((overtime_hours - 3) * 3 * seniority_multiplier * hourly_rate)

    overtime_wages = round(overtime_wages, 2)
    print("The overtime wages is: ", overtime_wages)
    return overtime_wages

# execute function
calculate_overtime_wages(2, 2.5, 20)
