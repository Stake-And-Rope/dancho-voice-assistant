import subprocess
def runner():
    try:
        subprocess.run(input("Please, provide path: "))
    except ValueError():
        print("Invalid path")
