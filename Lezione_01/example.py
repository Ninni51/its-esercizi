PATH: str = "Lezione_1/example.txt"
mode: str = "r"
encoding: str = "utf-8"

for p in ["Lezione_1/example.txt",   "Lezione_1/example2.txt"]: 
    try:
        file = open(p, mode, encoding=encoding)
        output: str = file.read() 
        print (output)
    except FileNotFoundError as e:
        print (f"File not found: {e}")
    except Exception as e:
        print (f"An error occurred: {e}")
    finally:
        file.close()
file = open (PATH)
# output: str = file.read()
# print(output)
#file.close()


file = open(PATH, "r", encoding="utf-8") 
output: str = file.read()
print(output) 
file.close()

# file = open("Lezione_1/example.txt", "a")
# try:
    # pass
# except Exception as e:
    # pass
# finally:
#    file.close()
# Lezione_1/example.txt
# -/vscode_projects/ITS/Lezione_1/example.txt


# with open("Lezione_1/example.txt", "w") as file:
# print(file.read())