# Project Euler

Python solutions to the freeCodeCamp Project Euler problems.

## Progress

| # | Problem | File | Approach | Time |
|---|---------|------|----------|------|
| 1 | [Multiples of 3 or 5](#problem-1-multiples-of-3-or-5) | [`001_sumOfMultiples.py`](001_sumOfMultiples.py) | Arithmetic-series formula | O(1) |

## Solutions

Each solved problem gets a section below with its statement, the logic used and how to run it.

### Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value `number`.

**Approach:** the multiples of `d` below `number` are `d, 2d, …, m·d`, where `m = (number - 1) // d`. Their sum is `d · m(m + 1) / 2`. Add this sum for `a` and for `b`, then subtract the sum for `a*b`, because those multiples were counted twice. The script reads `a`, `b` and the limit from input, so it is not tied to 3 and 5.

**Time:** O(1). It does three formula evaluations however large `number` is, instead of looping over every number below it.

**Tests:** with `a = 3` and `b = 5`, the function passes all five tests.

| Call | Expected |
|------|----------|
| `multiples_a_and_b(3, 5, 10)` | a number (23) |
| `multiples_a_and_b(3, 5, 49)` | 543 |
| `multiples_a_and_b(3, 5, 1000)` | 233168 |
| `multiples_a_and_b(3, 5, 8456)` | 16687353 |
| `multiples_a_and_b(3, 5, 19564)` | 89301183 |

**Known issues:**

1. Line 11 calls `multiples_a_and_b(a,b,)` without the limit, so the script stops with `TypeError: multiples_a_and_b() missing 1 required positional argument: 'number'`. It should pass `limit` as the third argument.
2. The numbers counted twice are the common multiples of `a` and `b`, which start at their least common multiple, not always at `a*b`. The two are the same only when `a` and `b` share no factor. For example, `a = 2`, `b = 4`, limit 10 gives 24 instead of 20. Using `math.lcm(a, b)` fixes it.

**Run:**

```bash
python3 001_sumOfMultiples.py
```

Enter `3 5`, then `1000`. Once line 11 is fixed, it should print `Sum of multiples of 3 and 5 below 1000 = 233168`.
