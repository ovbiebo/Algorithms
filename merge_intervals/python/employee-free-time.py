def find_employee_free_time(schedules):
    grouped_schedules = []
    free_hours = []

    for schedule in schedules:
        grouped_schedules += schedule

    grouped_schedules.sort(key=lambda hours: hours[0])
    grouped_schedules.sort(key=lambda hours: hours[1])

    for i in range(1, len(grouped_schedules)):
        if grouped_schedules[i][0] > grouped_schedules[i - 1][1]:
            free_hours.append([grouped_schedules[i - 1][1], grouped_schedules[i][0]])

    return free_hours


if __name__ == '__main__':
    print(f"Free intervals: {find_employee_free_time([[[1, 3], [5, 6]], [[2, 3], [6, 8]]])}")
    print(f"Free intervals: {find_employee_free_time([[[1, 3], [9, 12]], [[2, 4]], [[6, 8]]])}")
    print(f"Free intervals: {find_employee_free_time([[[1, 3]], [[2, 4]], [[3, 5], [7, 9]]])}")
