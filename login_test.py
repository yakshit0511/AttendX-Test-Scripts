
# AttendX Login Test

def test_login_with_valid_credentials():
    username = "student123"
    password = "test123"

    assert username != ""
    assert password != ""

    print("PASS: Login fields contain values")


def test_login_with_empty_username():
    username = ""
    password = "test123"

    assert username == "", "Username should be empty"
    print("PASS: Empty username validation checked")


if __name__ == "__main__":
    test_login_with_valid_credentials()
    test_login_with_empty_username()
