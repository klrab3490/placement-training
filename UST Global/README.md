# UST Global Coding Questions

This repository contains solutions to five coding problems that can be useful for coding interviews and practice. Each problem is explained in detail, along with example inputs and outputs.

## Table of Contents

1. [Matrix Pattern Generation](#problem-1-matrix-pattern-generation)
2. [Chair Arrangement Validation](#problem-2-chair-arrangement-validation)
3. [Matrix Number Generation](#problem-3-matrix-number-generation)
4. [Stone Game](#problem-4-stone-game)
5. [Diamond Pattern Generation](#problem-5-diamond-pattern-generation)

---

## Problem 1: Matrix Pattern Generation

Given an integer `n`, create a matrix of the form:

**Example:**
For `n = 4`, the output should be:

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
| 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| 4 | 3 | 3 | 3 | 3 | 3 | 4 |
| 4 | 3 | 2 | 2 | 2 | 3 | 4 |
| 4 | 3 | 2 | 1 | 2 | 3 | 4 |
| 4 | 3 | 2 | 2 | 2 | 3 | 4 |
| 4 | 3 | 3 | 3 | 3 | 3 | 4 |
| 4 | 4 | 4 | 4 | 4 | 4 | 4 |
|   |   |   |   |   |   |   |

Code File: [Matrix Pattern Generator Python File](./Question%201.py)

## Problem 2: Chair Arrangement Validation

There are 26 chairs named from A to Z that need to be arranged according to the ordinal number of the letter in the English alphabet. Given a string, find the number of chairs that are correctly placed.

**Example:**

Input: `abcdodcek`
Output: `4`

Code File: [Chair Arrangement Validation](./Question%202.py)

## Problem 3: Matrix Number Generation

Given an integer `n`, create a matrix of the form:

**Example:**
For `n = 5`, the output should be:

|   |   |   |   |   |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 2 |
| 3 | 2 | 2 | 2 | 2 |
| 3 | 3 | 3 | 3 | 4 |
| 5 | 4 | 4 | 4 | 4 |
| 5 | 5 | 5 | 5 | 6 |
|   |   |   |   |   |

Code File: [Matrix Number Generation](./Question%203.py)

## Problem 4: Stone Game

Alice and Bob are playing a game called "Stone Game". In this game, each player can remove either 1 or 4 stones from a pile. The player who picks the last stone wins. Alice always goes first.

Your task is to determine if Alice can win if both play optimally.

**Example:**

Input: `3`

Output: `Yes`

Input: `55`

Output: `No`

Code File: [Stone Game](./Question%204.py)

## Problem 5: Diamond Pattern Generation

Generate a diamond-like pattern of numbers as described below.

**Example:**
For `N = 5`, the output should be:

|   |   |   |   |   |
|---|---|---|---|---|
| 1 |   |   |   | 5 |
|   | 2 |   | 4 |   |
|   |   | 3 |   |   |
|   | 2 |   | 4 |   |
| 1 |   |   |   | 5 |
|   |   |   |   |   |

Code File: [Diamond Pattern Generation](./Question%205.py)
