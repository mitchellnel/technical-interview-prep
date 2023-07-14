def canAttendAllAppointments(appointments):
    if len(appointments) < 2:
        return True

    START, END = 0, 1

    appointments.sort(key=lambda x: x)

    prev_interval = appointments[0]
    for i in range(1, len(appointments)):
        curr_interval = appointments[i]

        if prev_interval[END] > curr_interval[START]:
            return False

        prev_interval = curr_interval

    return True


def main():
    print(
        "Can attend all appointments: "
        + str(canAttendAllAppointments([[1, 4], [2, 5], [7, 9]]))
    )
    print(
        "Can attend all appointments: "
        + str(canAttendAllAppointments([[6, 7], [2, 4], [8, 12]]))
    )
    print(
        "Can attend all appointments: "
        + str(canAttendAllAppointments([[4, 5], [2, 3], [3, 6]]))
    )


main()
