
# AttendX Attendance Marking Test

def test_attendance_status():
    student_id = "STU001"
    attendance_status = "Present"

    assert student_id != ""
    assert attendance_status in ["Present", "Absent"]

    print("PASS: Attendance data is valid")


if __name__ == "__main__":
    test_attendance_status()
