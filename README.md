# On the Finiteness and Modular Constraints of Limit Cycles in Generalized Subcritical Collatz Mappings

## Abstract
We investigate the periodic orbit structure of generalized affine Collatz mappings $T: \mathbb{Z}^+ \to \mathbb{Z}^+$ parameterized by $(m, k, r)$ with division base $m \ge 2$, multiplier $A = m + k$, and residue offsets $c_j \in \{1, \dots, m-1\}$. By expanding the cyclic recurrence relation into a degree-$q$ polynomial in $A$, we derive an explicit modular congruence relating the cycle generator $x_0$ to the terminal residue offset $c_{q-1}$. Under the subcritical stopping-time threshold $A < m^{\frac{m}{m-1}}$, the existence of a compact trapping region $[1, M_{\max}]$ implies the strict finiteness of the cycle set.

---

## 1. System Definition

Let $m \in \mathbb{Z}_{\ge 2}$ and $k \in \mathbb{Z}^+$. Define the piecewise affine map $T: \mathbb{Z}^+ \to \mathbb{Z}^+$:

$$T(x) = \begin{cases} \dfrac{x}{m}, & \text{if } x \equiv 0 \pmod m \\[8pt] \dfrac{A x + c(r)}{m^{v(x)}}, & \text{if } x \equiv r \not\equiv 0 \pmod m \end{cases}$$

where:
* $A = m + k$ is the multiplier.
* $c(r) \in \{1, 2, \dots, m-1\}$ is the minimal integer offset ensuring $A x + c(r) \equiv 0 \pmod m$.
* $v(x) = v_m(A x + c(r))$ is the $m$-adic valuation.

---

## 2. Algebraic Cycle Identity

**Theorem 1.** Let $x_0$ generate a periodic cycle with $q$ multiplication steps, total division power $p$, and intermediate cumulative division counts $P_j = \sum_{i=0}^{j-1} v_i$ (with $P_0 = 0$). Then $x_0$ satisfies:

$$x_0 m^p = x_0 A^q + \sum_{j=0}^{q-1} c_j m^{P_j} A^{q-1-j}$$

Equivalently, the polynomial identity in $A$ is:

$$x_0 A^q + c_0 A^{q-1} + c_1 m^{P_1} A^{q-2} + \dots + c_{q-2} m^{P_{q-2}} A + (c_{q-1} m^{P_{q-1}} - x_0 m^p) = 0$$

---

## 3. Modular Congruence on $x_0$

**Theorem 2.** If $\gcd(m, A) = 1$, the cycle generator $x_0$ is uniquely constrained modulo $A$ by the terminal offset $c_{q-1}$:

$$x_0 \equiv c_{q-1} \cdot m^{-(p - P_{q-1})} \pmod A$$

**Corollary.** Because $1 \le c_{q-1} \le m - 1$, for any fixed signature $(p, q)$ and terminal division count $v_{q-1} = p - P_{q-1}$, the cycle head $x_0$ belongs to at most $m - 1$ distinct residue classes modulo $A$.

---

## 4. Conditional Finiteness Theorem

**Definition.** The system is subcritical if its geometric mean drift factor satisfies:

$$\rho = \frac{A^{\frac{m-1}{m}}}{m} < 1 \iff A < m^{\frac{m}{m-1}}$$

**Theorem 3.** Under the subcritical drift condition, assuming an ergodic trapping ceiling $x \le M_{\max} < \infty$, the total number of distinct periodic cycles $\mathcal{N}_{\text{cycles}}$ is strictly finite:

$$\mathcal{N}_{\text{cycles}} \le \lfloor M_{\max} \rfloor < \infty$$# Generalized-Collatz-Cycles
