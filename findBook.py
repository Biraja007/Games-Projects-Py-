#check if a bk is available
collectionOfBooks=["The Alchemist","How to win friends and influence people","The seven habits of highly effective people"]
print("Enter the name of the Book:")
bookToBeChecked=input()
for book in collectionOfBooks:
    if book==bookToBeChecked:
        print("YES its available")
        break
else:
    print("NO i dont have the book")
    print("Available books are:",collectionOfBooks)
