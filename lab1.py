'''
ISTA 131 Lab 1 Spring 2023
'''
def build_dict():
    '''
    Define a function, build_dict(), that returns a dictionary mapping the alphabet to numbers as follows: {'a':1, 'b':2, ..., 'z':26}. Use a loop.
    '''
    import string
    alphabet = {}
    num = 0
    for i in string.ascii_lowercase:
        alphabet[i] = num
        num += 1
    return alphabet

def score_name(alphabet_values, name):
    '''
    Define a function, score_name(), that takes the dictionary from build_dict() and a name and returns the sum of the characters' values.
    For example, 'rich' -> 38
    '''
    alphabet_values = build_dict()
    summ = 0
    for char in name:
        if char.lower() in alphabet_values:
            summ += alphabet_values[char.lower()]
    return summ
    pass

def sort_values(matrix):
    '''
    Define a function, sort_values(), that takes a matrix of integers and returns a list of the values from the matrix sorted from smallest to largest.
    For example, if the matrix is [[1, 3, 4], [-1, -4, 9]], the function should return [-4, -1, 1, 3, 4, 9].
    '''
    normal_list = []
    for row in matrix:
        for element in row:
            normal_list.append(element)
    return sorted(normal_list)
    pass

def bigger(matrix, c=5):
    '''
    Define a function, bigger(), that takes a matrix and a value with a default argument of 5 and returns True if the value is greater than all elements in the matrix, False if not.
    For example, if the matrix is [[1, 2, 3], [4, 5, 6]] and no value is provided (the default is used), the function should return False.
    '''
    for row in matrix:
        for elem in row:
            if c < elem:
                return False
    return True
    pass

def main():
    '''
    The main has been written for you to check your work. Uncomment each section as you complete each function.
    '''
    # creating the alphabet dictionary using build_dict()
    alphabet_values = build_dict()

    # two calls for score_name(), one for the user's first name and one for their last name

    first_name = input('Enter first name: ')
    first_score = score_name(alphabet_values, first_name)
    print('First name score: ', str(first_score))

    last_name = input('Enter last name: ')
    last_score = score_name(alphabet_values, last_name)
    print('Last name score: ', str(last_score))

    # sorting a matrix using sort_values()

    matrix = [[1, 3, 4], [-1, -4, 9]]
    print(sort_values(matrix))


    # finding if a user's value is bigger than all elements in a matrix, two calls of bigger()

    matrix2 = [[1, 2, 3], [4, 5, 6]]
    print(bigger(matrix2))
    print(bigger(matrix2, 10))


if __name__ == '__main__':
    main()
