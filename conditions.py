status=True

if status:
    print("present")
else:
    print("absent")

marks = 230

if(marks>500):
    print("pass")
else:
    print("Fail")

status_code = 250

if status_code>=200 and status_code <300:
    print("API call successfull")
else:
    print("API Call Unsuccessfull")

collegeMarks = 400

if collegeMarks == 200:
    print("marks is 200")
elif collegeMarks == 300:
    print("marks is 300")
elif collegeMarks == 400:
    print("marks is 400")
else:
    print("marks is unknown")

code = 200
website= "www.yahoo.com"

if code == 200:
    if website == "www.google.com":
        print("all is working")
    else:
        print("website is unknonwn")
else:
    print("Test case failed") 