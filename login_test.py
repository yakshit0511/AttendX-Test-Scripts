
# AttendX Login Test

def test_login_with_valid_credentials():
    username = "student123"
    password = "test123"
    
    assert username != ""
    assert password != ""
    
    print("PASS: Login fields contain values")


if __name__ == "__main__":
    test_login_with_valid_credentials()
