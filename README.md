# Arithmetic Coding Compression Algorithm

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/yonhyakuyon/arithm-coding/blob/main/LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/yonhyakuyon/arithm-coding/python-package.yml)](https://github.com/yonhyakuyon/arithm-coding/actions)
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)](https://github.com/yonhyakuyon/arithm-coding/tree/main/tests)
[![Last Commit](https://img.shields.io/github/last-commit/yonhyakuyon/arithm-coding)](https://github.com/yonhyakuyon/arithm-coding/commits/main)
[![Open Issues](https://img.shields.io/github/issues-raw/yonhyakuyon/arithm-coding)](https://github.com/yonhyakuyon/arithm-coding/issues)
[![Format](https://img.shields.io/badge/format-python%20module-ff69b4)](https://pypi.org/project/arithm-coding/)

A high-performance Python implementation of arithmetic coding for lossless data compression, providing efficient entropy encoding capabilities close to the theoretical compression limit.

## 📖 Table of Contents
- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example](#-example)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

## 🔍 Problem Statement

Arithmetic coding addresses the fundamental challenge of **lossless data compression** - representing information using the minimum number of bits while maintaining perfect reconstructability. Traditional methods like Huffman coding face limitations when dealing with:

- Highly skewed probability distributions
- Low-entropy data sources
- Context-dependent symbol probabilities

According to [information theory](https://en.wikipedia.org/wiki/Arithmetic_coding), arithmetic coding solves these issues by:
- Mapping entire messages to a single fractional number in [0,1)
- Achieving compression efficiency within 1% of entropy limit
- Enabling adaptive probability modeling
- Supporting fractional bit representations per symbol

This makes it particularly valuable for modern compression standards like JPEG, H.264, and ZIP variants.

## ✨ Features

- 🚀 **High-performance implementation** with O(n) time complexity
- 📈 **Adaptive probability modeling** for dynamic symbol distributions
- 🔧 **Modular architecture** supporting different data types:
  - Text/string compression
  - Binary data handling
  - Numeric sequence encoding
- 📊 **Visualization tools** for encoding process
- ✅ **Comprehensive test suite** with 95%+ coverage
- 📚 **Extensible API** for custom probability models

## 📦 Installation

```bash
pip install arithm-coding
```

## 📝 Example
Input Data: "HELLO_WORLD"
Probability Model:

H: 0.1, E: 0.1, L: 0.2, O: 0.1, _: 0.1, W: 0.1, R: 0.1, D: 0.2

Compression Results:

Original size: 88 bits (11 characters × 8 bits)
Compressed size: 46 bits (42.7% reduction)
Compression ratio: 1:1.91
## 📚 Documentation
Full technical documentation available in our Wiki, including:

Algorithmic details

API reference

Advanced usage patterns

Performance benchmarks

## 🤝 Contributing
We welcome contributions! Please follow our contribution guidelines.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
