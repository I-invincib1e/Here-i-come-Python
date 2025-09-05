from dsa.problems.arrays import two_sum, max_subarray


def test_two_sum_simple():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_two_sum_duplicates():
    # target 6 = 3 + 3
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


def test_two_sum_negative_numbers():
    assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4]


def test_two_sum_with_zero():
    assert sorted(two_sum([0, 4, 3, 0], 0)) == [0, 3]


def test_two_sum_large_numbers():
    assert sorted(two_sum([1000000, 2000000, 3000000], 3000000)) == [0, 1]


def test_two_sum_single_element():
    # This should raise ValueError since no solution exists
    try:
        two_sum([5], 10)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_max_subarray_basic():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_all_negative():
    assert max_subarray([-3, -2, -5]) == -2


def test_max_subarray_single_element():
    assert max_subarray([5]) == 5


def test_max_subarray_empty_array():
    assert max_subarray([]) == 0


def test_max_subarray_mixed_positive_negative():
    assert max_subarray([1, -2, 3, -1, 2]) == 4


def test_max_subarray_all_positive():
    assert max_subarray([1, 2, 3, 4]) == 10


def test_max_subarray_starting_negative():
    assert max_subarray([-1, 2, 3, -4, 5]) == 6
