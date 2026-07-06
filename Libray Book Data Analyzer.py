#PROJECT
#LIBRARY BOOK DATA ANALYZER
import numpy as np
books=np.array([
    [89,120,67,90],
    [120,45,67,83],
    [65,78,90,130],
    [67,123,56,89],
    [190,98,45,32]
])
print("A 2d array of books:",books)

#step 2 (Total books per day)
total_books_perday=np.sum(books,axis=1)
print("Total books per day:",total_books_perday)

#step 3 (Total books per section)
total_books_persection=np.sum(books,axis=0)
print("Total books per section:",total_books_persection)

#step 4 (values>100)filter
filter_values=books[books>100]
print("values greater than 100:",filter_values)

#step 5 (slice data day 2-4)
slice=books[1:4] #use of index for slicing  
print("AFter slicing:",slice)
#step 6(highest books issued)
highest_book=np.max(books)
print("Highest book:",highest_book)

#step 7 (flatten array)#
flattend_aray=books.flatten()
print("Flattened array:", flattend_aray) 
