


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