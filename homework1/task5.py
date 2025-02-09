some_books = [
    ('The Road', 'Cormac MacCarthy'),
    ('Frankenstein', 'Mary Shelley'),
    ('The Great Gatsby', 'F. Scott Fitzgerald'),
    ('And Then There Were None', 'Agatha Christie'),
    ('Dagon', 'H.P. Lovecraft')
]

student_db = {
    "Alice": 1001,
    "Bob": 1002,
    "Charlie": 1003
}

print(some_books[0:3])

def test_structures():
    assert type(some_books) is list
    assert len(some_books[0:3]) == 3
    assert some_books[0:3] == [('The Road', 'Cormac MacCarthy'), 
                               ('Frankenstein', 'Mary Shelley'), 
                               ('The Great Gatsby', 'F. Scott Fitzgerald')]
    assert type(student_db) is dict
    assert student_db['Bob'] == 1002

