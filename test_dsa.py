from binary_search import binary_search
from selection_sort import selection_sort
from recursion import factorial, fibonacci
from quicksort import quicksort

def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    val = 4

    assert binary_search(arr, val) == 3


def test_selection_sort():
    int_arr = [1, 2, 5, 10, 22, 5, 6, 12, 11, 13, 20, 21, 0, 3]
    assert selection_sort(int_arr, "asc") == [0, 1, 2, 3, 5 ,5, 6, 10, 11, 12, 13, 20, 21, 22]
    assert selection_sort(int_arr, "desc") == [22, 21, 20, 13, 12, 11, 10, 6, 5, 5, 3, 2, 1, 0]

    char_arr = ["a", "c", "f", "z", "q", "b"]
    assert selection_sort(char_arr, "asc") == ["a", "b", "c", "f", "q", "z"]
    assert selection_sort(char_arr, "desc") == ["z", "q", "f", "c", "b", "a"]


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 0
    assert factorial(8) == 40320
    assert factorial(-1) == 0
    
    
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(8) == 21
    assert fibonacci(-1) == 0


def test_quicksort():
    long_arr = [1, 2, 5, 6, 88, 98, 91, 81, 85, 83, 100, 99, 13, 10, 11, 20, 15]
    assert quicksort(long_arr) == [1, 2, 5, 6, 10, 11, 13, 15, 20, 81, 83, 85, 88, 91, 98, 99, 100]
    assert quicksort([1]) == [1]
    assert quicksort([]) == []
    assert quicksort([5, 2]) == [2, 5]
