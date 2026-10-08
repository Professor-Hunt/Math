# Lesson M1.4: Functions: Definitions and Notation

**Prerequisites:** Lessons M1.1–M1.3

**Estimated study time:** 3 hours

## Learning Objectives

- Define a function using its domain, codomain, and assignment rule; distinguish the range from the codomain.
- Find natural domains and ranges, and evaluate functions given by formulas or cases.
- Form sums, products, quotients, and compositions while tracking their domains.
- Decide when a function has an inverse and find the inverse with its correct domain and range.
- Describe basic graph transformations and use function notation in simple models.

## 1. What is a function?

A **function** \(f:A\to B\) assigns **exactly one** element \(f(x)\in B\) to every input \(x\in A\). The set \(A\) is the **domain**, \(B\) is the **codomain**, and the **range** (or image) is \(f(A)=\{f(x):x\in A\}\subseteq B\). The assignment need not use every value in \(B\).

For example, \(f:\mathbb R\to\mathbb R\), \(f(x)=x^2\), has range \([0,\infty)\), even though its codomain is all of \(\mathbb R\). A different declaration, \(f:\mathbb R\to[0,\infty)\) with the same rule, has a different codomain. The declared domain matters too: \(x^2\) on \(\mathbb R\) and \(x^2\) on \([0,\infty)\) are different functions, and only the latter has an inverse from its range back to its domain.

The notation \(f(x)\) means the **output at input \(x\)**. It does not mean \(f\) multiplied by \(x\). To evaluate \(f(a+h)\), substitute the entire expression \(a+h\) for the input.

**Example.** For \(f(x)=x^2-3x\),

\[\begin{aligned}f(a+h)&=(a+h)^2-3(a+h)\\&=a^2+2ah+h^2\\&\quad-3a-3h.\end{aligned}\]

This substitution is the starting point for the difference quotient in calculus.

### Graphs and the vertical line test

The graph is \(\{(x,f(x)):x\in A\}\). Every vertical line intersects a function graph **at most once**. An intersection is not required when that \(x\) is outside the domain. The circle \(x^2+y^2=1\) fails this test: for most \(x\in(-1,1)\), there are two \(y\)-values.

## 2. Domain and range

When a formula is supplied without a stated domain, its **natural real domain** consists of all real inputs for which the formula has a real value. In particular, denominators cannot be zero and even-root radicands must be nonnegative. A stated domain may restrict this further.

**Example: combined restrictions.** For

\[f(x)=\frac{\sqrt{9-x^2}}{x-1},\]

the radicand requires \(-3\le x\le3\), and the denominator excludes \(x=1\). Thus the domain is \([-3,1)\cup(1,3]\). Do not cancel or otherwise simplify a formula before recording its original exclusions.

The **range** answers a different question: which outputs actually occur? For \(f(x)=x^2\) on \([-2,3]\), the minimum is \(0\) at \(x=0\) and the maximum is \(9\) at \(x=3\). Every value between them occurs, so the range is \([0,9]\). The codomain must contain this range; it need not equal it.

### Piecewise functions

A piecewise rule assigns one expression to each part of the domain. Check the condition **before** evaluating:

\[p(x)=\begin{cases}x+1,&x<0,\\x^2,&0\le x\le2,\\5,&x>2.\end{cases}\]

Here \(p(-2)=-1\), \(p(0)=0\), \(p(2)=4\), and \(p(3)=5\). The first branch gives \(( -\infty,1)\), the middle gives \([0,4]\), and the last gives \(\{5\}\). Their union is \(( -\infty,4]\cup\{5\}\). A boundary belongs to the branch whose inequality includes equality.

## 3. Combining and composing functions

If \(f\) and \(g\) are real-valued, \((f+g)(x)=f(x)+g(x)\) and \((fg)(x)=f(x)g(x)\) are defined where **both** inputs are allowed. The quotient \((f/g)(x)=f(x)/g(x)\) also requires \(g(x)\ne0\).

Composition means doing the inner function first:

\[(f\circ g)(x)=f(g(x)).\]

Its domain is \(\{x\in\operatorname{dom}(g):g(x)\in\operatorname{dom}(f)\}\). Order matters: generally \(f\circ g\ne g\circ f\).

**Example.** Let \(f(x)=\sqrt{x-1}\), with domain \([1,\infty)\), and \(g(x)=x^2-2\), with domain \(\mathbb R\). Then

\[\begin{aligned}(f\circ g)(x)&=\sqrt{x^2-3},\\\operatorname{dom}(f\circ g)&=(-\infty,-\sqrt3]\\&\quad\cup[\sqrt3,\infty).\end{aligned}\]

Conversely, \((g\circ f)(x)=(\sqrt{x-1})^2-2=x-3\), but its domain is still \([1,\infty)\). The simplified rule \(x-3\) does **not** extend this composition to inputs below \(1\).

## 4. One-to-one functions and inverses

A function is **one-to-one** (injective) if \(f(a)=f(b)\) implies \(a=b\). On a graph, every horizontal line then intersects at most once. A function has an inverse \(f^{-1}:f(A)\to A\) precisely when it is one-to-one, if the inverse's domain is taken to be the range of \(f\). To have an inverse defined on the **entire declared codomain** \(B\), \(f:A\to B\) must also be onto \(B\).

For an invertible function,

\[\begin{aligned}f^{-1}(f(x))&=x\quad(x\in A),\\f(f^{-1}(y))&=y\quad(y\in f(A)).\end{aligned}\]

The notation \(f^{-1}\) does **not** mean \(1/f\).

**Example.** If \(f:\mathbb R\to\mathbb R\) is \(f(x)=3x-2\), write \(y=3x-2\) and solve for \(x\): \(x=(y+2)/3\). Thus \(f^{-1}(x)=(x+2)/3\). Substitution in both directions verifies the inverse.

The function \(x\mapsto x^2\) is not one-to-one on \(\mathbb R\), because \(f(-2)=f(2)\). Restricted to \([0,\infty)\), it is one-to-one with inverse \(x\mapsto\sqrt{x}\) on \([0,\infty)\). **Restricting the domain changes the function.**

## 5. Transformations and simple models

Starting with \(y=f(x)\):

| New rule | Effect on the graph |
|---|---|
| \(f(x)+k\) | Shift up by \(k\) (down if \(k<0\)) |
| \(f(x-h)\) | Shift right by \(h\) (left if \(h<0\)) |
| \(af(x)\) | Multiply output heights by \(|a|\); reflect across the horizontal axis if \(a<0\) |
| \(f(bx)\) | Multiply input coordinates by \(1/|b|\); reflect across the vertical axis if \(b<0\), for \(b\ne0\) |

For \(f(x)=|x|\), the graph of \(y=-2f(x+3)+1=-2|x+3|+1\) has vertex \((-3,1)\), opens downward, and has range \(( -\infty,1]\).

Function notation also keeps a model's units and domain clear. If \(R(q)=50q\) and \(C(q)=120+20q\) are revenue and cost in dollars for \(q\) units, profit is \(P(q)=R(q)-C(q)=30q-120\), for feasible \(q\ge0\) (usually whole units). The break-even input solves \(P(q)=0\), namely \(q=4\).

## Practice Problems

Try these before reading the solutions. State domains whenever a function is introduced without one.

### Basic

1. Find the natural real domain of \(f(x)=\dfrac{\sqrt{x+4}}{x-2}\).
2. Find the range of \(f(x)=x^2-4\) on the stated domain \([-1,3]\).
3. Let \(h(x)=x^2\) for \(x<1\), and \(h(x)=2x+1\) for \(x\ge1\). Find \(h(-2)\), \(h(1)\), and \(h(h(-2))\).

### Intermediate

4. Let \(f(x)=\sqrt{x+2}\) and \(g(x)=1/(x-1)\), each on its natural real domain. Find \(f\circ g\) and \(g\circ f\), with the exact domain of each.
5. Let \(f(x)=(2x-3)/(x+1)\), \(x\ne-1\). Show that it is one-to-one, find its range and inverse, and verify one composition.
6. Explain why \(x^2\) has no inverse on \(\mathbb R\). Restrict its domain to make an inverse, and give that inverse's domain.
7. Describe the transformations from \(y=|x|\) to \(y=-2|x+3|+1\). State the new vertex and range.

### Exam-level and application

8. Suppose \(f:A\to B\) and \(g:B\to C\), and \(g\circ f\) is one-to-one. Prove that \(f\) is one-to-one. Give an example where \(g\circ f\) is one-to-one but \(g\) is not one-to-one on all of \(B\).
9. For \(R(q)=50q\) and \(C(q)=120+20q\), find the profit function, profit at \(q=10\), and the break-even quantity. State a reasonable domain for \(q\).

## Solutions

### 1. Natural domain

The square root needs \(x+4\ge0\), so \(x\ge-4\). The denominator needs \(x\ne2\). The domain is \([-4,2)\cup(2,\infty)\).

### 2. Range on a restricted interval

The minimum of \(x^2-4\) is \(-4\) at \(x=0\). On \([-1,3]\), the largest \(x^2\) is \(9\) at \(x=3\), giving \(5\). Continuity fills all intermediate values, so the range is \([-4,5]\).

### 3. Piecewise evaluation

Because \(-2<1\), \(h(-2)=(-2)^2=4\). Because \(1\ge1\), \(h(1)=2(1)+1=3\). Finally \(h(h(-2))=h(4)=2(4)+1=9\).

### 4. Composition domains

\[(f\circ g)(x)=\sqrt{\frac1{x-1}+2}=\sqrt{\frac{2x-1}{x-1}}.\]

Require \(x\ne1\) and \((2x-1)/(x-1)\ge0\). A sign chart at \(1/2\) and \(1\) gives \(( -\infty,1/2]\cup(1,\infty)\).

\[(g\circ f)(x)=\frac1{\sqrt{x+2}-1}.\]

Require \(x\ge-2\) and \(\sqrt{x+2}\ne1\), which excludes \(x=-1\). Its domain is \([-2,-1)\cup(-1,\infty)\).

### 5. A rational inverse

If \(f(a)=f(b)\), cross multiplication is valid for \(a,b\ne-1\):

\[(2a-3)(b+1)=(2b-3)(a+1).\]

Expanding and rearranging gives \(5a=5b\), so \(f\) is one-to-one. Solving \(y=(2x-3)/(x+1)\) gives \(x=(y+3)/(2-y)\). The value \(y=2\) is impossible, because \(2(x+1)=2x-3\) would imply \(2=-3\). Every other real \(y\) yields an allowed \(x\), so the range is \(\mathbb R\setminus\{2\}\) and

\[f^{-1}(y)=\frac{y+3}{2-y},\qquad y\ne2.\]

Checking, \(f(f^{-1}(y))=(2(y+3)-3(2-y))/((y+3)+(2-y))=5y/5=y\) for \(y\ne2\).

### 6. Domain restriction

On \(\mathbb R\), \((-2)^2=2^2\), so the rule is not one-to-one. One choice is \(f:[0,\infty)\to[0,\infty)\), \(f(x)=x^2\). Its inverse is \(f^{-1}(y)=\sqrt y\), with domain \([0,\infty)\).

### 7. Transformations

The \(x+3\) shifts left 3. The negative sign reflects across the horizontal axis, the factor 2 stretches vertical distances by 2, and the \(+1\) shifts up 1. The vertex is \((-3,1)\) and the range is \(( -\infty,1]\).

### 8. What injectivity of a composition implies

If \(f(a)=f(b)\), applying \(g\) gives \(g(f(a))=g(f(b))\). Injectivity of \(g\circ f\) then gives \(a=b\). Thus \(f\) is one-to-one.

For the converse claim about \(g\), take \(A=[0,\infty)\), \(B=C=\mathbb R\), \(f(x)=x^2\), and \(g(t)=t^2\). Then \((g\circ f)(x)=x^4\) is one-to-one for \(x\ge0\), while \(g(-1)=g(1)\). Thus \(g\) need only be one-to-one **on the image of \(f\)**.

### 9. Revenue, cost, and profit

\[\begin{aligned}P(q)&=R(q)-C(q)\\&=50q-(120+20q)\\&=30q-120.\end{aligned}\]

Hence \(P(10)=180\) dollars, and \(P(q)=0\) when \(q=4\). A reasonable domain is \(q\in\{0,1,2,\ldots\}\) if units are indivisible.

## Summary

- A function has a declared domain and codomain; its range is the set of outputs it actually attains.
- Evaluation and composition require checking which inputs are allowed. Simplifying a formula does not erase restrictions inherited from the original function.
- The inverse reverses inputs and outputs and exists on the range when the function is one-to-one.
- Horizontal changes act inside the input expression; vertical changes act on the output.

**Common mistakes:** Confusing range with codomain; treating \(f^{-1}\) as a reciprocal; composing in the wrong order; losing domain exclusions after algebraic simplification; assigning a boundary point to the wrong piece.

**What's next:** Lesson M1.5 studies polynomial, rational, and root functions in more detail, including their graph behavior.
