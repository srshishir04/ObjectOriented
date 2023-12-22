class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book Name: {self.name}, Author: {self.author}, Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine Name: {self.name}, Chief Editor: {self.chief_editor}")

if __name__ == "__main__":
    donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
    donald_duck.print_information()

    compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)
    compartment_no_6.print_information()
