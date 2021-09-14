def sum_of_squares(a):
    squares = 0
    for i in a:
        squares += i*i
    return squares


def test_one():
    assert sum_of_squares([1,2,3]) == 14

test_one()

test_binary_search()


