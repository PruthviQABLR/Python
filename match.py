status_code = 200

match status_code:
    case 200:
        print("success")
    case 300:
        print("redirect")
    case 400:
        print("client error")
    case 500:
        print("server error")
    case _:
        print("unknown")