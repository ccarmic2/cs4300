import os

FILE_NAMES = ['task6_read_me.txt']
EXPECTED_VALUES = {
    'task6_read_me.txt': 104
}

def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()
            return len(words)
    except FileNotFoundError:
        return None

#create test function for each file in FILE_NAMES
for file in FILE_NAMES:
    def test_word_count():
        assert count_words(file) == EXPECTED_VALUES[file]
    #metaprograming - dynamic function name for file
    globals()[f"test_word_count_{os.path.splitext(file)[0]}"] = test_word_count




