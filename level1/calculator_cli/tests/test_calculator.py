import pytest

from level1.calculator_cli.main import calculate, get_operations


class TestGetOperations:
    def test_returns_dict_with_supported_ops(self):
        ops = get_operations()
        expected_keys = {"+", "-", "*", "/", "^"}
        assert set(ops.keys()) == expected_keys
        assert all(callable(func) for func in ops.values())


class TestCalculate:
    def test_addition(self):
        assert calculate("2 + 3") == 5.0

    def test_subtraction(self):
        assert calculate("10 - 4") == 6.0

    def test_multiplication(self):
        assert calculate("3 * 7") == 21.0

    def test_division(self):
        assert calculate("8 / 2") == 4.0

    def test_power(self):
        assert calculate("2 ^ 3") == 8.0

    def test_floats(self):
        assert calculate("1.5 + 2.5") == 4.0

    def test_negative_numbers(self):
        assert calculate("-5 + 10") == 5.0

    def test_invalid_format_too_few_tokens(self):
        with pytest.raises(ValueError, match="Use format: <number> <op> <number>"):
            calculate("2 +")

    def test_invalid_format_too_many_tokens(self):
        with pytest.raises(ValueError, match="Use format: <number> <op> <number>"):
            calculate("2 + 3 + 4")

    def test_invalid_operands(self):
        with pytest.raises(ValueError, match="Operands must be numbers"):
            calculate("a + 3")

    def test_unsupported_operator(self):
        with pytest.raises(ValueError, match="Unsupported operator '%'"):
            calculate("2 % 3")

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calculate("10 / 0")

    def test_whitespace_handling(self):
        assert calculate("  2   +   3  ") == 5.0
