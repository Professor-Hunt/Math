# Lesson M1.3: Equations and Inequalities

---

**Prerequisites:** Lesson M1.1 (Real Numbers, Properties, and Order), Lesson M1.2 (Algebraic Manipulation and Factoring)

**Learning Objectives:**
- Solve polynomial equations using factoring, the quadratic formula, and substitution
- Solve rational equations while tracking domain restrictions
- Solve radical equations with proper verification of solutions
- Solve absolute value equations systematically
- Solve compound inequalities and express solutions in interval notation
- Use sign analysis to solve polynomial and rational inequalities
- Recognize equation structures that appear in calculus, analysis, and linear algebra

---

## High-school level — Solving and checking

An equation asks which inputs make two expressions equal. An inequality asks which inputs make one expression larger or smaller. For every method below, record where the original expressions are defined and substitute candidate answers back into the original statement.

## 1. Polynomial Equations

A **polynomial equation** has the form $p(x) = 0$ where $p(x)$ is a polynomial.

### 1.1 Linear Equations

**Form:** $ax + b = 0$ where $a \neq 0$

**Solution:** $x = -\frac{b}{a}$

**Example:** Solve $3x - 7 = 5$

$3x = 12 \Rightarrow x = 4$

### 1.2 Quadratic Equations

**Form:** $ax^2 + bx + c = 0$ where $a \neq 0$

**Methods:**
1. **Factoring** (when possible)
2. **Quadratic Formula:** $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
3. **Completing the Square**

**The Discriminant:** $\Delta = b^2 - 4ac$

<details class="math-explainer">
<summary>Explain the discriminant</summary>
<p><strong>Read the whole expression:</strong> Delta equals b squared minus four times a times c.</p>
<dl><dt>Δ, &#x27;delta&#x27;</dt><dd>Name for the number that determines how many real quadratic roots occur.</dd>
<dt>b²</dt><dd>The middle coefficient multiplied by itself.</dd>
<dt>a, b, c</dt><dd>Coefficients in ax²+bx+c with a nonzero.</dd>
<dt>−</dt><dd>Subtract four times the leading and constant coefficients.</dd></dl>
<p><strong>Example:</strong> For 2x²−5x−3, a=2, b=−5, c=−3, so Δ=25+24=49; there are two real roots.</p>
</details>

| Discriminant | Nature of Roots |
|--------------|-----------------|
| $\Delta > 0$ | Two distinct real roots |
| $\Delta = 0$ | One repeated real root |
| $\Delta < 0$ | Two complex conjugate roots (no real roots) |

**Example:** Solve $2x^2 - 5x - 3 = 0$

**Method 1 (Factoring):** Find factors of $ac = -6$ that sum to $b = -5$: Numbers are $-6$ and $1$.

$2x^2 - 6x + x - 3 = 2x(x - 3) + 1(x - 3) = (x - 3)(2x + 1) = 0$

Solutions: $x = 3$ or $x = -\frac{1}{2}$

**Method 2 (Quadratic Formula):**
$$x = \frac{5 \pm \sqrt{25 + 24}}{4} = \frac{5 \pm 7}{4}$$

$x = \frac{12}{4} = 3$ or $x = \frac{-2}{4} = -\frac{1}{2}$

### 1.3 Higher-Degree Polynomial Equations

**Strategies:**
1. **Factor out GCF** first
2. **Factor by grouping** for four terms
3. **Substitution** for equations in quadratic form
4. **Rational Root Theorem** for finding rational roots
5. **Synthetic division** to reduce degree after finding one root

**Rational Root Theorem:** If $p(x) = a_n x^n + \cdots + a_0$ has integer coefficients and $\frac{p}{q}$ is a rational root (in lowest terms), then:
- $p$ divides $a_0$ (constant term)
- $q$ divides $a_n$ (leading coefficient)

**Example:** Solve $x^4 - 5x^2 + 4 = 0$

This is **quadratic in form**. Let $u = x^2$:

$u^2 - 5u + 4 = 0$

$(u - 4)(u - 1) = 0$

$u = 4$ or $u = 1$

Back-substitute: $x^2 = 4 \Rightarrow x = \pm 2$ and $x^2 = 1 \Rightarrow x = \pm 1$

**Solutions:** $x \in \{-2, -1, 1, 2\}$

**Example:** Solve $x^3 - 6x^2 + 11x - 6 = 0$

By the Rational Root Theorem, possible rational roots are $\pm 1, \pm 2, \pm 3, \pm 6$.

Test $x = 1$: $1 - 6 + 11 - 6 = 0$ ✓

Use synthetic division to factor out $(x - 1)$:
```
1 │  1   -6    11   -6
  │       1    -5    6
  ────────────────────
     1   -5     6    0
```

So $x^3 - 6x^2 + 11x - 6 = (x - 1)(x^2 - 5x + 6) = (x - 1)(x - 2)(x - 3)$

**Solutions:** $x = 1, 2, 3$

---

## 2. Rational Equations

A **rational equation** contains at least one rational expression (fraction with variable in denominator).

### 2.1 Strategy

1. **Identify domain restrictions** (values that make any denominator zero)
2. **Multiply both sides by the LCD** to clear fractions
3. **Solve the resulting polynomial equation**
4. **Check solutions** against domain restrictions (reject extraneous solutions)

### 2.2 Extraneous Solutions

⚠️ **Critical:** When you multiply by an expression containing variables, you may introduce extraneous solutions. Always verify!

**Example:** Solve $\frac{3}{x-2} + \frac{2}{x+1} = \frac{5x-1}{(x-2)(x+1)}$

**Step 1:** Domain restrictions: $x \neq 2$ and $x \neq -1$

**Step 2:** LCD = $(x-2)(x+1)$. Multiply both sides:

$3(x+1) + 2(x-2) = 5x - 1$

$3x + 3 + 2x - 4 = 5x - 1$

$5x - 1 = 5x - 1$

This is an identity! The equation is true for **all** $x$ in the domain.

**Solution:** All real numbers except $x = 2$ and $x = -1$, i.e., $\mathbb{R} \setminus \{-1, 2\}$

**Example:** Solve $\frac{x}{x-3} = \frac{3}{x-3} + 2$

**Step 1:** Domain restriction: $x \neq 3$

**Step 2:** Multiply by $(x-3)$:

$x = 3 + 2(x-3)$

$x = 3 + 2x - 6$

$x = 2x - 3$

$-x = -3$

$x = 3$

**Step 3:** Check: $x = 3$ is excluded from the domain!

**Solution:** No solution (the equation has no solution; $\emptyset$)

---

## 3. Radical Equations

A **radical equation** contains a variable under a radical (square root, cube root, etc.).

### 3.1 Strategy for Square Roots

1. **Isolate the radical** on one side
2. **Square both sides** (introduces potential extraneous solutions)
3. **Solve the resulting equation**
4. **Verify all solutions** in the original equation

### 3.2 Why Verification is Essential

Squaring is not a reversible operation: $a = b \Rightarrow a^2 = b^2$, but $a^2 = b^2 \not\Rightarrow a = b$.

**Example:** Solve $\sqrt{2x + 3} = x$

**Step 1:** The radical is already isolated.

**Step 2:** Square both sides:

$2x + 3 = x^2$

$x^2 - 2x - 3 = 0$

$(x - 3)(x + 1) = 0$

$x = 3$ or $x = -1$

**Step 3:** Verify:

- $x = 3$: $\sqrt{2(3) + 3} = \sqrt{9} = 3$ ✓
- $x = -1$: $\sqrt{2(-1) + 3} = \sqrt{1} = 1 \neq -1$ ✗

**Solution:** $x = 3$ only

### 3.3 Equations with Two Radicals

**Example:** Solve $\sqrt{x + 5} - \sqrt{x} = 1$

**Step 1:** Isolate one radical:

$\sqrt{x + 5} = 1 + \sqrt{x}$

**Step 2:** Square both sides:

$x + 5 = 1 + 2\sqrt{x} + x$

$4 = 2\sqrt{x}$

$\sqrt{x} = 2$

**Step 3:** Square again:

$x = 4$

**Step 4:** Verify:

$\sqrt{4 + 5} - \sqrt{4} = \sqrt{9} - 2 = 3 - 2 = 1$ ✓

**Solution:** $x = 4$

### 3.4 Cube Roots and Higher

For odd roots, no verification is needed (cubing is one-to-one on $\mathbb{R}$).

**Example:** Solve $\sqrt[3]{2x - 1} = 3$

Cube both sides: $2x - 1 = 27$

$x = 14$

**Solution:** $x = 14$ (no verification needed)

---

## 4. Absolute Value Equations

### 4.1 Basic Form

**Equation:** $|A| = k$ where $k \geq 0$

**Solution:** $A = k$ or $A = -k$

<details class="math-explainer">
<summary>Explain the two absolute-value cases</summary>
<p><strong>Read the whole expression:</strong> If the distance of A from zero is k, then A is k or negative k.</p>
<dl><dt>|A|</dt><dd>Distance of the value A from zero.</dd>
<dt>k</dt><dd>A nonnegative target distance.</dd>
<dt>or</dt><dd>Either equality may supply a solution; check both.</dd></dl>
<p><strong>Example:</strong> |x−2|=3 means x−2=3 or x−2=−3, giving x=5 or x=−1.</p>
</details>

**Example:** Solve $|3x - 5| = 7$

$3x - 5 = 7$ or $3x - 5 = -7$

$x = 4$ or $x = -\frac{2}{3}$

### 4.2 Equations with Two Absolute Values

**Equation:** $|A| = |B|$

**Solution:** $A = B$ or $A = -B$

**Example:** Solve $|2x - 1| = |x + 4|$

**Case 1:** $2x - 1 = x + 4 \Rightarrow x = 5$

**Case 2:** $2x - 1 = -(x + 4) \Rightarrow 2x - 1 = -x - 4 \Rightarrow 3x = -3 \Rightarrow x = -1$

**Verify:**
- $x = 5$: $|10 - 1| = |5 + 4| \Rightarrow 9 = 9$ ✓
- $x = -1$: $|-2 - 1| = |-1 + 4| \Rightarrow 3 = 3$ ✓

**Solution:** $x = 5$ or $x = -1$

### 4.3 No Solution Cases

If $|A| = k$ where $k < 0$, there is **no solution** (absolute value is never negative).

**Example:** $|2x + 3| = -5$ has no solution.

---

## 5. Compound Inequalities

### 5.1 Conjunction ("And")

**Form:** $a < x < b$ (equivalent to $x > a$ AND $x < b$)

The solution is the **intersection** of the individual solutions.

**Example:** Solve $-3 < 2x + 1 \leq 7$

Subtract 1: $-4 < 2x \leq 6$

Divide by 2: $-2 < x \leq 3$

**Solution:** $(-2, 3]$

### 5.2 Disjunction ("Or")

**Form:** $x < a$ OR $x > b$

The solution is the **union** of the individual solutions.

**Example:** Solve $3x - 1 < -7$ or $2x + 5 > 11$

First inequality: $3x < -6 \Rightarrow x < -2$

Second inequality: $2x > 6 \Rightarrow x > 3$

**Solution:** $(-\infty, -2) \cup (3, \infty)$

---

## Undergraduate level — Sign analysis and domains

An interval sign chart converts a global inequality into finitely many local checks. Polynomial signs can change only at roots, because polynomials are continuous; a rational expression can also change behavior at excluded denominator zeros. Never include a point where the original expression is undefined.

## 6. Polynomial and Rational Inequalities

### 6.1 Sign Analysis Method

**Key Principle:** A polynomial (or rational expression) can only change sign at its **zeros** (or points of discontinuity for rational expressions).

**Steps:**
1. Move all terms to one side (get $\geq 0$, $\leq 0$, $> 0$, or $< 0$)
2. Factor completely
3. Find **critical points** (zeros of numerator and denominator)
4. Create a **sign chart** with test points in each interval
5. Identify intervals satisfying the inequality
6. Include/exclude endpoints based on the inequality type and domain

### 6.2 Polynomial Inequalities

**Example:** Solve $x^2 - 4x - 5 > 0$

**Step 1:** Factor: $(x - 5)(x + 1) > 0$

**Step 2:** Critical points: $x = -1$ and $x = 5$

<details class="math-explainer">
<summary>Explain a sign-chart interval</summary>
<p><strong>Read the whole expression:</strong> The roots negative one and five split the number line into three intervals, on each of which the polynomial keeps one sign.</p>
<dl><dt>root or zero</dt><dd>An input making the polynomial equal zero.</dd>
<dt>(−∞,−1)</dt><dd>All real inputs smaller than negative one; the endpoint is excluded.</dd>
<dt>∪, &#x27;union&#x27;</dt><dd>Join intervals that both satisfy the requested sign.</dd></dl>
<p><strong>Example:</strong> For (x−5)(x+1)&gt;0, test x=−2, 0, and 6; the first and last intervals work.</p>
</details>

**Step 3:** Sign chart:

| Interval | $(x - 5)$ | $(x + 1)$ | Product |
|----------|-----------|-----------|---------|
| $x < -1$ | $-$ | $-$ | $+$ |
| $-1 < x < 5$ | $-$ | $+$ | $-$ |
| $x > 5$ | $+$ | $+$ | $+$ |

**Step 4:** We want product $> 0$: intervals where product is positive.

**Solution:** $(-\infty, -1) \cup (5, \infty)$

### 6.3 Rational Inequalities

⚠️ **Critical:** Never multiply both sides by an expression that could be negative without considering cases!

**Example:** Solve $\frac{x + 2}{x - 1} \leq 0$

**Step 1:** Expression is already simplified with 0 on one side.

**Step 2:** Critical points:
- Numerator zero: $x = -2$
- Denominator zero: $x = 1$ (excluded from domain)

**Step 3:** Sign chart:

| Interval | $(x + 2)$ | $(x - 1)$ | Quotient |
|----------|-----------|-----------|----------|
| $x < -2$ | $-$ | $-$ | $+$ |
| $-2 < x < 1$ | $+$ | $-$ | $-$ |
| $x > 1$ | $+$ | $+$ | $+$ |

**Step 4:** We want quotient $\leq 0$: where quotient is negative or zero.

- Negative in $(-2, 1)$
- Zero at $x = -2$ (include because $\leq$)
- Not defined at $x = 1$ (exclude)

**Solution:** $[-2, 1)$

### 6.4 More Complex Example

**Example:** Solve $\frac{x^2 - 4}{x^2 - 9} > 0$

**Step 1:** Factor:
$$\frac{(x-2)(x+2)}{(x-3)(x+3)} > 0$$

**Step 2:** Critical points: $x = -3, -2, 2, 3$

Domain restrictions: $x \neq -3, 3$

**Step 3:** Sign chart (5 intervals):

| Interval | $(x-2)$ | $(x+2)$ | $(x-3)$ | $(x+3)$ | Overall |
|----------|---------|---------|---------|---------|---------|
| $x < -3$ | $-$ | $-$ | $-$ | $-$ | $+$ |
| $-3 < x < -2$ | $-$ | $-$ | $-$ | $+$ | $-$ |
| $-2 < x < 2$ | $-$ | $+$ | $-$ | $+$ | $+$ |
| $2 < x < 3$ | $+$ | $+$ | $-$ | $+$ | $-$ |
| $x > 3$ | $+$ | $+$ | $+$ | $+$ | $+$ |

**Step 4:** We want $> 0$ (strictly positive):

**Solution:** $(-\infty, -3) \cup (-2, 2) \cup (3, \infty)$

---

## Master's level — Existence, uniqueness, and iteration

**Prerequisite bridge.** A continuous function has no jumps. The Intermediate Value Theorem (IVT) says that if a continuous function has opposite signs at the ends of an interval, it has a root inside. IVT proves **existence**, not uniqueness. To prove uniqueness, add a separate fact, such as strict monotonicity: a strictly decreasing function cannot cross zero twice.

Newton's method uses a tangent line: xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ), provided f′(xₙ) is nonzero. Smoothness and a simple root give *local* convergence only when the starting point is sufficiently close. A specified starting point needs a further argument; Problem 7 gives one using convexity on an interval. Convex means the graph lies above each tangent line, a fact reflected by f″ ≥ 0 when the second derivative exists.

<details class="math-explainer">
<summary>Explain the Newton update in this problem</summary>
<p><strong>Read the whole expression:</strong> The next estimate equals the current estimate minus the function value divided by its slope there.</p>
<dl><dt>xₙ</dt><dd>Current estimate of a root.</dd>
<dt>f(xₙ)</dt><dd>Current error in the equation f(x)=0, measured as a function value.</dd>
<dt>f′(xₙ), &#x27;f prime&#x27;</dt><dd>Slope of f at the current estimate; it must be nonzero.</dd>
<dt>xₙ₊₁</dt><dd>Next estimate obtained from the tangent&#x27;s zero.</dd></dl>
<p><strong>Example:</strong> For f(x)=x²−2 and x₀=1, the slope is 2 and the value is −1, so x₁=1−(−1)/2=1.5.</p>
</details>

## PhD-level connection — Contraction and quadratic forms

**Prerequisite bridge.** A *fixed point* of a map T is an input x* with T(x*)=x*. On a closed interval, if T maps the interval into itself and shrinks every distance by one common factor q<1, repeated application converges to a unique fixed point. The self-map condition matters: a small derivative bound alone does not keep iterates in the interval. In Problem 9, T(x)=cos x maps [0,1] into [cos 1,1]⊂[0,1], and |T′(x)|≤sin 1<1 there. Every solution in [0,π/2] is at most 1, so uniqueness on [0,1] also gives uniqueness on the larger interval.

<details class="math-explainer">
<summary>Explain the fixed-point condition</summary>
<p><strong>Read the whole expression:</strong> A fixed point x star is unchanged by T, and a contraction makes output distances smaller than input distances.</p>
<dl><dt>T(x*)=x*</dt><dd>Applying T to x* returns the same point.</dd>
<dt>T([0,1])⊂[0,1]</dt><dd>Every input in the interval stays inside it after one step.</dd>
<dt>|T′(x)|≤q&lt;1</dt><dd>A uniform slope bound that makes T shrink distances on this interval.</dd>
<dt>q</dt><dd>One shrinking factor valid for every pair of inputs, not a factor chosen separately at each point.</dd></dl>
<p><strong>Example:</strong> For T(x)=cos x on [0,1], q=sin 1 works; the fixed point is approximately 0.739.</p>
</details>

A **quadratic form** in two variables is homogeneous: Q(u,v)=au²+buv+cv². It can be written as [u v]A[u v]ᵀ for the symmetric matrix A with rows (a,b/2) and (b/2,c). The one-variable polynomial f(x)=ax²+bx+c is the *slice* Q(x,1), not itself a quadratic form. Under a>0, the condition b²<4ac is equivalent both to f(x)>0 for every real x and to Q(u,v)>0 for every nonzero pair (u,v). Completing the square proves the latter: Q(u,v)=a(u+bv/(2a))²+(c−b²/(4a))v².

<details class="math-explainer">
<summary>Explain positive definiteness here</summary>
<p><strong>Read the whole expression:</strong> Q is positive definite when it gives a positive value for every nonzero pair of inputs.</p>
<dl><dt>Q(u,v)</dt><dd>A homogeneous degree-two expression in two inputs.</dd>
<dt>(u,v)≠(0,0)</dt><dd>At least one input is nonzero.</dd>
<dt>b²&lt;4ac</dt><dd>The condition making both squared terms in the completed-square form positive in the required sense.</dd>
<dt>f(x)=Q(x,1)</dt><dd>The familiar parabola is a one-dimensional slice of Q.</dd></dl>
<p><strong>Example:</strong> If a=c=1 and b=0, Q(u,v)=u²+v² is positive for every nonzero pair; f(x)=x²+1 is positive for every real x.</p>
</details>

## Practice Problems

### Basic

**Problem 1:** Solve for $x$: $x^2 + 2x - 15 = 0$

**Problem 2:** Solve for $x$: $\frac{5}{x+2} = \frac{3}{x-1}$

**Problem 3:** Solve and express in interval notation: $|2x - 7| \leq 5$

### Intermediate

**Problem 4:** Solve: $\sqrt{3x + 1} - \sqrt{x - 1} = 2$

**Problem 5:** Solve: $x^3 - 2x^2 - 5x + 6 = 0$

**Problem 6:** Solve and express in interval notation: $\frac{x - 3}{x + 4} \geq 2$

### Exam-Level

**Problem 7:** *(Real Analysis Connection)*

Let $f(x) = x^3 - 3x + 1$.

(a) Show that $f$ has exactly three real roots.

(b) Prove that exactly one root lies in the interval $(0, 1)$.

(c) Show that Newton's method starting from $x_0 = 0.5$ converges to this root. Give a reason beyond IVT for this specific starting point.

**Problem 8:** *(Linear Algebra Connection)*

Find all values of $\lambda$ for which the matrix 
$$A - \lambda I = \begin{pmatrix} 3 - \lambda & 1 \\ 4 & 3 - \lambda \end{pmatrix}$$
is singular (i.e., find the eigenvalues of $A$).

**Problem 9:** *(Numerical Analysis Connection)*

The equation $x = \cos(x)$ has a unique solution in $[0, \pi/2]$.

(a) Prove that a solution exists using the Intermediate Value Theorem.

(b) Show that the iteration $x_{n+1} = \cos(x_n)$ is a contraction on $[0, 1]$ by verifying $|\cos'(x)| < 1$ for $x \in [0, 1]$.

(c) If fixed-point iteration converges linearly, what does this tell us about $\cos'(x^*)$ where $x^*$ is the fixed point?

**Problem 10:** *(Analysis/Optimization Connection)*

Solve the inequality that determines when the quadratic $f(x) = ax^2 + bx + c$ (with $a > 0$) satisfies $f(x) > 0$ for all real $x$.

---

## Solutions

### Problem 1: Solve $x^2 + 2x - 15 = 0$

**Solution:**

**Step 1:** Factor the quadratic.

We need two numbers with product $-15$ and sum $2$. These are $5$ and $-3$.

$x^2 + 2x - 15 = (x + 5)(x - 3) = 0$

**Step 2:** Apply zero product property.

$x + 5 = 0$ or $x - 3 = 0$

$x = -5$ or $x = 3$

**Verification:**
- $x = -5$: $(-5)^2 + 2(-5) - 15 = 25 - 10 - 15 = 0$ ✓
- $x = 3$: $(3)^2 + 2(3) - 15 = 9 + 6 - 15 = 0$ ✓

**Answer:** $x = -5$ or $x = 3$

---

### Problem 2: Solve $\frac{5}{x+2} = \frac{3}{x-1}$

**Solution:**

**Step 1:** Identify domain restrictions.

$x \neq -2$ and $x \neq 1$

**Step 2:** Cross-multiply (since both sides are single fractions).

$5(x - 1) = 3(x + 2)$

$5x - 5 = 3x + 6$

$2x = 11$

$x = \frac{11}{2}$

**Step 3:** Verify domain.

$x = \frac{11}{2} = 5.5 \neq -2$ and $\neq 1$ ✓

**Verification:**
- LHS: $\frac{5}{5.5 + 2} = \frac{5}{7.5} = \frac{2}{3}$
- RHS: $\frac{3}{5.5 - 1} = \frac{3}{4.5} = \frac{2}{3}$ ✓

**Answer:** $x = \frac{11}{2}$

---

### Problem 3: Solve $|2x - 7| \leq 5$

**Solution:**

**Step 1:** Apply the absolute value inequality rule.

For $|A| \leq k$ where $k \geq 0$: $-k \leq A \leq k$

$-5 \leq 2x - 7 \leq 5$

**Step 2:** Solve the compound inequality.

Add 7 to all parts:
$2 \leq 2x \leq 12$

Divide by 2:
$1 \leq x \leq 6$

**Answer:** $[1, 6]$

**Verification:** Test boundary and interior points:
- $x = 1$: $|2(1) - 7| = |-5| = 5 \leq 5$ ✓
- $x = 6$: $|2(6) - 7| = |5| = 5 \leq 5$ ✓
- $x = 3.5$: $|2(3.5) - 7| = |0| = 0 \leq 5$ ✓

---

### Problem 4: Solve $\sqrt{3x + 1} - \sqrt{x - 1} = 2$

**Solution:**

**Step 1:** Domain analysis.

For $\sqrt{3x + 1}$: need $3x + 1 \geq 0 \Rightarrow x \geq -\frac{1}{3}$

For $\sqrt{x - 1}$: need $x - 1 \geq 0 \Rightarrow x \geq 1$

Domain: $x \geq 1$

**Step 2:** Isolate one radical.

$\sqrt{3x + 1} = 2 + \sqrt{x - 1}$

**Step 3:** Square both sides.

$3x + 1 = 4 + 4\sqrt{x - 1} + (x - 1)$

$3x + 1 = 3 + x + 4\sqrt{x - 1}$

$2x - 2 = 4\sqrt{x - 1}$

$x - 1 = 2\sqrt{x - 1}$

**Step 4:** Substitute $u = \sqrt{x - 1}$ (so $u^2 = x - 1$).

$u^2 = 2u$

$u^2 - 2u = 0$

$u(u - 2) = 0$

$u = 0$ or $u = 2$

**Step 5:** Back-substitute.

$\sqrt{x - 1} = 0 \Rightarrow x - 1 = 0 \Rightarrow x = 1$

$\sqrt{x - 1} = 2 \Rightarrow x - 1 = 4 \Rightarrow x = 5$

**Step 6:** Verify in original equation.

$x = 1$: $\sqrt{3(1) + 1} - \sqrt{1 - 1} = \sqrt{4} - 0 = 2$ ✓

$x = 5$: $\sqrt{3(5) + 1} - \sqrt{5 - 1} = \sqrt{16} - \sqrt{4} = 4 - 2 = 2$ ✓

**Answer:** $x = 1$ or $x = 5$

---

### Problem 5: Solve $x^3 - 2x^2 - 5x + 6 = 0$

**Solution:**

**Step 1:** Use the Rational Root Theorem.

Possible rational roots: $\pm 1, \pm 2, \pm 3, \pm 6$

**Step 2:** Test candidates.

$x = 1$: $1 - 2 - 5 + 6 = 0$ ✓

**Step 3:** Factor using synthetic division.

```
1 │  1   -2   -5    6
  │       1   -1   -6
  ─────────────────────
     1   -1   -6    0
```

$x^3 - 2x^2 - 5x + 6 = (x - 1)(x^2 - x - 6)$

**Step 4:** Factor the quadratic.

$x^2 - x - 6 = (x - 3)(x + 2)$

**Step 5:** Complete factorization.

$x^3 - 2x^2 - 5x + 6 = (x - 1)(x - 3)(x + 2) = 0$

**Answer:** $x = -2, 1, 3$

---

### Problem 6: Solve $\frac{x - 3}{x + 4} \geq 2$

**Solution:**

**Step 1:** Move all terms to one side.

$\frac{x - 3}{x + 4} - 2 \geq 0$

$\frac{x - 3 - 2(x + 4)}{x + 4} \geq 0$

$\frac{x - 3 - 2x - 8}{x + 4} \geq 0$

$\frac{-x - 11}{x + 4} \geq 0$

**Step 2:** Find critical points.

Numerator zero: $-x - 11 = 0 \Rightarrow x = -11$

Denominator zero: $x + 4 = 0 \Rightarrow x = -4$ (excluded from domain)

**Step 3:** Sign chart.

| Interval | $(-x - 11)$ | $(x + 4)$ | Quotient |
|----------|-------------|-----------|----------|
| $x < -11$ | $+$ | $-$ | $-$ |
| $-11 < x < -4$ | $-$ | $-$ | $+$ |
| $x > -4$ | $-$ | $+$ | $-$ |

**Step 4:** Identify solution.

We need quotient $\geq 0$:
- Positive in $(-11, -4)$
- Zero at $x = -11$ (include because $\geq$)
- Undefined at $x = -4$ (exclude)

**Answer:** $[-11, -4)$

**Verification:** 
- $x = -11$: $\frac{-11 - 3}{-11 + 4} = \frac{-14}{-7} = 2 \geq 2$ ✓
- $x = -7$: $\frac{-7 - 3}{-7 + 4} = \frac{-10}{-3} = \frac{10}{3} \approx 3.33 \geq 2$ ✓

---

### Problem 7: Real Analysis Connection — Cubic Roots

Let $f(x) = x^3 - 3x + 1$.

**(a) Show that $f$ has exactly three real roots.**

**Solution:**

**Step 1:** Analyze the derivative.

$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x-1)(x+1)$

Critical points: $x = -1$ and $x = 1$

**Step 2:** Classify critical points using second derivative or sign analysis.

$f''(x) = 6x$

- At $x = -1$: $f''(-1) = -6 < 0$ → local maximum
- At $x = 1$: $f''(1) = 6 > 0$ → local minimum

**Step 3:** Evaluate $f$ at critical points.

$f(-1) = (-1)^3 - 3(-1) + 1 = -1 + 3 + 1 = 3 > 0$

$f(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1 < 0$

**Step 4:** Analyze end behavior.

$\lim_{x \to -\infty} f(x) = -\infty$ and $\lim_{x \to +\infty} f(x) = +\infty$

**Step 5:** Apply the Intermediate Value Theorem.

Since $f$ is continuous:
- the limit of $f(x)$ as $x\to-\infty$ is negative infinity, so some finite left endpoint has $f(x)<0$, while $f(-1)=3>0$ → root in $(-\infty, -1)$
- $f(-1) = 3 > 0$ and $f(1) = -1 < 0$ → root in $(-1, 1)$
- $f(1)=-1<0$, while $f(x)\to+\infty$ as $x\to+\infty$, so some finite right endpoint has $f(x)>0$ → root in $(1, +\infty)$

Since a cubic has at most 3 real roots, **$f$ has exactly three real roots.** ∎

**(b) Prove that exactly one root lies in $(0, 1)$.**

**Solution:**

$f(0) = 0 - 0 + 1 = 1 > 0$

$f(1) = 1 - 3 + 1 = -1 < 0$

By IVT, since $f(0) > 0$ and $f(1) < 0$, there exists at least one $c \in (0, 1)$ with $f(c) = 0$.

For uniqueness: On $(0, 1)$, we have $f'(x) = 3x^2 - 3 = 3(x^2 - 1) < 0$ (since $x^2 < 1$).

Thus $f$ is strictly decreasing on $(0, 1)$, so there can be **at most one** root.

Combined: **Exactly one root in $(0, 1)$.** ∎

**(c) Newton's method convergence from $x_0 = 0.5$.**

Newton's update is $x_{n+1}=x_n-f(x_n)/f'(x_n)$. Here $f(1/2)=-3/8$ and $f'(1/2)=-9/4$, so $x_1=1/2-1/6=1/3$. Also $f(1/3)=1/27>0$ and $f(1/2)<0$, so the unique root $r$ lies in $(1/3,1/2)$.

On $[1/3,r]$, $f'(x)=3x^2-3<0$ and $f''(x)=6x>0$: the function is decreasing and convex. If $x<r$, then $f(x)>0$, and the Newton update $N(x)=x-f(x)/f'(x)$ is greater than $x$. Convexity puts the graph above its tangent at $x$, so $0=f(r)\ge f(x)+f'(x)(r-x)$. Since $f'(x)<0$, rearranging gives $N(x)\le r$. Thus, starting at $x_1=1/3$, the iterates increase but stay at or below $r$. They converge to a limit $L$; continuity of $N$ on this interval gives $L=N(L)$, hence $f(L)=0$ and $L=r$. The first two steps are $x_1=1/3$ and $x_2=25/72\approx0.34722$.

IVT established the root's existence; monotonicity and convexity justify convergence from this particular starting point. The root is simple, so the eventual convergence rate is quadratic.

---

### Problem 8: Linear Algebra Connection — Eigenvalues

Find all $\lambda$ for which $A - \lambda I = \begin{pmatrix} 3 - \lambda & 1 \\ 4 & 3 - \lambda \end{pmatrix}$ is singular.

**Solution:**

A matrix is singular if and only if its determinant is zero.

**Step 1:** Compute the determinant.

$\det(A - \lambda I) = (3 - \lambda)(3 - \lambda) - (1)(4)$

$= (3 - \lambda)^2 - 4$

$= 9 - 6\lambda + \lambda^2 - 4$

$= \lambda^2 - 6\lambda + 5$

**Step 2:** Set equal to zero and solve (this is the characteristic equation).

$\lambda^2 - 6\lambda + 5 = 0$

Factor: $(\lambda - 5)(\lambda - 1) = 0$

**Step 3:** Find eigenvalues.

$\lambda = 5$ or $\lambda = 1$

**Verification of properties:**
- Sum of eigenvalues: $5 + 1 = 6 = \text{tr}(A) = 3 + 3$ ✓
- Product of eigenvalues: $5 \cdot 1 = 5 = \det(A) = 9 - 4 = 5$ ✓

**Answer:** The eigenvalues are $\lambda = 1$ and $\lambda = 5$.

---

### Problem 9: Numerical Analysis Connection — Fixed Point Iteration

The equation $x = \cos(x)$ has a unique solution in $[0, \pi/2]$.

**(a) Prove existence using IVT.**

**Solution:**

Define $g(x) = x - \cos(x)$.

$g(0) = 0 - \cos(0) = 0 - 1 = -1 < 0$

$g(\pi/2) = \pi/2 - \cos(\pi/2) = \pi/2 - 0 = \pi/2 > 0$

Since $g$ is continuous on $[0, \pi/2]$ and $g(0) < 0 < g(\pi/2)$, by the Intermediate Value Theorem, there exists $c \in (0, \pi/2)$ such that $g(c) = 0$, i.e., $c = \cos(c)$. ∎

**Uniqueness on $[0,\pi/2]$.** The function $g(x)=x-\cos x$ has derivative $g'(x)=1+\sin x>0$ there, so it is strictly increasing and has at most one root. Together with IVT, it has exactly one.

**(b) Show the iteration is a contraction on $[0, 1]$.**

**Solution:**

For $\phi(x) = \cos(x)$ to be a contraction on $[0, 1]$, we need $|\phi'(x)| < 1$ for all $x \in [0, 1]$.

$\phi'(x) = -\sin(x)$

$|\phi'(x)| = |\sin(x)|$

For $x \in [0, 1]$:
- At $x = 0$: $|\sin(0)| = 0$
- At $x = 1$: $|\sin(1)| \approx 0.841$

Since $\sin$ is increasing on $[0, 1]$ (as $1 < \pi/2$):

$|\phi'(x)| = \sin(x) \leq \sin(1) \approx 0.841 < 1$ for all $x \in [0, 1]$

Therefore, $\phi$ is a contraction with Lipschitz constant $L = \sin(1) < 1$. ∎

The iteration also stays inside the interval: $\cos([0,1])=[\cos 1,1]\subset[0,1]$. Thus the contraction theorem applies on $[0,1]$.

**(c) Linear convergence and $\cos'(x^*)$.**

**Solution:**

For fixed-point iteration $x_{n+1} = \phi(x_n)$, the convergence is linear with rate $|\phi'(x^*)|$ when $0 < |\phi'(x^*)| < 1$.

The error satisfies: $|x_{n+1} - x^*| \approx |\phi'(x^*)| \cdot |x_n - x^*|$

At the fixed point $x^* \approx 0.739$:

$|\cos'(x^*)| = |\sin(x^*)| = \sin(0.739) \approx 0.673$

This means:
- Each iteration reduces the error by a factor of approximately $0.673$
- The convergence is **linear** (not quadratic like Newton's method)
- For sufficiently late iterations, each additional step multiplies the error by approximately $0.673$; the simple $(0.673)^n$ estimate is asymptotic, not an exact bound from an arbitrary initial guess

**Interpretation:** Since $\cos'(x^*) \neq 0$, we get only linear convergence. If we wanted faster convergence, we could use Newton's method on $g(x) = x - \cos(x)$, which would give quadratic convergence. ∎

---

### Problem 10: Analysis/Optimization Connection — Positive Definite Quadratic

**Problem:** Solve the inequality that determines when $f(x) = ax^2 + bx + c$ (with $a > 0$) satisfies $f(x) > 0$ for all real $x$.

**Solution:**

**Step 1:** Understand the geometry.

Since $a > 0$, the parabola opens upward. For $f(x) > 0$ for all $x$, the parabola must lie entirely above the x-axis.

This happens if and only if the parabola has **no real roots**.

**Step 2:** Apply the discriminant condition.

The quadratic $ax^2 + bx + c = 0$ has no real roots when:

$\Delta = b^2 - 4ac < 0$

**Step 3:** State the condition.

$$b^2 - 4ac < 0$$

Or equivalently:

$$b^2 < 4ac$$

**Answer:** $f(x) = ax^2 + bx + c > 0$ for all $x \in \mathbb{R}$ if and only if $a > 0$ and $b^2 < 4ac$.

**Connection to Linear Algebra:** The expression $f(x)=ax^2+bx+c$ is not a quadratic form because it includes lower-degree terms. Define the homogeneous quadratic form $Q(u,v)=au^2+buv+cv^2$ instead; then $f(x)=Q(x,1)$. The symmetric matrix of $Q$ is $A=\begin{pmatrix}a&b/2\\b/2&c\end{pmatrix}$. Completing the square gives $Q(u,v)=a(u+bv/(2a))^2+(c-b^2/(4a))v^2$. Hence, under $a>0$, $Q$ is positive definite exactly when $b^2<4ac$, the same condition found for $f(x)>0$ on all of $\mathbb R$.

This generalizes to the Sylvester criterion for positive definiteness of $n \times n$ matrices. ∎

---

## Summary

### Key Takeaways

- **Polynomial equations:** Use factoring, quadratic formula, rational root theorem, or substitution based on structure
- **Rational equations:** Always find domain restrictions first; check for extraneous solutions
- **Radical equations:** Isolate, raise to power, solve, **verify** (squaring can introduce false solutions)
- **Absolute value equations:** Split into cases; $|A| = k$ means $A = k$ or $A = -k$
- **Compound inequalities:** "And" = intersection; "Or" = union
- **Sign analysis:** Factor completely, find critical points, test intervals, respect domain restrictions

### Common Mistakes

- Forgetting to check solutions against domain restrictions
- Not reversing inequality when multiplying/dividing by negative
- Missing extraneous solutions from squaring radical equations
- Incorrectly assuming $|A| = |B|$ implies $A = B$ (also need to check $A = -B$)
- Including points where rational expressions are undefined
- Sign errors when distributing negatives in compound inequalities

### Connections to Advanced Topics

| Technique | Where It Appears |
|-----------|------------------|
| Solving polynomial equations | Finding eigenvalues (characteristic polynomial) |
| Sign analysis | Optimization (determining where $f'(x) > 0$) |
| Rational equations | Partial fractions, resolvent equations |
| IVT for existence | Proving existence of roots, fixed points |
| Discriminant conditions | Positive definiteness, stability analysis |

### What's Next

**Lesson M1.4: Functions — Definitions and Notation** covers function concepts, domain/range, composition, inverses, and transformations — essential language for calculus and analysis.

---

*Ready for Lesson M1.4 when you are!*
