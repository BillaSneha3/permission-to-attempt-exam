attendance = input()
attendance = attendance[ : len(attendance) - 1]
attendance = int(attendance)
medical_reason = input()

if (attendance >= 75):
    print("Allowed to write exam")
elif (attendance <= 75 and medical_reason == "Y"):
    print("Allowed to write exam")
elif (attendance <= 75 and medical_reason == "N"):
    print("Cannot write exam")