# Lesson M1.2: Algebraic Manipulation and Factoring

---

**Prerequisites:** Lesson M1.1 — Real Numbers, Properties, and Order

**Learning Objectives:**
- Perform polynomial arithmetic fluently (addition, subtraction, multiplication, division)
- Apply all standard factoring techniques systematically
- Simplify rational expressions and complex fractions
- Rationalize denominators (including conjugates)
- Recognize algebraic structures that appear in calculus and analysis

---

## High-school level — Expressions and factoring

An expression names a value; an equation asserts two values are equal. In this section, every manipulation is reversible algebra unless a denominator is zero. Work each example before looking at the next line, then check by expanding or substitution.

## 1. Polynomial Arithmetic

A **polynomial** in variable x is an expression of the form:

$$p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$$

Here $n$ is a positive integer, the coefficients $a_0, a_1, \ldots, a_n$ are real, and the **degree** is $n$ when $a_n\neq0$. A nonzero constant $p(x)=a_0$ is also a polynomial, of degree zero. The zero polynomial's degree is usually left undefined.

### 1.1 Addition and Subtraction

**Rule:** Combine like terms (same power of x).

**Example:** $(3x^3 - 2x + 5) + (x^3 + 4x^2 - 7)$

Group by degree:
- $x^3$ terms: $3x^3 + x^3 = 4x^3$
- $x^2$ terms: $0 + 4x^2 = 4x^2$
- $x$ terms: $-2x + 0 = -2x$
- Constants: $5 + (-7) = -2$

**Result:** $4x^3 + 4x^2 - 2x - 2$

<details class="math-explainer">
<summary>Explain polynomial powers and coefficients</summary>
<p><strong>Read the whole expression:</strong> Four x cubed plus four x squared minus two x minus two.</p>
<dl><dt>x³, &#x27;x cubed&#x27;</dt><dd>x multiplied by itself three times.</dd>
<dt>4, coefficient</dt><dd>The multiplier of x³ or x² in this expression.</dd>
<dt>−, minus</dt><dd>Subtract the following term.</dd>
<dt>like terms</dt><dd>Terms with the same power of x; only these can be combined directly.</dd></dl>
<p><strong>Example:</strong> At x = 2, 4x³ is 4 times 8, or 32; 4x² is 4 times 4, or 16.</p>
</details>

### 1.2 Multiplication

**Rule:** Use the distributive property (every term times every term), then combine like terms.

**Example:** $(2x - 3)(x^2 + 4x - 1)$

Distribute each term from the first factor:
- $2x \cdot (x^2 + 4x - 1) = 2x^3 + 8x^2 - 2x$
- $-3 \cdot (x^2 + 4x - 1) = -3x^2 - 12x + 3$

Combine: $2x^3 + 8x^2 - 3x^2 - 2x - 12x + 3 = 2x^3 + 5x^2 - 14x + 3$

### 1.3 Special Products

Memorize these — they appear constantly:

| Pattern | Formula |
|---------|---------|
| **Square of a sum** | $(a + b)^2 = a^2 + 2ab + b^2$ |
| **Square of a difference** | $(a - b)^2 = a^2 - 2ab + b^2$ |
| **Difference of squares** | $(a + b)(a - b) = a^2 - b^2$ |
| **Cube of a sum** | $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ |
| **Cube of a difference** | $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$ |

**Example:** Expand $(x + 2)^3$

Using the formula with $a = x$, $b = 2$:
$(x + 2)^3 = x^3 + 3(x^2)(2) + 3(x)(4) + 8 = x^3 + 6x^2 + 12x + 8$

### 1.4 Polynomial Division

**Long Division:** Used when dividing by polynomials of degree ≥ 2 or when you need both quotient and remainder.

**Example:** Divide $x^3 - 2x^2 + 4$ by $x - 2$.

Write the missing coefficient as $0x$. The leading term $x^3$ divided by the leading term $x$ gives $x^2$. Multiply back: $x^2(x-2)=x^3-2x^2$. Subtracting this product from $x^3-2x^2+0x+4$ leaves the constant $4$. Its degree is less than the divisor's degree, so division stops:

$$x^3-2x^2+4=(x-2)x^2+4.$$

The quotient is $x^2$ and the remainder is $4$. Multiplying the divisor by the quotient and adding the remainder checks the result.

**Synthetic Division:** A shortcut when dividing by $(x - c)$.

**Example:** Divide $x^3 - 2x^2 + 4$ by $x - 2$ using synthetic division:

```
2 │  1   -2    0    4
  │       2    0    0
  ─────────────────────
     1    0    0    4
```

Quotient: $x^2 + 0x + 0 = x^2$, Remainder: $4$

So: $\frac{x^3 - 2x^2 + 4}{x - 2} = x^2 + \frac{4}{x-2}$

---

## 2. Factoring Techniques

Factoring is the reverse of multiplication — expressing a polynomial as a product of simpler polynomials. This skill is essential for simplifying expressions, solving equations, and computing limits.

### 2.1 Strategy: Always Start with GCF

**Greatest Common Factor (GCF):** Factor out the largest expression that divides every term.

**Example:** Factor $6x^4 - 9x^3 + 15x^2$

GCF of coefficients: $\gcd(6, 9, 15) = 3$  
GCF of variables: $x^2$ (lowest power)

Factor: $3x^2(2x^2 - 3x + 5)$

### 2.2 Factoring by Grouping

**When to use:** Four or more terms that can be grouped into pairs with common factors.

**Example:** Factor $x^3 + 2x^2 - 3x - 6$

Group: $(x^3 + 2x^2) + (-3x - 6)$

Factor each group: $x^2(x + 2) - 3(x + 2)$

Factor out $(x + 2)$: $(x + 2)(x^2 - 3)$

### 2.3 Factoring Trinomials: $ax^2 + bx + c$

**Case 1: $a = 1$ (Monic trinomials)**

Find two numbers that multiply to $c$ and add to $b$.

**Example:** Factor $x^2 + 5x + 6$

Need: product = 6, sum = 5  
Numbers: 2 and 3

Factor: $(x + 2)(x + 3)$

**Case 2: $a \neq 1$ (Non-monic trinomials)**

**AC Method:** Find two numbers that multiply to $ac$ and add to $b$, then factor by grouping.

**Example:** Factor $6x^2 + 11x - 10$

Here $a = 6$, $b = 11$, $c = -10$, so $ac = -60$

Need: product = -60, sum = 11  
Numbers: 15 and -4 (since $15 \times (-4) = -60$ and $15 + (-4) = 11$)

Rewrite middle term: $6x^2 + 15x - 4x - 10$

Group: $(6x^2 + 15x) + (-4x - 10)$

Factor: $3x(2x + 5) - 2(2x + 5)$

Result: $(2x + 5)(3x - 2)$

### 2.4 Special Factoring Patterns

| Pattern | Formula |
|---------|---------|
| **Difference of squares** | $a^2 - b^2 = (a + b)(a - b)$ |
| **Perfect square trinomial** | $a^2 + 2ab + b^2 = (a + b)^2$ |
| **Perfect square trinomial** | $a^2 - 2ab + b^2 = (a - b)^2$ |
| **Sum of cubes** | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ |
| **Difference of cubes** | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ |

⚠️ **Critical:** There is NO "sum of squares" factorization over the reals: $a^2 + b^2$ cannot be factored with real coefficients.

**Example:** Factor $x^3 - 8$

Recognize: $8 = 2^3$, so this is a difference of cubes.

Apply formula with $a = x$, $b = 2$:
$x^3 - 8 = (x - 2)(x^2 + 2x + 4)$

**Verification:** $(x - 2)(x^2 + 2x + 4) = x^3 + 2x^2 + 4x - 2x^2 - 4x - 8 = x^3 - 8$ ✓

**Example:** Factor $x^4 - 16$

This is a difference of squares: $x^4 - 16 = (x^2)^2 - 4^2 = (x^2 + 4)(x^2 - 4)$

But $x^2 - 4$ factors further: $x^2 - 4 = (x + 2)(x - 2)$

**Final:** $x^4 - 16 = (x^2 + 4)(x + 2)(x - 2)$

Note: $x^2 + 4$ doesn't factor over ℝ.

### 2.5 Substitution for Complex Expressions

Sometimes an expression has a repeated structure. Substitute to reveal a simpler pattern.

**Example:** Factor $x^4 - 5x^2 + 4$

Let $u = x^2$. Then: $u^2 - 5u + 4$

Factor: $(u - 4)(u - 1)$

Substitute back: $(x^2 - 4)(x^2 - 1)$

Factor further: $(x + 2)(x - 2)(x + 1)(x - 1)$

---

## Undergraduate level — Domains and rational identities

Cancellation is an identity only on the common domain of the original expressions. A cancelled factor does not restore an excluded input. This is the bridge from manipulation of symbols to reasoning about functions.

## 3. Rational Expressions

A **rational expression** is a ratio of two polynomials: $\frac{P(x)}{Q(x)}$ where $Q(x) \neq 0$.

<details class="math-explainer">
<summary>Explain a rational expression and its restriction</summary>
<p><strong>Read the whole expression:</strong> P of x divided by Q of x, provided Q of x is not zero.</p>
<dl><dt>P(x), numerator</dt><dd>A polynomial supplying the top value.</dd>
<dt>Q(x), denominator</dt><dd>A polynomial supplying the bottom value.</dd>
<dt>≠, &#x27;is not equal to&#x27;</dt><dd>Excludes inputs where division would be undefined.</dd>
<dt>x</dt><dd>The input to both polynomials in this expression.</dd></dl>
<p><strong>Example:</strong> For (x+3)/(x−2), the input x=2 is excluded even if later algebra seems to cancel a factor.</p>
</details>

### 3.1 Domain Restrictions

The expression is undefined wherever the denominator equals zero.

**Example:** Find the domain of $\frac{x + 3}{x^2 - 4}$

Set denominator = 0: $x^2 - 4 = 0 \Rightarrow x = \pm 2$

**Domain:** All real numbers except $x = 2$ and $x = -2$, or $\mathbb{R} \setminus \{-2, 2\}$

### 3.2 Simplifying Rational Expressions

**Step 1:** Factor numerator and denominator completely.  
**Step 2:** Cancel common factors.

**Example:** Simplify $\frac{x^2 - 9}{x^2 + 5x + 6}$

Factor numerator: $x^2 - 9 = (x + 3)(x - 3)$

Factor denominator: $x^2 + 5x + 6 = (x + 2)(x + 3)$

Cancel $(x + 3)$: $\frac{(x + 3)(x - 3)}{(x + 2)(x + 3)} = \frac{x - 3}{x + 2}$, valid for $x \neq -3, -2$

### 3.3 Operations with Rational Expressions

**Multiplication:** $\frac{A}{B} \cdot \frac{C}{D} = \frac{AC}{BD}$ (factor and cancel first)

**Division:** $\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \cdot \frac{D}{C}$

**Addition/Subtraction:** Find LCD, convert, then combine numerators.

**Example:** Simplify $\frac{2}{x - 1} + \frac{3}{x + 2}$

LCD: $(x - 1)(x + 2)$

Convert: $\frac{2(x + 2)}{(x-1)(x+2)} + \frac{3(x - 1)}{(x-1)(x+2)}$

Combine: $\frac{2(x + 2) + 3(x - 1)}{(x-1)(x+2)} = \frac{2x + 4 + 3x - 3}{(x-1)(x+2)} = \frac{5x + 1}{(x-1)(x+2)}$

### 3.4 Complex Fractions

A **complex fraction** has fractions in its numerator, denominator, or both.

**Method 1:** Simplify numerator and denominator separately, then divide.

**Method 2:** Multiply numerator and denominator by the LCD of all inner fractions.

**Example:** Simplify $\frac{\frac{1}{x} - \frac{1}{y}}{\frac{1}{x} + \frac{1}{y}}$

**Using Method 2:** The LCD of all inner fractions is $xy$.

Multiply top and bottom by $xy$:

$$\frac{xy \cdot \left(\frac{1}{x} - \frac{1}{y}\right)}{xy \cdot \left(\frac{1}{x} + \frac{1}{y}\right)} = \frac{y - x}{y + x}$$

---

## 4. Rationalizing

**Rationalizing** eliminates radicals from a denominator (or sometimes numerator, especially in calculus).

### 4.1 Rationalizing with Single Terms

Multiply by $\frac{\sqrt{a}}{\sqrt{a}}$ to eliminate $\sqrt{a}$ from the denominator.

**Example:** Rationalize $\frac{5}{\sqrt{3}}$

$$\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}$$

### 4.2 Rationalizing with Conjugates

For expressions like $a + \sqrt{b}$ or $\sqrt{a} + \sqrt{b}$, multiply by the **conjugate**.

**Conjugate pairs:** $(a + \sqrt{b})(a - \sqrt{b}) = a^2 - b$

**Example:** Rationalize $\frac{2}{3 + \sqrt{5}}$

Multiply by the conjugate:

$$\frac{2}{3 + \sqrt{5}} \cdot \frac{3 - \sqrt{5}}{3 - \sqrt{5}} = \frac{2(3 - \sqrt{5})}{9 - 5} = \frac{2(3 - \sqrt{5})}{4} = \frac{3 - \sqrt{5}}{2}$$

### 4.3 Rationalizing the Numerator (Calculus Application)

In calculus, we often rationalize the numerator to evaluate limits.

**Example:** Simplify $\frac{\sqrt{x+h} - \sqrt{x}}{h}$ by rationalizing the numerator.

Multiply by the conjugate of the numerator:

$$\frac{\sqrt{x+h} - \sqrt{x}}{h} \cdot \frac{\sqrt{x+h} + \sqrt{x}}{\sqrt{x+h} + \sqrt{x}}$$

$$= \frac{(x+h) - x}{h(\sqrt{x+h} + \sqrt{x})} = \frac{h}{h(\sqrt{x+h} + \sqrt{x})} = \frac{1}{\sqrt{x+h} + \sqrt{x}}$$

This form allows us to evaluate the limit as $h \to 0$.

---

## Master's level — The division theorem and proof habits

**Prerequisite bridge.** The *degree* of a nonzero polynomial is its highest exponent with nonzero coefficient. For real polynomials P and D with D not the zero polynomial, long division gives a quotient Q and remainder R such that

\[P=DQ+R,\qquad R=0\ \text{or}\ \deg R<\deg D.\]

Why are Q and R unique? Suppose P = DQ₁ + R₁ = DQ₂ + R₂ with both remainders smaller than D. Then D(Q₁ − Q₂) = R₂ − R₁. If Q₁ − Q₂ were nonzero, the left side would have degree at least deg D, while the right side would have degree below deg D. That is impossible. Thus Q₁ = Q₂ and R₁ = R₂. Existence comes from repeatedly cancelling the leading term, lowering the degree each time.

<details class="math-explainer">
<summary>Explain quotient and remainder notation</summary>
<p><strong>Read the whole expression:</strong> P equals D times Q plus R, where R is zero or has smaller degree than D.</p>
<dl><dt>P</dt><dd>Polynomial being divided.</dd>
<dt>D</dt><dd>Nonzero divisor polynomial.</dd>
<dt>Q</dt><dd>Quotient polynomial.</dd>
<dt>R</dt><dd>Remainder polynomial.</dd>
<dt>deg, &#x27;degree&#x27;</dt><dd>Highest exponent with nonzero coefficient.</dd>
<dt>&lt;</dt><dd>The remainder&#x27;s degree is strictly smaller.</dd></dl>
<p><strong>Example:</strong> x³−2x²+4 = (x−2)x²+4: P is the cubic, D is x−2, Q is x², and R is 4.</p>
</details>

## 5. Algebraic Structures in Analysis

These manipulations appear repeatedly in qualifying exams:

### 5.1 Difference Quotients

The derivative definition uses: $\frac{f(x+h) - f(x)}{h}$

This requires algebraic simplification before taking the limit.

### 5.2 Partial Fractions (Preview)

Used for integration and Laplace transforms. We decompose:

$$\frac{2x + 3}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}$$

To find $A$ and $B$: multiply both sides by $(x-1)(x+2)$:

$2x + 3 = A(x+2) + B(x-1)$

Set $x = 1$: $5 = 3A \Rightarrow A = 5/3$

Set $x = -2$: $-1 = -3B \Rightarrow B = 1/3$

### 5.3 Completing the Square

Essential for quadratics, integration, and optimization.

**Template:** $ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)$

**Example:** Complete the square for $x^2 + 6x + 2$

Half of 6 is 3; square it: $3^2 = 9$

$x^2 + 6x + 2 = (x^2 + 6x + 9) - 9 + 2 = (x + 3)^2 - 7$

---

## PhD-level connection — Algebra and numerical sensitivity

**Prerequisite bridge.** Error analysis asks how much an output can move when its input moves. The factorization in Problem 9 is useful beyond finding roots. For an integer n ≥ 1 and real x,y,

\[x^n-y^n=(x-y)\sum_{k=0}^{n-1}x^{n-1-k}y^k.\]

If |x|,|y| ≤ M for some M>0, each of the n terms in the sum has absolute value at most Mⁿ⁻¹. The triangle inequality therefore gives

\[|x^n-y^n|\le nM^{n-1}|x-y|.\]

This is a finite-error bound with stated assumptions, not just an infinitesimal approximation. For nonzero x, the *local relative condition number* of F(x)=xⁿ is |xF′(x)/F(x)|=n: a small relative input error is amplified by about n in the output. Condition number describes the mathematical problem; it does not by itself certify that a particular algorithm is stable.

<details class="math-explainer">
<summary>Explain the power-map error bound</summary>
<p><strong>Read the whole expression:</strong> The difference between x to the nth power and y to the nth power is at most n times M to the n minus one times the distance between x and y.</p>
<dl><dt>| |, absolute value</dt><dd>Measures size or distance without sign.</dd>
<dt>n</dt><dd>A positive whole-number exponent.</dd>
<dt>M</dt><dd>A shared upper bound for the sizes of x and y.</dd>
<dt>≤</dt><dd>An upper bound, including equality.</dd>
<dt>x−y</dt><dd>The input perturbation whose effect we measure.</dd></dl>
<p><strong>Example:</strong> For n=2 and |x|,|y|≤3, the output difference is at most 6|x−y|.</p>
</details>

## Practice Problems

### Basic

**Problem 1.** Expand and simplify: $(3x - 2)^2 - (x + 4)(x - 4)$

**Problem 2.** Factor completely: $x^3 - 4x^2 - x + 4$

**Problem 3.** Simplify: $\frac{x^2 - 4x + 3}{x^2 - 1}$

### Intermediate

**Problem 4.** Simplify the complex fraction:
$$\frac{\frac{1}{x+h} - \frac{1}{x}}{h}$$

**Problem 5.** Factor completely: $x^6 - 1$

*Hint: First use difference of squares, then factor the resulting cubics.*

**Problem 6.** Rationalize the numerator and simplify:
$$\frac{\sqrt{x} - \sqrt{a}}{x - a}$$

### Exam-Level

**Problem 7.** (Real Analysis Connection)

Let $f(x) = \frac{1}{x^2}$. Use the definition of the derivative to find $f'(x)$.

That is, compute:
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Show all algebraic simplification steps before taking the limit.

**Problem 8.** (Linear Algebra Connection)

The characteristic polynomial of a $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is:

$$p(\lambda) = \lambda^2 - (a+d)\lambda + (ad - bc)$$

(a) For $A = \begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$, find and factor the characteristic polynomial.

(b) Verify that the eigenvalues satisfy $\lambda_1 + \lambda_2 = \text{tr}(A)$ and $\lambda_1 \lambda_2 = \det(A)$.

**Problem 9.** (Numerical Analysis Connection)

In error analysis, we often need to bound expressions. Prove the following algebraic identity and then explain its use:

$$a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + a^{n-3}b^2 + \cdots + ab^{n-2} + b^{n-1})$$

*Hint: Verify by expanding the right side, or use the geometric series formula.*

**Problem 10.** (Mock Qual Problem)

Simplify the following expression completely:

$$\frac{x^4 - 16}{x^3 + 8} \cdot \frac{x^2 - 2x + 4}{x^2 + 4} \div \frac{x - 2}{x + 2}$$

---

**PhD-level practice, Problem 11.** Let F(x)=x⁵ and suppose |x|,|y|≤2. Prove |F(x)−F(y)|≤80|x−y|. Then find the local relative condition number for x≠0 and explain what each statement does and does not say.

## Solutions

### Problem 1

**Expand and simplify: $(3x - 2)^2 - (x + 4)(x - 4)$**

**Step 1:** Expand $(3x - 2)^2$ using the square of a difference:
$(3x - 2)^2 = (3x)^2 - 2(3x)(2) + 2^2 = 9x^2 - 12x + 4$

**Step 2:** Expand $(x + 4)(x - 4)$ using difference of squares:
$(x + 4)(x - 4) = x^2 - 16$

**Step 3:** Subtract:
$(9x^2 - 12x + 4) - (x^2 - 16) = 9x^2 - 12x + 4 - x^2 + 16 = 8x^2 - 12x + 20$

**Step 4:** Factor out GCF:
$8x^2 - 12x + 20 = 4(2x^2 - 3x + 5)$

**Answer:** $4(2x^2 - 3x + 5)$

---

### Problem 2

**Factor completely: $x^3 - 4x^2 - x + 4$**

**Step 1:** Try grouping:
$(x^3 - 4x^2) + (-x + 4)$

**Step 2:** Factor each group:
$x^2(x - 4) - 1(x - 4)$

**Step 3:** Factor out $(x - 4)$:
$(x - 4)(x^2 - 1)$

**Step 4:** Factor $x^2 - 1$ as difference of squares:
$(x - 4)(x + 1)(x - 1)$

**Answer:** $(x - 4)(x + 1)(x - 1)$

**Verification:** Multiply out: $(x-4)(x+1) = x^2 - 3x - 4$, then $(x^2 - 3x - 4)(x - 1) = x^3 - x^2 - 3x^2 + 3x - 4x + 4 = x^3 - 4x^2 - x + 4$ ✓

---

### Problem 3

**Simplify: $\frac{x^2 - 4x + 3}{x^2 - 1}$**

**Step 1:** Factor numerator.
$x^2 - 4x + 3$: Need two numbers with product 3 and sum -4. Numbers: -3 and -1.
$x^2 - 4x + 3 = (x - 3)(x - 1)$

**Step 2:** Factor denominator.
$x^2 - 1 = (x + 1)(x - 1)$

**Step 3:** Cancel common factors.
$$\frac{(x - 3)(x - 1)}{(x + 1)(x - 1)} = \frac{x - 3}{x + 1}$$

**Answer:** $\frac{x - 3}{x + 1}$, for $x \neq 1, -1$

---

### Problem 4

**Simplify the complex fraction: $\frac{\frac{1}{x+h} - \frac{1}{x}}{h}$**

**Step 1:** Find common denominator for the numerator.
LCD of $\frac{1}{x+h}$ and $\frac{1}{x}$ is $x(x+h)$.

$$\frac{1}{x+h} - \frac{1}{x} = \frac{x}{x(x+h)} - \frac{x+h}{x(x+h)} = \frac{x - (x+h)}{x(x+h)} = \frac{-h}{x(x+h)}$$

**Step 2:** Divide by $h$.
$$\frac{\frac{-h}{x(x+h)}}{h} = \frac{-h}{x(x+h)} \cdot \frac{1}{h} = \frac{-1}{x(x+h)}$$

**Answer:** $\frac{-1}{x(x+h)}$

**Note:** This is the difference quotient for $f(x) = \frac{1}{x}$. Taking $h \to 0$ gives $f'(x) = \frac{-1}{x^2}$.

---

### Problem 5

**Factor completely: $x^6 - 1$**

**Step 1:** Use difference of squares.
$x^6 - 1 = (x^3)^2 - 1^2 = (x^3 + 1)(x^3 - 1)$

**Step 2:** Factor each cubic.

$x^3 + 1$ is a sum of cubes: $x^3 + 1 = (x + 1)(x^2 - x + 1)$

$x^3 - 1$ is a difference of cubes: $x^3 - 1 = (x - 1)(x^2 + x + 1)$

**Step 3:** Combine.
$$x^6 - 1 = (x + 1)(x^2 - x + 1)(x - 1)(x^2 + x + 1)$$

**Step 4:** Check if quadratic factors can be factored further.

For $x^2 - x + 1$: Discriminant = $1 - 4 = -3 < 0$. No real roots; doesn't factor over ℝ.

For $x^2 + x + 1$: Discriminant = $1 - 4 = -3 < 0$. No real roots; doesn't factor over ℝ.

**Answer:** $(x - 1)(x + 1)(x^2 - x + 1)(x^2 + x + 1)$

---

### Problem 6

**Rationalize the numerator and simplify: $\frac{\sqrt{x} - \sqrt{a}}{x - a}$**

**Step 1:** Multiply by the conjugate of the numerator.
$$\frac{\sqrt{x} - \sqrt{a}}{x - a} \cdot \frac{\sqrt{x} + \sqrt{a}}{\sqrt{x} + \sqrt{a}}$$

**Step 2:** Simplify the numerator using difference of squares.
$$(\sqrt{x})^2 - (\sqrt{a})^2 = x - a$$

**Step 3:** Write the result.
$$\frac{x - a}{(x - a)(\sqrt{x} + \sqrt{a})}$$

**Step 4:** Cancel $(x - a)$.
$$\frac{1}{\sqrt{x} + \sqrt{a}}$$

**Answer:** $\frac{1}{\sqrt{x} + \sqrt{a}}$, for $x \neq a$

**Note:** This is the simplified form of $\frac{f(x) - f(a)}{x - a}$ where $f(x) = \sqrt{x}$. For $a>0$, taking $x \to a$ gives $f'(a) = \frac{1}{2\sqrt{a}}$; at $a=0$ this finite derivative formula does not apply.

---

### Problem 7 (Exam-Level)

**Find $f'(x)$ for $f(x) = \frac{1}{x^2}$ using the limit definition.**

**Step 1:** Write the difference quotient.
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} = \lim_{h \to 0} \frac{\frac{1}{(x+h)^2} - \frac{1}{x^2}}{h}$$

**Step 2:** Find common denominator in the numerator.
$$\frac{1}{(x+h)^2} - \frac{1}{x^2} = \frac{x^2 - (x+h)^2}{x^2(x+h)^2}$$

**Step 3:** Expand $(x+h)^2$ and simplify the numerator.
$$x^2 - (x+h)^2 = x^2 - (x^2 + 2xh + h^2) = -2xh - h^2 = -h(2x + h)$$

**Step 4:** Substitute back.
$$\frac{\frac{-h(2x + h)}{x^2(x+h)^2}}{h} = \frac{-h(2x + h)}{h \cdot x^2(x+h)^2} = \frac{-(2x + h)}{x^2(x+h)^2}$$

**Step 5:** Take the limit as $h \to 0$.
$$f'(x) = \lim_{h \to 0} \frac{-(2x + h)}{x^2(x+h)^2} = \frac{-(2x + 0)}{x^2 \cdot x^2} = \frac{-2x}{x^4} = \frac{-2}{x^3}$$

**Answer:** $f'(x) = -\frac{2}{x^3}$

---

### Problem 8 (Exam-Level)

**Part (a):** Find and factor the characteristic polynomial for $A = \begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$.

Using the formula $p(\lambda) = \lambda^2 - (a+d)\lambda + (ad - bc)$:

- Trace: $a + d = 5 + 4 = 9$
- Determinant: $ad - bc = 5(4) - 2(3) = 20 - 6 = 14$

$$p(\lambda) = \lambda^2 - 9\lambda + 14$$

Factor: Need two numbers with product 14 and sum 9. Numbers: 7 and 2.

$$p(\lambda) = (\lambda - 7)(\lambda - 2)$$

**Eigenvalues:** $\lambda_1 = 7$, $\lambda_2 = 2$

**Part (b):** Verify the relationships.

$\lambda_1 + \lambda_2 = 7 + 2 = 9 = \text{tr}(A)$ ✓

$\lambda_1 \cdot \lambda_2 = 7 \cdot 2 = 14 = \det(A)$ ✓

**Note:** This relationship (Vieta's formulas for the characteristic polynomial) holds for all $n \times n$ matrices: the sum of eigenvalues equals the trace, and the product equals the determinant.

---

### Problem 9 (Exam-Level)

**Prove: $a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + a^{n-3}b^2 + \cdots + ab^{n-2} + b^{n-1})$**

**Proof by expansion:**

Let $S = a^{n-1} + a^{n-2}b + a^{n-3}b^2 + \cdots + ab^{n-2} + b^{n-1}$

When $a\ne0$ this may be viewed as a geometric series with ratio $b/a$; the expansion proof below also works when $a=0$.

Compute $(a - b) \cdot S$:

$$a \cdot S = a^n + a^{n-1}b + a^{n-2}b^2 + \cdots + a^2b^{n-2} + ab^{n-1}$$

$$b \cdot S = a^{n-1}b + a^{n-2}b^2 + a^{n-3}b^3 + \cdots + ab^{n-1} + b^n$$

Subtract:
$$a \cdot S - b \cdot S = a^n - b^n$$

All middle terms cancel (telescoping sum).

Therefore: $(a - b) \cdot S = a^n - b^n$ ∎

**Application in Numerical Analysis:**

This identity is used to analyze the error $|x^n - x_0^n|$ when approximating a value $x$ by $x_0$:

$$|x^n - x_0^n| = |x - x_0| \cdot |x^{n-1} + x^{n-2}x_0 + \cdots + x_0^{n-1}|$$

If $|x|, |x_0| \leq M$, then the sum has $n$ terms each bounded by $M^{n-1}$, so:

$$|x^n - x_0^n| \leq n M^{n-1} |x - x_0|$$

This shows that small errors in $x$ can be amplified by a factor of $nM^{n-1}$ when computing $x^n$ — relevant to conditioning analysis.

---

### Problem 10 (Exam-Level)

**Simplify: $\frac{x^4 - 16}{x^3 + 8} \cdot \frac{x^2 - 2x + 4}{x^2 + 4} \div \frac{x - 2}{x + 2}$**

**Step 1:** Convert division to multiplication.
$$= \frac{x^4 - 16}{x^3 + 8} \cdot \frac{x^2 - 2x + 4}{x^2 + 4} \cdot \frac{x + 2}{x - 2}$$

**Step 2:** Factor all expressions.

$x^4 - 16 = (x^2 + 4)(x^2 - 4) = (x^2 + 4)(x + 2)(x - 2)$

$x^3 + 8 = (x + 2)(x^2 - 2x + 4)$ (sum of cubes)

$x^2 - 2x + 4$: doesn't factor (discriminant = $4 - 16 = -12 < 0$)

$x^2 + 4$: doesn't factor over ℝ

**Step 3:** Substitute factored forms.
$$= \frac{(x^2 + 4)(x + 2)(x - 2)}{(x + 2)(x^2 - 2x + 4)} \cdot \frac{x^2 - 2x + 4}{x^2 + 4} \cdot \frac{x + 2}{x - 2}$$

**Step 4:** Cancel common factors.

- $(x^2 + 4)$ cancels
- $(x + 2)$ appears twice in numerator, once in denominator — one cancels
- $(x - 2)$ cancels
- $(x^2 - 2x + 4)$ cancels

$$= \frac{\cancel{(x^2 + 4)} \cdot \cancel{(x + 2)} \cdot \cancel{(x - 2)}}{\cancel{(x + 2)} \cdot \cancel{(x^2 - 2x + 4)}} \cdot \frac{\cancel{(x^2 - 2x + 4)}}{\cancel{(x^2 + 4)}} \cdot \frac{(x + 2)}{\cancel{(x - 2)}}$$

**Step 5:** What remains.
$$= x + 2$$

**Answer:** $x + 2$, for $x \neq 2, -2$

**Verification:** The original expression is undefined at $x = 2$ (from $x - 2$ in denominator after converting division) and at $x = -2$ (from $x^3 + 8 = 0$). These restrictions carry through to the simplified answer.

---

### Problem 11 (PhD-level): A power-map bound

Factor x⁵−y⁵=(x−y)(x⁴+x³y+x²y²+xy³+y⁴). Each of the five terms in parentheses has absolute value at most 2⁴=16. The triangle inequality gives |x⁵−y⁵|≤5·16|x−y|=80|x−y|. For x≠0, F′(x)=5x⁴, so |xF′(x)/F(x)|=5. The first statement is a finite absolute bound on [−2,2]; the second is a local relative sensitivity at a nonzero input. Neither is a claim about roundoff error in a particular program.

## Summary

### Key Takeaways

- **Always factor out GCF first** before attempting other factoring techniques
- **Special patterns** (difference of squares, sum/difference of cubes) appear constantly — recognize them instantly
- **Rational expressions:** Factor completely, cancel carefully, track domain restrictions
- **Complex fractions:** Multiply by LCD of all inner fractions
- **Rationalizing:** Use conjugates for expressions with square roots
- **These techniques are tools for calculus/analysis** — difference quotients, limits, and partial fractions all require algebraic fluency

### Common Mistakes

- Forgetting domain restrictions after simplifying (cancelled factors still cause undefined points)
- Writing $a^2 + b^2 = (a + b)^2$ — this is wrong; $a^2 + b^2$ doesn't factor over ℝ
- Sign errors when distributing negatives across parentheses
- Incomplete factoring — always check if factors can be factored further
- Confusing $(a - b)^2 = a^2 - 2ab + b^2$ with $a^2 - b^2 = (a+b)(a-b)$

### What's Next

**Lesson M1.3: Equations and Inequalities** — solving polynomial, rational, radical, and absolute value equations; compound inequalities; sign analysis for rational inequalities.

---

*Ready for Lesson M1.3 when you are!*
