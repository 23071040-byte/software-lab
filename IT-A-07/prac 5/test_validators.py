import pytest

from validators import is_valid_email


@pytest.mark.parametrize(
    "email",
    [
        "alice@example.com",
        "john.doe@example.org",
        "user_name+tag@example.co.uk",
        "USER123@Sub-Domain.net",
        "a@b.co",
        "first.last+tag@domain-name.io",
        "user@-example.com",
        "user@example..com",
    ],
)
def test_is_valid_email_accepts_valid_addresses(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "plaintext",
        "@example.com",
        "user@",
        "user.example.com",
        "user@@example.com",
        "user@domain",
        "user@domain.c",
        "user name@example.com",
        "user@exam_ple.com",
        "user@exam!ple.com",
        "user@domain.com/extra",
    ],
)
def test_is_valid_email_rejects_invalid_addresses(email):
    assert is_valid_email(email) is False


@pytest.mark.parametrize(
    "email",
    [
        "a@b.co",
        "A@B.COM",
        "12345@67890.net",
        "a+b@c.de",
        "x_y.z@sub.domain.org",
    ],
)
def test_is_valid_email_handles_boundary_and_unusual_but_valid_cases(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "",
        "   ",
    ],
)
def test_is_valid_email_rejects_empty_or_blank_strings(email):
    assert is_valid_email(email) is False


def test_is_valid_email_rejects_missing_at_symbol():
    assert is_valid_email("user.example.com") is False


def test_is_valid_email_rejects_missing_username():
    assert is_valid_email("@example.com") is False


def test_is_valid_email_rejects_missing_domain():
    assert is_valid_email("user@") is False


def test_is_valid_email_rejects_multiple_at_symbols():
    assert is_valid_email("user@@example.com") is False


def test_is_valid_email_rejects_invalid_characters():
    assert is_valid_email("user!name@example.com") is False


def test_is_valid_email_rejects_none_input():
    assert is_valid_email(None) is False


def test_is_valid_email_rejects_integer_input():
    assert is_valid_email(12345) is False


def test_is_valid_email_rejects_list_input():
    assert is_valid_email(["user@example.com"]) is False


def test_is_valid_email_handles_unusual_edge_cases():
    assert is_valid_email("user@sub-domain.example.com") is True
    assert is_valid_email("user.name+test@sub.domain.io") is True
    assert is_valid_email("user@domain.com ") is False
    assert is_valid_email(" user@example.com") is False
    assert is_valid_email("user@example.com\n") is True
