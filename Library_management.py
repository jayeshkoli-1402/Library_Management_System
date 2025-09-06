print("****Library Managment Program****\n\n".center(80))

while True:
  try:
    userchoice = int(
        input(
            "\nEnter what you want to do?\n(1:Add book)(2:View book)(3:Search book)(4:issue book)(5:return book)(6:Delate book)(0:Exit)"
        ))
    match (userchoice):
  
      case 1:
        book_name_add = input("\nEnter the name of book to add: ")
        author = input(f"Enter the name of author of {book_name_add}: ")
        
        with open("bookshelf.txt", "a") as file:
          file.write(f"{book_name_add} by {author}\n")
          print(f"\n{book_name_add} by {author} added succesfully")
        
          
          
        
  
      case 2:
        try:
          with open("bookshelf.txt", "r") as file:
            books = file.readlines()
          
            if books:
              for i, book in enumerate(books, 1):
                print(f"\n{i}. {book.strip()}")
              print()
            else:
              print("\nNo books found")
  
        except (FileNotFoundError, FileExistsError):
          print("\nNo books found, Library is empty")
  
      case 3:
        book_name_search = input("\nEnter the name of book to search: ").strip().lower()
        try:
          with open("bookshelf.txt", "r") as file:
            found = False
            for line in file:
              if book_name_search in line.lower():
                print(f"\n{book_name_search} is available")
                found = True
                break
    
            if not found:
              print(f"\nSorry! {book_name_search} is not found")
        except (FileNotFoundError, FileExistsError):
          print("\nNo book found, The library is empty")
          
      case 4:
        book_name_issue = input("\nEnter the name of book to issue: ").strip().lower()
  
        try:
          with open("bookshelf.txt", "r") as f:
            books = f.readlines()
    
          issued = False
          with open("bookshelf.txt", "w") as f:  
            for book in books:
              if book_name_issue in book.lower() and not issued:
                issued = True
                
                with open("issued.txt", "a") as issued_file:
                  issued_file.write(book)
              else:
                f.write(book)  
    
          if issued:
            print(f"\n{book_name_issue} issued successfully")
          else:
            print(f"\n{book_name_issue} not found or already issued")
        except(FileExistsError, FileNotFoundError):
          print("\nNo issued books found")
  
    
      case 5:
        book_name_return = input("\nEnter the name of book to return: ").strip().lower()
        returned = False
    
        try:
          with open("issued.txt", "r") as issued:
              books = issued.readlines()
      
         
          with open("issued.txt", "w") as issued_file:
              for book in books:
                  if book_name_return in book.lower() and not returned:
                      returned = True
  
                      with open("bookshelf.txt", "a") as bookshelf_file:
                          bookshelf_file.write(book)   
                  else:
                      issued_file.write(book)
      
          if returned:
              print(f"\n{book_name_return} returned successfully")
          else:
              print(f"\nThe {book_name_return} was not issued or does not belong to this library")
    
        except (FileExistsError, FileNotFoundError):
          print("\nNo book found, Library is empty")
  
    
      case 6:
        book_name_delate = input("\nEnter the name of book to delate: ").lower().strip()
        delated = False
        try:
          with open("bookshelf.txt", "r") as bookshelf:
            books = bookshelf.readlines()
          with open("bookshelf.txt", "w") as bookshelf:
            for book in books:
              if book_name_delate in book.lower() and not delated:
                delated = True
                continue
              bookshelf.write(book)
          if delated:
            print(f"\n{book_name_delate} delated succesfully")
          else:
            print(f"\n{book_name_delate} is already delated or not part of this library")
        except(FileExistsError, FileNotFoundError):
          print("\nNo book found, Library is empty")
  
    
      case 0:
        print("\nExited succesfully")
        break
  
      case _:
        print("\nWrong input please try again")
  
  except (ValueError):
    print("\nWrong input please try again")
    
      