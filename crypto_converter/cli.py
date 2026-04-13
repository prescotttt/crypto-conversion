"""
crypto_converter.cli
====================
CLI entry point.  Run as:

    python -m crypto_converter [amount] [from asset] [to asset] --ref-from [amount] --ref-to [amount]
    python main.py [amount] [from asset] [to asset] --ref-from [amount] --ref-to [amount]
"""

import argparse
from decimal import Decimal, getcontext

getcontext().prec = 28


def calculate_rate(from_amount: Decimal, to_amount: Decimal) -> Decimal:
    return to_amount / from_amount


def convert(amount: Decimal, rate: Decimal) -> Decimal:
    return amount * rate


def main():
    parser = argparse.ArgumentParser(description="Crypto conversion calculator")

    parser.add_argument("amount", type=Decimal)
    parser.add_argument("from_asset", nargs="?", default="A")
    parser.add_argument("to_asset", nargs="?", default="B")

    parser.add_argument("--ref-from", type=Decimal, required=True)
    parser.add_argument("--ref-to", type=Decimal, required=True)

    args = parser.parse_args()

    rate = calculate_rate(args.ref_from, args.ref_to)
    result = convert(args.amount, rate)

    print(f"Rate: 1 {args.from_asset} = {rate} {args.to_asset}")
    print(f"{args.amount} {args.from_asset} = {result} {args.to_asset}")


if __name__ == "__main__":
    main()
