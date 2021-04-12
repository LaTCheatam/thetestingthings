from app.roman_numerals import parse
from pytest import mark

@mark.parametrize("x,expected", [("IX", 9), ("X", 10)])
def test_roman_numeral_parser(x, expected):
  result = parse(x)

  assert result == expected

