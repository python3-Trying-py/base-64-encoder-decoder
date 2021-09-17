while True:
    import base64
    import random
    que = input("Encode or decode?\n").lower()
    ansE = "encode"
    ansD = "decode"
    if que == ansE:
        queE = input("Input unencoded text below.\n").encode()
        print(base64.b64encode(queE))
    elif que == ansD:
        queD = input("Input encoded text below.\n")
        print(base64.b64decode(queD))
