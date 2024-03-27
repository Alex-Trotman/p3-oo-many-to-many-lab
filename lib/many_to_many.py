class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []  # Initialize an empty list to store contracts

    def contracts(self):
        return self._contracts

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise TypeError("contract must be an instance of Contract")
        self._contracts.append(contract)

    def books(self):
        return list({contract.book for contract in self._contracts})

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)
        return contract

    def total_royalties(self):
        return sum({contract.royalties for contract in self._contracts})
    

class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
    
    def contracts(self):
        return self._contracts

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise TypeError("contract must be an instance of Contract")
        self._contracts.append(contract)

    def authors(self):
        # Return a list of unique authors associated with this book's contracts
        return list({contract.author for contract in self._contracts})

class Contract:
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add this contract to the author's and book's list of contracts
        author.add_contract(self)
        book.add_contract(self)
    def contracts_by_date(self):
        pass

