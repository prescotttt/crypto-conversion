# Crypto Converter CLI

A simple Python CLI tool for converting between cryptocurrencies using a known reference trade.

## Features

- High precision using Python `Decimal`
- No negative ledger sign confusion
- Simple CLI interface
- Lightweight (no dependencies)

## Installation

Clone the repo:

```
git clone https://github.com/YOURNAME/crypto-converter.git

cd crypto-converter

pip install -e .
```


## Usage

Example reference trade:

```
1845.612 ETH -> 5396.4 USDT
```

Convert 100 ETH:

```
crypto-convert 100 ETH USDT
--ref-from 1845.612
--ref-to 5396.4
```

Output:

```
Rate: 1 ETH = 2.92265 USDT
100 ETH = 292.265 USDT
```

## Running the Tests

```
python -m pytest tests/ -v
```

## Why

Crypto exchange ledgers often record trades as asset movements rather than explicit prices.
This tool derives the conversion rate from a reference trade and applies it to other.
