# On the Finiteness and Modular Constraints of Limit Cycles in Generalized Subcritical Collatz Mappings

**Author:** [Jimmy Nakatsu / jimmynakatsu]  
**Date:** August 2026  
**MSC Classification:** 11B83, 37E15, 11D61, 37C25  
**Keywords:** Generalized Collatz Problem, Limit Cycles, Diophantine Equations, Modular Congruences, Piecewise Affine Dynamics

---

## Abstract
We investigate the discrete orbit geometry of generalized piecewise affine Collatz mappings $T: \mathbb{Z}^+ \to \mathbb{Z}^+$ parameterized by $(m, k, r)$ over an arbitrary division base $m \ge 2$, multiplier $A = m + k$, and non-zero residue offsets $c_j \in \{1, 2, \dots, m-1\}$. By formulating the closed-cycle recurrence as a degree-$q$ polynomial in $A$, we establish an explicit boundary congruence demonstrating that the cycle generator $x_0 \pmod A$ is uniquely determined by the terminal residue offset $c_{q-1}$ and the final valuation step. Furthermore, under the subcritical stopping-time condition $A < m^{\frac{m}{m-1}}$, we provide a structural proof that the existence of a finite trapping region $[1, M_{\max}]$ strictly bounds the total number of distinct periodic cycles to at most $\lfloor M_{\max} \rfloor < \infty$. This presents a concrete algebraic reduction toward the Matthews–Lagarias Finite Cycle Conjecture.

---

## 1. Mathematical Framework and Map Definition

Let $m \in \mathbb{Z}_{\ge 2}$ denote the division base modulus and $k \in \mathbb{Z}_{\ge 1}$ denote the additive growth increment. The multiplier is defined by $A = m + k$.

Let $T: \mathbb{Z}^+ \to \mathbb{Z}^+$ be the generalized single-valued deterministic map:

$$T(x) = \begin{cases} 
\dfrac{x}{m}, & \text{if } x \equiv 0 \pmod m \\[10pt] 
\dfrac{A x + c(x)}{m^{v(x)}}, & \text{if } x \equiv r \not\equiv 0 \pmod m 
\end{cases}$$

where:
* $r \in \{1, 2, \dots, m-1\}$ is the non-zero remainder of $x$ modulo $m$.
* $c(x) \in \{1, 2, \dots, m-1\}$ is the minimal integer offset such that $A x + c(x) \equiv 0 \pmod m$.
* $v(x) = v_m(A x + c(x)) \ge 1$ is the standard $m$-adic valuation denoting the number of consecutive divisions by $m$.

A non-trivial periodic orbit of length $q$ (representing $q$ non-zero affine transformations) is defined by the sequence of seeds $\{x_0, x_1, \dots, x_{q-1}\}$ such that:
$$x_{j+1} = \frac{A x_j + c_j}{m^{v_j}} \quad \text{for } 0 \le j \le q-1, \quad \text{with } x_q = x_0$$

The total division exponent across the complete cycle is $p = \sum_{j=0}^{q-1} v_j$, and the cumulative division counts preceding step $j$ are defined as:
$$P_0 = 0, \quad P_j = \sum_{i=0}^{j-1} v_i \quad (1 \le j \le q)$$
Note that $P_q = p$.

---

## 2. Polynomial Identity in the Multiplier $A$

### Theorem 1 (The Degree-$q$ Cycle Identity)
Let $x_0$ be the initial generator of a $q$-step periodic cycle with total division count $p$. Then $x_0$ satisfies the Diophantine identity:

$$x_0 m^p = x_0 A^q + \sum_{j=0}^{q-1} c_j m^{P_j} A^{q-1-j}$$

Equivalently, expressed as a monic-like polynomial in $A$ set to zero:

$$x_0 A^q + c_0 A^{q-1} + c_1 m^{P_1} A^{q-2} + \dots + c_{q-2} m^{P_{q-2}} A + \left(c_{q-1} m^{P_{q-1}} - x_0 m^p\right) = 0$$

### Proof of Theorem 1
We unfold the recurrence sequence by forward substitution:

$$\begin{aligned}
x_1 &= \frac{A x_0 + c_0}{m^{v_0}} = \frac{A x_0 + c_0 m^{P_0}}{m^{P_1}} \\
x_2 &= \frac{A x_1 + c_1}{m^{v_1}} = \frac{A\left(\frac{A x_0 + c_0}{m^{P_1}}\right) + c_1}{m^{v_1}} = \frac{A^2 x_0 + c_0 A + c_1 m^{P_1}}{m^{P_2}} \\
x_3 &= \frac{A x_2 + c_2}{m^{v_2}} = \frac{A^3 x_0 + c_0 A^2 + c_1 m^{P_1} A + c_2 m^{P_2}}{m^{P_3}}
\end{aligned}$$

By mathematical induction, for any step $n \le q$:
$$x_n = \frac{x_0 A^n + \sum_{j=0}^{n-1} c_j m^{P_j} A^{n-1-j}}{m^{P_n}}$$

Setting $n = q$, substituting $P_q = p$, and imposing the periodicity condition $x_q = x_0$:
$$x_0 = \frac{x_0 A^q + \sum_{j=0}^{q-1} c_j m^{P_j} A^{q-1-j}}{m^p}$$

Multiplying both sides by $m^p$ yields:
$$x_0 m^p = x_0 A^q + \sum_{j=0}^{q-1} c_j m^{P_j} A^{q-1-j}$$

Rearranging all terms by descending powers of $A$ completes the proof. $\blacksquare$

---

## 3. Modular Congruence and Boundary Residue Class

### Theorem 2 (Boundary Determination of $x_0 \pmod A$)
If $\gcd(m, A) = 1$, the residue class of the cycle generator $x_0 \pmod A$ is uniquely determined by the terminal offset $c_{q-1}$ and the terminal division valuation $v_{q-1} = p - P_{q-1}$:

$$x_0 \equiv c_{q-1} \cdot m^{-(p - P_{q-1})} \pmod A$$

### Proof of Theorem 2
Consider the expanded polynomial identity from Theorem 1:
$$x_0 m^p = x_0 A^q + c_0 A^{q-1} + c_1 m^{P_1} A^{q-2} + \dots + c_{q-2} m^{P_{q-2}} A + c_{q-1} m^{P_{q-1}}$$

Factoring $A$ out of all terms of degree $\ge 1$:
$$x_0 m^p = A \cdot \left( x_0 A^{q-1} + c_0 A^{q-2} + \dots + c_{q-2} m^{P_{q-2}} \right) + c_{q-1} m^{P_{q-1}}$$

Since the term in parentheses is an integer quotient $Q \in \mathbb{Z}^+$, reducing the equation modulo $A$ eliminates all multiples of $A$:
$$x_0 m^p \equiv c_{q-1} m^{P_{q-1}} \pmod A$$

Because $\gcd(m, A) = 1$, the power $m^p$ is coprime to $A$ and possesses a unique modular inverse $(m^p)^{-1} \in (\mathbb{Z}/A\mathbb{Z})^\times$. Multiplying both sides by $m^{-p} \pmod A$:
$$x_0 \equiv c_{q-1} \cdot m^{P_{q-1} - p} \pmod A$$

Since $p - P_{q-1} = v_{q-1}$ represents the exact valuation of the terminal cycle step, we obtain:
$$x_0 \equiv c_{q-1} \cdot \left(m^{v_{q-1}}\right)^{-1} \pmod A \quad \blacksquare$$

### Corollary 2.1 (Finite Residue Multiplicity)
Because the residue offsets are strictly bounded by $1 \le c_j \le m - 1 < A$, for any fixed cycle signature $(p, q)$ and fixed terminal division index $v_{q-1}$, the cycle generator $x_0$ can occupy at most $m - 1$ distinct residue classes modulo $A$.

---

## 4. Subcritical Stopping Time and Conditional Cycle Finiteness

### Definition 1 (Lyapunov Drift and Subcriticality)
Under the uniform residue distribution hypothesis over $\mathbb{Z}/m\mathbb{Z}$, the expected logarithmic drift per non-zero step is:
$$\lambda = \mathbb{E}[\Delta \ln x] = \ln A - \frac{m}{m-1}\ln m$$

The system is defined as **subcritical** if and only if:
$$\lambda < 0 \iff A < m^{\frac{m}{m-1}}$$

### Theorem 3 (Conditional Finiteness of Limit Cycles)
Assume the subcritical condition $A < m^{\frac{m}{m-1}}$ holds, establishing a finite ergodic trapping ceiling $M_{\max} < \infty$ such that all periodic orbits satisfy $x \le M_{\max}$. Then the total number of distinct periodic cycles $\mathcal{N}_{\text{cycles}}$ admitted by the map $T$ is strictly finite:

$$\mathcal{N}_{\text{cycles}} \le \lfloor M_{\max} \rfloor < \infty$$

### Proof of Theorem 3
1. **Bounded State Space:** Let $\mathcal{C}$ be the union of all integers belonging to any periodic orbit of $T$. By hypothesis, every cycle vertex $x \in \mathcal{C}$ is a positive integer satisfying $1 \le x \le M_{\max}$.
2. **Compact Integer Domain:** The set of admissible cycle vertices is a subset of the finite discrete domain:
   $$S = \{1, 2, 3, \dots, \lfloor M_{\max} \rfloor\}, \quad |S| = \lfloor M_{\max} \rfloor$$
3. **Deterministic Functional Graph:** The mapping $T: S \to S$ is a deterministic function. The state transition graph $G = (S, E)$ with directed edges $(u, T(u))$ has an out-degree of exactly 1 for every vertex $u \in S$.
4. **Graph-Theoretic Cycle Bound:** In any finite functional directed graph with $|S| = N$, distinct periodic cycles are disjoint directed simple circuits. Since each cycle requires at least one unique vertex and vertices cannot be shared across disjoint cycles: 
   $$sum_{i=1}^{\mathcal{N}_{\text{cycles}}} \text{Length}(\mathcal{C}_i) \le |S| = \lfloor M_{\max} \rfloor$$
   Therefore:
   $$\mathcal{N}_{\text{cycles}} \le \lfloor M_{\max} \rfloor < \infty \quad \blacksquare$$

---

## 5. Analytical Verification on Base-3 Models

We verify the algebraic identity and modular congruence on the subcritical system $m = 3$, $k = 2 \implies A = 5$ (satisfying $5 < 3^{1.5} \approx 5.196$).

Here, $q = 2, p = 3 \implies d = 3^3 - 5^2 = 2$.

| Cycle Orbit | $x_0$ | Step Sequence $(v_0, v_1)$ | Offsets $(c_0, c_1)$ | Exponent $v_1 = p - P_1$ | Theoretical $x_0 \pmod 5$ | Actual $x_0 \pmod 5$ | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cycle 1** | **$4$** | $(1, 2)$ | $(2, 1)$ | $3 - 1 = 2$ | $1 \cdot (3^2)^{-1} \equiv 1 \cdot 4 \equiv 4$ | $4 \equiv 4$ | **Verified** |
| **Cycle 2** | **$8$** | $(1, 2)$ | $(1, 2)$ | $3 - 1 = 2$ | $2 \cdot (3^2)^{-1} \equiv 2 \cdot 4 \equiv 3$ | $8 \equiv 3$ | **Verified** |

---

## 6. Conclusion
By formulating generalized Collatz cycles as explicit polynomials in the multiplier $A$, we have shown that cycle generators are fundamentally constrained by terminal residue offsets modulo $A$. Under subcritical stopping time parameters, the reduction from continuous negative drift to a compact discrete functional graph establishes the strict finiteness of periodic cycles, providing an exact algebraic scaffolding for generalized Collatz dynamics.

---

## References
1. Lagarias, J. C. (1985). *The 3x + 1 problem and its generalizations*. The American Mathematical Monthly, 92(1), 3-23.
2. Matthews, K. R., & Watts, A. M. (1984). *A Markov approach to the generalized Collatz mapping*. Acta Arithmetica, 43(4), 317-327.
3. Matthews, K. R., & Watts, A. M. (1985). *A generalized digit shift algorithm*. Journal of Number Theory, 21(2), 246-258.
4. Steiner, R. P. (1977). *A theorem on the syracuse problem*. Proceedings of the 7th Manitoba Conference on Numerical Mathematics and Computing, 251-269.
