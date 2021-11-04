import os

current_path = os.getcwd()
print("running from import")
print(current_path)

if __name__ == __main__:
    print("running directly from ", __name__)
    print(current_path)
