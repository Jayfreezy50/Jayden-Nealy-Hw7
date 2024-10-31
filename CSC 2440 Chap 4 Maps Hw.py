#Jayden Nealy
class Phonebook:
    def __init__(self):
        self.phonebook = {}

    def add_number(self, name, phone_number):
        self.phonebook[name] = phone_number
        print(f"Added: {name}: {phone_number}")

    def delete_number(self, name):
        if name in self.phonebook:
            del self.phonebook[name]
            print(f"Deleted entry for {name}.")
        else:
            print("Entry not found.")

    def search_number(self, name):
        return self.phonebook.get(name, "Entry not found.")


    def display_number(self):
        if not self.phonebook:
            print("Phonebook is empty.")
        else:
            for name, phone_number in self.phonebook.items():
                print(f"{name}: {phone_number}")

#Diver Code
if __name__ == "__main__":
    pb = Phonebook()

    pb.add_number("Max", "123-456-7890")
    pb.add_number("James", "516-765-4444")

    print(pb.search_number("Max"))
    print(pb.search_number("Tommy"))
    pb.display_number()

    pb.delete_number("James")
    pb.display_number()