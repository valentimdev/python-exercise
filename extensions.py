prompt = input("File name: ")

def checagem(prompt):
    if ".gif" in prompt:
        print("image/gif")
    elif ".pdf" in prompt:
        print("application/pdf")
    elif ".jpeg" or ".jpg" in prompt:
        print ("image/jpeg")
    elif ".png" in prompt:
        print ("image/png")
    elif ".txt" in prompt:
        print ("text/plain")
    elif ".zip" in prompt:
        print ("application/zip")
