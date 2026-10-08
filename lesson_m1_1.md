# Lesson M1.1: Real Numbers, Properties, and Order

**Prerequisites:** None — this is the starting point

**Learning Objectives:**
- Identify and classify numbers within the real number system
- Apply the algebraic properties of real numbers
- Work fluently with inequalities and absolute value
- Use interval notation correctly
- Understand the completeness property (preview for analysis)

---

## High-school level — Numbers, order, and distance

Start with the number line: a real number names a position, an inequality compares positions, and absolute value measures distance. Familiar arithmetic is the entry point; later sections ask why the rules work.

## 1. The Real Number System

The real numbers, denoted **ℝ**, form the foundation of all calculus and analysis. They consist of every point on the number line — no gaps.

### 1.1 Subsets of ℝ

| Set | Symbol | Description | Examples |
|-----|--------|-------------|----------|
| Natural Numbers | ℕ | Counting numbers | 1, 2, 3, 4, ... |
| Whole Numbers | ℕ₀ | Naturals plus zero | 0, 1, 2, 3, ... |
| Integers | ℤ | Whole numbers and negatives | ..., -2, -1, 0, 1, 2, ... |
| Rational Numbers | ℚ | Ratios of integers (p/q, q ≠ 0) | 1/2, -3/4, 7, 0.333... |
| Irrational Numbers | ℝ \ ℚ | Cannot be expressed as ratio | √2, π, e |
| Real Numbers | ℝ | All rationals and irrationals | Everything above |

**Key relationship:** ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ

<details class="math-explainer">
<summary>Explain the chain of number sets</summary>
<p><strong>Read the whole expression:</strong> N is contained in Z, which is contained in Q, which is contained in R.</p>
<dl><dt>N, natural numbers</dt><dd>Counting numbers 1, 2, 3, and so on.</dd>
<dt>Z, integers</dt><dd>Whole numbers, their negatives, and zero.</dd>
<dt>Q, rational numbers</dt><dd>Fractions of integers with a nonzero denominator.</dd>
<dt>R, real numbers</dt><dd>All points on the number line.</dd>
<dt>⊂, &#x27;is contained in&#x27;</dt><dd>Every member of the set on the left is also in the set on the right.</dd></dl>
<p><strong>Example:</strong> −2 is an integer and hence a rational and a real number; 1/2 is rational and real but not an integer.</p>
</details>

### 1.2 Rational vs. Irrational

A number is **rational** if and only if its decimal expansion either:
- Terminates (e.g., 0.75), or
- Repeats (e.g., 0.333... = 1/3)

A number is **irrational** if its decimal expansion neither terminates nor repeats.

**Example:** Is 0.101001000100001... rational or irrational?

The pattern grows but never repeats — it's irrational.

---

## 2. Algebraic Properties of Real Numbers

For all real numbers a, b, c:

### 2.1 Field Properties

| Property | Addition | Multiplication |
|----------|----------|----------------|
| **Closure** | a + b ∈ ℝ | a · b ∈ ℝ |
| **Commutative** | a + b = b + a | a · b = b · a |
| **Associative** | (a + b) + c = a + (b + c) | (a · b) · c = a · (b · c) |
| **Identity** | a + 0 = a | a · 1 = a |
| **Inverse** | a + (-a) = 0 | a · (1/a) = 1, for a ≠ 0 |
| **Distributive** | a · (b + c) = a · b + a · c | |

### 2.2 Why These Matter

These aren't just abstract rules — they justify every algebraic manipulation you'll ever do.

**Example:** Why can we "factor out" in the expression 3x + 3y?

By the distributive property: 3x + 3y = 3(x + y)

**Example:** Why does (-1)(-1) = 1?

We need: (-1) + (-1)(-1) = (-1)(1 + (-1)) = (-1)(0) = 0

So (-1)(-1) must be the additive inverse of (-1), which is 1.

---

## 3. Order Properties

The real numbers are **ordered**: for any two distinct reals, one is larger.

### 3.1 Trichotomy

For any real numbers a and b, exactly one holds:
- a < b
- a = b
- a > b

### 3.2 Properties of Inequalities

For real numbers a, b, c:

| Property | Statement |
|----------|-----------|
| **Transitive** | If a < b and b < c, then a < c |
| **Addition** | If a < b, then a + c < b + c |
| **Multiplication (positive)** | If a < b and c > 0, then ac < bc |
| **Multiplication (negative)** | If a < b and c < 0, then ac > bc |

⚠️ **Critical:** Multiplying or dividing by a negative number **reverses** the inequality.

**Example:** Solve -2x < 6

Dividing by -2 (negative), we reverse: x > -3

---

## 4. Absolute Value

### 4.1 Definition

The **absolute value** of a real number a is:

$$|a| = \begin{cases} a & \text{if } a \geq 0 \\ -a & \text{if } a < 0 \end{cases}$$

Geometrically: |a| is the distance from a to 0 on the number line.

<details class="math-explainer">
<summary>Explain absolute-value bars</summary>
<p><strong>Read the whole expression:</strong> The absolute value of a is the distance from a to zero.</p>
<dl><dt>| |, absolute-value bars</dt><dd>Take distance, so the result is never negative.</dd>
<dt>a</dt><dd>The input whose distance from zero we measure.</dd>
<dt>≥, &#x27;greater than or equal to&#x27;</dt><dd>Zero is allowed as the smallest possible distance.</dd></dl>
<p><strong>Example:</strong> The point −3 is three units from zero, so |−3| = 3.</p>
</details>

### 4.2 Key Properties

For all real a, b:

1. |a| ≥ 0, and |a| = 0 if and only if a = 0
2. |-a| = |a|
3. |ab| = |a| · |b|
4. |a/b| = |a| / |b| (for b ≠ 0)
5. **Triangle Inequality:** |a + b| ≤ |a| + |b|

### 4.3 Solving Absolute Value Equations and Inequalities

**Type 1:** |x| = k (where k ≥ 0)
- Solution: x = k or x = -k

**Type 2:** |x| < k (where k > 0)
- Solution: -k < x < k

**Type 3:** |x| > k (where k ≥ 0)
- Solution: x < -k or x > k

**Example:** Solve |2x - 3| ≤ 5

This means: -5 ≤ 2x - 3 ≤ 5

Add 3: -2 ≤ 2x ≤ 8

Divide by 2: -1 ≤ x ≤ 4

---

## 5. Interval Notation

Intervals describe connected subsets of ℝ.

| Notation | Set-Builder | Description |
|----------|-------------|-------------|
| (a, b) | {x : a < x < b} | Open interval |
| [a, b] | {x : a ≤ x ≤ b} | Closed interval |
| [a, b) | {x : a ≤ x < b} | Half-open (closed left) |
| (a, b] | {x : a < x ≤ b} | Half-open (closed right) |
| (a, ∞) | {x : x > a} | Unbounded above |
| (-∞, b] | {x : x ≤ b} | Unbounded below |
| (-∞, ∞) | ℝ | All real numbers |

**Convention:** Parentheses ( ) mean "not included"; brackets [ ] mean "included."

∞ and -∞ are never included (always use parentheses with them).

---

## Undergraduate level — Sets, bounds, and proof

The first five sections describe how real numbers behave. The next step is to make claims about *sets* of numbers and justify them from definitions. A bound is a ceiling for every member of a set; it need not itself belong to that set. Proofs in this lesson use definitions rather than examples alone.

## 6. Completeness (Preview)

Here's the property that separates ℝ from ℚ:

**Completeness Axiom:** Every nonempty subset of ℝ that is bounded above has a least upper bound (supremum) in ℝ.

<details class="math-explainer">
<summary>Explain a least upper bound</summary>
<p><strong>Read the whole expression:</strong> Every nonempty set of real numbers with some ceiling has a smallest possible ceiling among real numbers.</p>
<dl><dt>R, real numbers</dt><dd>The number system containing the set and its supremum.</dd>
<dt>sup S, &#x27;supremum of S&#x27;</dt><dd>The least upper bound of S; it need not be a member of S.</dd>
<dt>upper bound</dt><dd>A number at least as large as every element of S.</dd></dl>
<p><strong>Example:</strong> For S = {1 − 1/n : n = 1, 2, ...}, every element is below 1, yet elements approach 1; sup S = 1.</p>
</details>

**Why ℚ fails this:** Consider S = {x ∈ ℚ : x² < 2}. This set is bounded above (by 2, for instance), but its least upper bound would be √2, which is not in ℚ.

<details class="math-explainer">
<summary>Explain the set-builder notation here</summary>
<p><strong>Read the whole expression:</strong> S is the set of rational numbers x whose square is less than two.</p>
<dl><dt>∈, &#x27;is an element of&#x27;</dt><dd>x must be rational in this example.</dd>
<dt>:, &#x27;such that&#x27;</dt><dd>Introduces the condition an element must satisfy.</dd>
<dt>x², &#x27;x squared&#x27;</dt><dd>x multiplied by itself.</dd>
<dt>&lt;, &#x27;is less than&#x27;</dt><dd>The square must be strictly below two.</dd></dl>
<p><strong>Example:</strong> The rational number 1 belongs to S because 1² &lt; 2. The rational number 2 does not.</p>
</details>

This axiom is the foundation of real analysis — we'll return to it rigorously in Module M7.

---

## Master's level — Proving a bound from definitions

**Prerequisite bridge.** A proof of an inequality has to cover every allowed input. The triangle inequality says the direct distance from one point to another cannot exceed the distance along a detour. Apply it to a = (a − b) + b:

\[|a|\le |a-b|+|b|.\]

Subtract |b|. Then swap a and b and repeat. The two results trap |a| − |b| between −|a − b| and |a − b|, proving the **reverse triangle inequality**:

\[\bigl||a|-|b|\bigr|\le |a-b|.\]

This is a model proof technique: rewrite the quantity you need to bound, use a known theorem, and state why the two-sided bound implies an absolute-value bound. Problem 7 below works through every step.

<details class="math-explainer">
<summary>Explain the reverse triangle inequality</summary>
<p><strong>Read the whole expression:</strong> The distance between the sizes of a and b is no greater than the distance between a and b.</p>
<dl><dt>|a − b|</dt><dd>Distance between a and b on the number line.</dd>
<dt>||a| − |b||</dt><dd>Distance between the nonnegative sizes |a| and |b|.</dd>
<dt>≤, &#x27;is at most&#x27;</dt><dd>Allows equality as well as a smaller left side.</dd></dl>
<p><strong>Example:</strong> For a = 7 and b = −2, the left side is |7 − 2| = 5 and the right side is |7 − (−2)| = 9.</p>
</details>

## PhD-level connection — Completeness and fixed points

**Prerequisite bridge.** A sequence x₀, x₁, ... is *Cauchy* when its later terms become arbitrarily close to one another. Completeness of the real numbers means every real Cauchy sequence has a real limit. That idea gives an existence-and-uniqueness theorem used throughout numerical analysis and differential equations; studying those applications fully still requires their own courses.

Let T map a closed interval [a,b] into itself and suppose some 0 ≤ q < 1 satisfies |T(x) − T(y)| ≤ q|x − y| for every x,y in the interval. Such a T is a **contraction**. Begin anywhere in [a,b] and repeatedly set xₙ₊₁ = T(xₙ). The first step has size d = |x₁ − x₀|. Each later step is at most q times the previous one, so |xₙ₊₁ − xₙ| ≤ qⁿd. For m > n, the triangle inequality and a geometric sum give

\[|x_m-x_n|\le d\sum_{k=n}^{m-1}q^k\le \frac{dq^n}{1-q}.\]

The last bound tends to zero, so the iterates are Cauchy and converge to some x* in [a,b]. The contraction inequality makes T continuous; taking limits in xₙ₊₁ = T(xₙ) gives T(x*) = x*. If u and v are fixed points, then |u − v| = |T(u) − T(v)| ≤ q|u − v|, forcing u = v. Thus the fixed point exists and is unique.

<details class="math-explainer">
<summary>Explain the contraction condition</summary>
<p><strong>Read the whole expression:</strong> The distance between two outputs of T is at most q times the distance between the corresponding inputs, with q smaller than one.</p>
<dl><dt>T</dt><dd>A rule that sends every point of the chosen interval back into that interval.</dd>
<dt>|T(x) − T(y)|</dt><dd>Distance between the two outputs.</dd>
<dt>q</dt><dd>A fixed shrinking factor between zero and one.</dd>
<dt>|x − y|</dt><dd>Distance between the inputs.</dd>
<dt>≤</dt><dd>The output distance may equal or fall below the bound.</dd></dl>
<p><strong>Example:</strong> For T(x) = (x + 2)/3 on [0,2], output distances are exactly one third of input distances; the unique fixed point is 1.</p>
</details>

## Practice Problems

**Basic:**

1. Classify each number as natural, integer, rational, or irrational (choose the most specific):
   - (a) -7
   - (b) 4/2
   - (c) √9
   - (d) √5
   - (e) 0.121212...

2. State which property justifies each step:
   - 3 + (x + 2) = 3 + (2 + x) = (3 + 2) + x = 5 + x

3. Solve: -3x + 7 > 1

**Intermediate:**

4. Solve and express in interval notation: |4 - 2x| < 6

5. Prove that the product of two rational numbers is rational.

6. Solve: |x - 3| + |x + 1| = 6

**Exam-Level:**

7. Prove: For all real a, b: |a - b| ≥ ||a| - |b||
   *(This is the reverse triangle inequality)*

8. Let S = {1 - 1/n : n ∈ ℕ}.
   - (a) List the first five elements of S.
   - (b) Is S bounded above? If so, what is sup(S)?
   - (c) Is sup(S) ∈ S?

---

**PhD-level practice, Problem 9.** For T(x) = (x + 2)/3 on [0,2], verify that T maps the interval into itself, find q, solve T(x) = x, and bound |xₙ − x*| after n iterations from any x₀ in [0,2].

## Solutions

---

### Problem 1: Number Classification

**Classify each number as natural, integer, rational, or irrational (choose the most specific):**

### (a) -7

**Solution:**

Let's check each category from most specific to least:
- Natural (ℕ)? No — naturals are positive: 1, 2, 3, ...
- Integer (ℤ)? **Yes** — integers include all whole numbers and their negatives
- Rational (ℚ)? Also yes — we can write -7 = -7/1
- Irrational? No — it's rational

**Most specific classification: Integer (ℤ)**

---

### (b) 4/2

**Solution:**

First, simplify: 4/2 = 2

Now classify 2:
- Natural (ℕ)? **Yes** — 2 is a counting number
- Integer (ℤ)? Also yes
- Rational (ℚ)? Also yes

**Most specific classification: Natural Number (ℕ)**

---

### (c) √9

**Solution:**

First, simplify: √9 = 3 (taking the principal/positive root)

Now classify 3:
- Natural (ℕ)? **Yes** — 3 is a counting number

**Most specific classification: Natural Number (ℕ)**

---

### (d) √5

**Solution:**

Can √5 be simplified to a nice number? Let's check if 5 is a perfect square: 1, 4, 9, 16, ... — no, 5 is not a perfect square.

Is √5 rational? Suppose √5 = p/q where p, q are integers with no common factors.

Then: 5 = p²/q², so p² = 5q²

This means p² is divisible by 5, so p is divisible by 5 (since 5 is prime).
Write p = 5k for some integer k.

Then: (5k)² = 5q² → 25k² = 5q² → 5k² = q²

So q² is divisible by 5, meaning q is divisible by 5.

But if both p and q are divisible by 5, they share a common factor — contradiction!

Therefore √5 is **irrational**.

**Most specific classification: Irrational (ℝ \ ℚ)**

---

### (e) 0.121212...

**Solution:**

This decimal repeats with period 2 (the block "12" repeats forever).

Any repeating decimal is rational. Let's prove it by finding the fraction:

Let x = 0.121212...

Multiply by 100 (since the repeating block has 2 digits):
100x = 12.121212...

Subtract the original:
100x - x = 12.121212... - 0.121212...
99x = 12
x = 12/99 = 4/33

**Verification:** 4 ÷ 33 = 0.121212... ✓

**Most specific classification: Rational (ℚ)**

(Note: It's not an integer because 4/33 doesn't simplify to a whole number)

---

### Problem 2: Identify Properties

**State which property justifies each step:**

3 + (x + 2) = 3 + (2 + x) = (3 + 2) + x = 5 + x

**Solution:**

**Step 1:** 3 + (x + 2) = 3 + (2 + x)

Inside the parentheses, we swapped x + 2 to 2 + x.

**Property: Commutative Property of Addition** (a + b = b + a)

---

**Step 2:** 3 + (2 + x) = (3 + 2) + x

We regrouped: instead of adding 3 to the quantity (2 + x), we add (3 + 2) to x.

**Property: Associative Property of Addition** ((a + b) + c = a + (b + c))

---

**Step 3:** (3 + 2) + x = 5 + x

We computed 3 + 2 = 5.

**Property: Substitution / Arithmetic** (not a named field property — just computation)

Some texts call this "closure" since 3 + 2 produces another real number, but more precisely it's just evaluation.

---

### Problem 3: Solve -3x + 7 > 1

**Solution:**

**Step 1:** Isolate the term with x

Subtract 7 from both sides:
-3x + 7 - 7 > 1 - 7
-3x > -6

**Step 2:** Solve for x

Divide both sides by -3.

⚠️ **Critical:** We're dividing by a negative number, so we must **reverse the inequality sign**.

-3x / (-3) < -6 / (-3)
x < 2

**Step 3:** Express the solution

**Solution: x < 2, or in interval notation: (-∞, 2)**

**Verification:** Let's test x = 0 (which should work) and x = 3 (which shouldn't):
- x = 0: -3(0) + 7 = 7 > 1 ✓
- x = 3: -3(3) + 7 = -9 + 7 = -2 > 1? No, -2 < 1 ✓ (correctly excluded)

---

### Problem 4: Solve |4 - 2x| < 6

**Solution:**

**Step 1:** Apply the absolute value inequality rule

For |expression| < k where k > 0, we have:
-k < expression < k

So: -6 < 4 - 2x < 6

**Step 2:** Solve the compound inequality

We need to isolate x in the middle. Work on all three parts simultaneously.

Subtract 4 from all parts:
-6 - 4 < 4 - 2x - 4 < 6 - 4
-10 < -2x < 2

**Step 3:** Divide by -2

⚠️ **Critical:** Dividing by negative reverses BOTH inequality signs.

-10 / (-2) > -2x / (-2) > 2 / (-2)
5 > x > -1

**Step 4:** Rewrite in standard order

5 > x > -1 is the same as -1 < x < 5

**Solution: -1 < x < 5, or in interval notation: (-1, 5)**

**Verification:**
- x = 0: |4 - 2(0)| = |4| = 4 < 6 ✓
- x = 2: |4 - 2(2)| = |0| = 0 < 6 ✓
- x = -1: |4 - 2(-1)| = |6| = 6 < 6? No, 6 is not less than 6 ✓ (boundary correctly excluded)
- x = 5: |4 - 2(5)| = |-6| = 6 < 6? No ✓ (boundary correctly excluded)

---

### Problem 5: Prove that the product of two rational numbers is rational

**Solution:**

**What we're proving:** If a ∈ ℚ and b ∈ ℚ, then a · b ∈ ℚ.

**Proof:**

Let a and b be rational numbers.

By definition of rational, there exist integers p, q, r, s with q ≠ 0 and s ≠ 0 such that:
- a = p/q
- b = r/s

Consider their product:
a · b = (p/q) · (r/s) = (p · r) / (q · s)

Now we verify this is rational:
- p · r is an integer (integers are closed under multiplication)
- q · s is an integer (integers are closed under multiplication)
- q · s ≠ 0 (since q ≠ 0 and s ≠ 0, and the product of nonzero numbers is nonzero)

Therefore a · b = (pr)/(qs) is a ratio of two integers with nonzero denominator.

**By definition, a · b is rational. ∎**

---

### Problem 6: Solve |x - 3| + |x + 1| = 6

**Solution:**

This problem has two absolute values with different expressions inside. We need to consider cases based on where each expression changes sign.

**Step 1:** Find critical points

|x - 3| changes sign at x = 3
|x + 1| changes sign at x = -1

These divide the number line into three regions: x < -1, -1 ≤ x < 3, and x ≥ 3

**Step 2:** Case 1 — x < -1

In this region:
- x - 3 < 0, so |x - 3| = -(x - 3) = -x + 3
- x + 1 < 0, so |x + 1| = -(x + 1) = -x - 1

The equation becomes:
(-x + 3) + (-x - 1) = 6
-2x + 2 = 6
-2x = 4
x = -2

**Check:** Is x = -2 in our region x < -1? Yes, -2 < -1 ✓

**Verify:** |(-2) - 3| + |(-2) + 1| = |-5| + |-1| = 5 + 1 = 6 ✓

**x = -2 is a solution.**

---

**Step 3:** Case 2 — -1 ≤ x < 3

In this region:
- x - 3 < 0, so |x - 3| = -(x - 3) = -x + 3
- x + 1 ≥ 0, so |x + 1| = x + 1

The equation becomes:
(-x + 3) + (x + 1) = 6
4 = 6

This is a contradiction! No solution exists in this region.

---

**Step 4:** Case 3 — x ≥ 3

In this region:
- x - 3 ≥ 0, so |x - 3| = x - 3
- x + 1 > 0, so |x + 1| = x + 1

The equation becomes:
(x - 3) + (x + 1) = 6
2x - 2 = 6
2x = 8
x = 4

**Check:** Is x = 4 in our region x ≥ 3? Yes, 4 ≥ 3 ✓

**Verify:** |4 - 3| + |4 + 1| = |1| + |5| = 1 + 5 = 6 ✓

**x = 4 is a solution.**

---

**Final Solution: x = -2 or x = 4**

**Geometric Interpretation:** |x - 3| is the distance from x to 3, and |x + 1| is the distance from x to -1. We're looking for points whose total distance to both -1 and 3 equals 6. The distance between -1 and 3 is 4. Any point between them has total distance exactly 4, so we need points outside the interval where the "extra" distance adds up to 2 (one unit on each side, giving us -2 and 4).

---

### Problem 7: Prove |a - b| ≥ ||a| - |b|| (Reverse Triangle Inequality)

**Solution:**

**What we're proving:** For all real numbers a and b, |a - b| ≥ ||a| - |b||

**Proof:**

We'll use the standard triangle inequality: |x + y| ≤ |x| + |y|

**Part 1:** Show |a| - |b| ≤ |a - b|

Write a = (a - b) + b

Apply the triangle inequality:
|a| = |(a - b) + b| ≤ |a - b| + |b|

Subtract |b| from both sides:
|a| - |b| ≤ |a - b| ... (Inequality 1)

**Part 2:** Show |b| - |a| ≤ |a - b|

By symmetry (swap a and b in the argument above):
|b| - |a| ≤ |b - a|

But |b - a| = |-(a - b)| = |a - b|, so:
|b| - |a| ≤ |a - b|

Multiply both sides by -1 (this reverses the inequality):
|a| - |b| ≥ -|a - b| ... (Inequality 2)

**Part 3:** Combine the inequalities

From Inequality 1: |a| - |b| ≤ |a - b|
From Inequality 2: |a| - |b| ≥ -|a - b|

Together: -|a - b| ≤ |a| - |b| ≤ |a - b|

By the definition of absolute value (|x| ≤ k iff -k ≤ x ≤ k), this means:
||a| - |b|| ≤ |a - b|

Equivalently: **|a - b| ≥ ||a| - |b|| ∎**

---

**Example to illustrate:** Let a = 7, b = 2

- |a - b| = |7 - 2| = 5
- ||a| - |b|| = ||7| - |2|| = |7 - 2| = 5

So |a - b| = ||a| - |b|| = 5. (Equality holds when a and b have the same sign.)

Now let a = 7, b = -2:
- |a - b| = |7 - (-2)| = |9| = 9
- ||a| - |b|| = ||7| - |-2|| = |7 - 2| = 5

So 9 ≥ 5 ✓ (Strict inequality when a and b have opposite signs.)

---

### Problem 8: Supremum Problem

**Let S = {1 - 1/n : n ∈ ℕ}**

### (a) List the first five elements of S

**Solution:**

Substitute n = 1, 2, 3, 4, 5:

- n = 1: 1 - 1/1 = 1 - 1 = 0
- n = 2: 1 - 1/2 = 1/2 = 0.5
- n = 3: 1 - 1/3 ≈ 0.667
- n = 4: 1 - 1/4 = 3/4 = 0.75
- n = 5: 1 - 1/5 = 4/5 = 0.8

**First five elements: {0, 1/2, 2/3, 3/4, 4/5}**

Or equivalently: **{0, 0.5, 0.667..., 0.75, 0.8}**

---

### (b) Is S bounded above? If so, what is sup(S)?

**Solution:**

**Is S bounded above?**

Observe the pattern: as n increases, 1/n decreases, so 1 - 1/n increases.

For all n ∈ ℕ:
- 1/n > 0 (since n ≥ 1)
- Therefore 1 - 1/n < 1

So every element of S is less than 1. **S is bounded above by 1.**

**What is sup(S)?**

We claim sup(S) = 1. To prove this, we need to show:
1. 1 is an upper bound of S
2. No number less than 1 is an upper bound of S

**Part 1:** We showed above that 1 - 1/n < 1 for all n ∈ ℕ, so 1 is an upper bound. ✓

**Part 2:** Let M < 1. We need to find an element of S that exceeds M.

We want: 1 - 1/n > M
Rearranging: 1 - M > 1/n
So: n > 1/(1 - M)

Since 1 - M > 0 (because M < 1), the value 1/(1 - M) is a positive real number.

By the Archimedean property, there exists a natural number n > 1/(1 - M).

For this n: 1 - 1/n > M

So M is not an upper bound of S. ✓

**Therefore, sup(S) = 1.**

---

### (c) Is sup(S) ∈ S?

**Solution:**

Is 1 ∈ S?

For 1 to be in S, we'd need: 1 - 1/n = 1 for some n ∈ ℕ

This would require: 1/n = 0

But 1/n > 0 for all n ∈ ℕ, so there is no natural number n that gives 1 - 1/n = 1.

**No, sup(S) = 1 is NOT an element of S.**

---

**This is a key example!** The set S gets arbitrarily close to 1 but never reaches it. This illustrates:
- The difference between maximum (largest element in the set) and supremum (least upper bound)
- S has no maximum, but it does have a supremum
- The supremum of a set need not belong to the set

This concept is fundamental to real analysis — limits, continuity, and the completeness axiom all build on understanding suprema.

---

### Problem 9: A contraction on an interval

For 0 ≤ x ≤ 2, 2/3 ≤ T(x) ≤ 4/3, so T([0,2]) lies inside [0,2]. Also |T(x) − T(y)| = |x − y|/3, so q = 1/3. Solving (x + 2)/3 = x gives x* = 1. Since each iteration shrinks the distance from the fixed point by exactly one third,

\[|x_n-1|=3^{-n}|x_0-1|.\]

This is an exact equality for this affine T, stronger than a general contraction bound.

### Summary of Key Techniques

| Problem Type | Strategy |
|--------------|----------|
| Number classification | Simplify first, then check categories from most to least specific |
| Inequality with negative coefficient | Flip the sign when multiplying/dividing by negative |
| Absolute value inequality | Convert to compound inequality, mind the sign reversal |
| Multiple absolute values | Use case analysis based on critical points |
| Prove closure property | Start from definitions, show result fits the definition |
| Reverse triangle inequality | Clever use of forward triangle inequality |
| Supremum problems | Show it's an upper bound AND nothing smaller works |

---

Ready for Lesson M1.2 (Algebraic Manipulation and Factoring) when you are!
## Summary

**Key Takeaways:**
- ℝ contains all rationals and irrationals; it has no "gaps"
- The field properties justify all algebraic manipulation
- Multiplying/dividing inequalities by negatives reverses the sign
- Absolute value measures distance; the triangle inequality is fundamental
- Interval notation: parentheses exclude endpoints, brackets include them
- Completeness distinguishes ℝ from ℚ — every nonempty set bounded above has a real supremum

**Common Mistakes:**
- Forgetting to flip inequality when multiplying by negative
- Using brackets with infinity: [3, ∞] is wrong; use [3, ∞)
- Thinking |a + b| = |a| + |b| (only true when a, b have same sign or one is zero)

**What's Next:** Lesson M1.2 covers Algebraic Manipulation and Factoring — rebuilding fluency with polynomials, fractions, and expressions.

---
