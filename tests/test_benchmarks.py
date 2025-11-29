import re

TEST_NUMBER_1 = 1234
TEST_NUMBER_2 = 123456789111111111
TEST_STRING = "   \tThis is a string \n with \r many \t spaces and \n newlines.   "


def digitize_string_conv(n: int):
    """Convert to string and back (Naive)"""
    return [int(d) for d in str(n)]


def digitize_math(n: int):
    """Mathematical digit extraction"""
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    return digits[::-1]


def remove_whitespace_naive(s: str) -> str:
    """Thrasher equivalent"""
    out = ""
    for char in s:
        if not char.isspace():
            out += char
    return out


def remove_whitespace_builder(s: str) -> str:
    """Pythonic list join (Builder equivalent)"""
    return "".join([c for c in s if not c.isspace()])


def remove_whitespace_regex(s: str) -> str:
    """Regex approach"""
    return re.sub(r"\s+", "", s)


# --- Benchmarks ---


def test_benchmark_digitize_math(benchmark):
    benchmark(digitize_math, TEST_NUMBER_2)


def test_benchmark_digitize_conv(benchmark):
    benchmark(digitize_string_conv, TEST_NUMBER_2)


def test_benchmark_naive_strip(benchmark):
    benchmark(remove_whitespace_naive, TEST_STRING)


def test_benchmark_builder_strip(benchmark):
    benchmark(remove_whitespace_builder, TEST_STRING)


def test_benchmark_regex_strip(benchmark):
    benchmark(remove_whitespace_regex, TEST_STRING)
