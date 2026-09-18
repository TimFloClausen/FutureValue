# FutureValue

FutureValue is a small Python program that calculates how money can grow over time using different saving and investment methods.

The project was created to combine **Python programming with mathematics and financial calculations**.

## Features

With FutureValue, you can:

* Choose between different saving and investment methods
* Calculate a **one-time investment**
* Calculate **monthly contributions**
* Choose an investment period in years
* Calculate the effect of **compound interest**
* Compare the development of different investment scenarios
* See how much money was contributed and how much was gained

## Investment Methods

FutureValue currently includes three different methods:

* **MSCI World** – based on an assumed annual return
* **S&P 500** – based on an assumed annual return
* **Bank Savings** – based on an assumed annual interest rate

The returns and interest rates used by the program are assumptions for the calculation. They do **not** represent guaranteed or predicted future returns.

## How It Works

The program uses mathematical formulas to calculate the development of an investment over time.

For monthly contributions, the program calculates the development month by month.

## Example

For example, you could enter:

```text
Initial investment:    CHF 1,000
Monthly contribution:  CHF 200
Investment period:     10 years
Annual return:         5 %
```

FutureValue then calculates how the investment could develop over the selected period.

## Technologies

* **Python 3**
* Mathematical calculations
* Functions
* Loops
* User input
* Data processing
* Different tutorials and sources (see `Sources.txt`)

## Installation

Make sure you have **Python 3** installed.

Clone the repository:

```bash
git clone https://github.com/TimFloClausen/FutureValue.git
```

Then run:

```bash
python main.py
```

## Disclaimer

FutureValue is an educational programming project.

The calculations are based on assumptions and simplified mathematical models. Actual investment returns, interest rates, fees, taxes and inflation can differ significantly.

This program is **not financial advice** and should not be used as the basis for real investment decisions.

## About the Project

I created FutureValue as a personal **application project for an apprenticeship** to practice programming while exploring mathematical concepts such as **compound interest, investment growth and recurring contributions**.

The goal was to build a small application that combines something I enjoy — **programming and mathematics** — with a practical use case related to the financial sector.
