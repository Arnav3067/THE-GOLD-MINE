import csv

data = [
    {"Book" : "To Kill A Mockingbird", "Author" : "Harper Lee", "Year" : "1960"},
    {"Book" : "A Brief History Of Time", "Author" : "Stephen Hawkings", "Year" : "1968"},
    {"Book" : "The Great Gatsby", "Author" : "F.Scot Fitzgerald", "Year" : "1922"},
    {"Book" : "The Man Who Mistook His Wife For A Hat", "Author" : "Oliver Sacks", "Year" : "1985"},
    {"Book" : "Pride and Prejudice", "Author" : "Jane Austen", "Year" : "1813"}
]


books = open("Books.csv", "w")
fieldNames = ["Book", "Author", "Year"]
writer = csv.DictWriter(books, fieldnames=fieldNames)
writer.writeheader()
writer.writerows(data)