SOME_BOOKS = [
    ('The Road', 'Cormac MacCarthy'),
    ('Frankenstein', 'Mary Shelley'),
    ('The Great Gatsby', 'F. Scott Fitzgerald'),
    ('And Then There Were None', 'Agatha Christie'),
    ('Dagon', 'H.P. Lovecraft')
]

STUDENT_IDS = {
    "Alice": 1001,
    "Bob": 1002,
    "Charlie": 1003
}

print(SOME_BOOKS[0:3])

def test_list():
    assert type(SOME_BOOKS) is list
    assert len(SOME_BOOKS[0:3]) == 3
    assert SOME_BOOKS[0:3] == [('The Road', 'Cormac MacCarthy'), 
                               ('Frankenstein', 'Mary Shelley'), 
                               ('The Great Gatsby', 'F. Scott Fitzgerald')]

def test_dict():
    assert type(STUDENT_IDS) is dict
    assert STUDENT_IDS['Bob'] == 1002

