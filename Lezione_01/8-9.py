
listamessaggi = ["ciao", "Ciao", "Scemo", "coglione", "Muori", "addio"]

def show_messages(messages:list) -> None:
    for i in messages:
        print(i)

#show_messages(listamessaggi)

sent_messages = []

def send_messages(messages:list) -> list:
    for i in range(len(messages)):
        sent_messages.append(messages[0])
        messages.pop(0)
    print(messages)  
    print(sent_messages)  
send_messages(listamessaggi)

send_messages(["ciao", "Ciao", "Scemo", "coglione", "Muori", "addio"])
print(listamessaggi)

def sandwich(**kwargs) -> list:
    print(f"So, you want a sandwich with {fillings}, correct?")

fillings = {'keyword1': "Dayum",'keyword2': "Goddamn", 'keyword3': "Onion", 'keyword4':"Sauce"}
sandwich(**fillings)