"""
tests/test_conversion.py
==================
Unit tests for the crypto conversion rate calculator, conversion, and cli.
Run with:  python -m pytest tests/ -v
"""

from decimal import Decimal
from crypto_converter.cli import calculate_rate, convert
from subprocess import run, PIPE


def test_rate_calculation():
    from_amount = Decimal("2")
    to_amount = Decimal("6000")

    rate = calculate_rate(from_amount, to_amount)

    assert rate == Decimal("3000")


def test_conversion():
    rate = Decimal("3000")
    amount = Decimal("1.5")

    result = convert(amount, rate)

    assert result == Decimal("4500")


def test_fractional_conversion():
    rate = calculate_rate(
        Decimal("1845.612"),
        Decimal("5396.4")
    )

    result = convert(Decimal("100"), rate)

    assert result == Decimal("292.3908167047028302806873817")


def test_cli():
    result = run(
        [
            "python",
            "-m",
            "crypto_converter.cli",
            "10",
            "ETH",
            "USDT",
            "--ref-from",
            "2",
            "--ref-to",
            "6000"
        ],
        stdout=PIPE,
        text=True,
    )

    assert "10 ETH = 30000 USDT" in result.stdout
