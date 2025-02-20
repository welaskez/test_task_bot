import pytest
from utils.case_converters import camel_case_to_snake_case


@pytest.mark.parametrize(
    "string, expected_string",
    [
        ("Anatomy", "anatomy"),
        ("SomeString", "some_string"),
        ("ClassNameEx", "class_name_ex"),
        ("", ""),
    ],
)
def test_camel_case_to_snake_case(string: str, expected_string: str):
    assert camel_case_to_snake_case(string) == expected_string


def test_none_camel_case_to_snake_case():
    with pytest.raises(TypeError):
        camel_case_to_snake_case(None)
