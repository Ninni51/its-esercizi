class ContactManager:
    def __init__(self, contacts:dict[str, list[str]]):
        self.contacts = contacts
    
    def listContacts(self):
        contacts = self.contacts.keys()
        return list(contacts)

    def create_contact(self, name:str, phone_numbers:list[str]) -> dict[str, list[str]]:
        if name in self.contacts:
            raise ValueError("Il contatto è già presente nella lista di contatti")
        else:
            self.contacts.update({name: phone_numbers})
        return {name:phone_numbers}

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict: 
            if contact_name in self.contacts:
                if phone_number not in self.contacts[contact_name]:
                    self.contacts[contact_name].append(phone_number)
                else:
                    raise ValueError("Il numero è già presente nella lista dei contatti")
            else:
                raise ValueError("Il contatto non è presente nella lista dei contatti")
            return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict:
            if contact_name in self.contacts:
                if phone_number in self.contacts[contact_name]:
                    self.contacts[contact_name].remove(phone_number)
                else:
                    raise ValueError("Il numero non è presente nella lista dei contatti")
            else:
                raise ValueError("Il contatto non è presente nella lista dei contatti")
            return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number:str) -> dict: 
            if contact_name in self.contacts:
                if old_phone_number in self.contacts[contact_name]:
                    self.contacts[contact_name].remove(old_phone_number)
                    self.contacts[contact_name].append(new_phone_number)
                else:
                    raise ValueError("Il numero non è nella lista dei contatti")
            else:
                raise ValueError("Il contatto non è presente nella lista dei contatti")
            return {contact_name: self.contacts[contact_name]}

    def search_contact_by_phone_number(self, phone_number:str) -> dict: 
        for i, j in self.contacts.items():
            if phone_number in j:
                return {i: j}
        else:
            raise ValueError("Il numero non è nella lista dei contatti")
