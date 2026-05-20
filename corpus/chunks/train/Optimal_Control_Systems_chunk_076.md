# 2.3.1 Fixed-End Time and Fixed-End State System

We address a fixed-end time and fixed-end state problem, where both the initial time and state and the final time and state are fixed or given a priori. Let $x(t)$ be a scalar function with continuous first derivatives and the vector case can be similarly dealt with. The problem is to find the optimal function $x^{*}(t)$ for which the functional

$$J (x (t)) = \int_ {t _ {0}} ^ {t _ {f}} V (x (t), \dot {x} (t), t) d t \tag {2.3.1}$$

has a relative optimum. It is assumed that the integrand V has continuous first and second partial derivatives w.r.t. all its arguments; $t_{0}$ and $t_{f}$ are fixed (or given a priori) and the end points are fixed, i.e.,

$$x (t = t _ {0}) = x _ {0}; \quad x (t = t _ {f}) = x _ {f}. \tag {2.3.2}$$

We already know from Theorem 2.1 that the necessary condition for an optimum is that the variation of a functional vanishes. Hence, in our attempt to find the optimum of $x(t)$ , we first define the increment for $J$ , obtain its variation and finally apply the fundamental theorem of the calculus of variations (Theorem 2.1).

Thus, the various steps involved in finding the optimal solution to the fixed-end time and fixed-end state system are first listed and then discussed in detail.

- Step 1: Assumption of an Optimum   
- Step 2: Variations and Increment   
- Step 3: First Variation   
- Step 4: Fundamental Theorem   
- Step 5: Fundamental Lemma   
- Step 6: Euler-Lagrange Equation

\- Step 1: Assumption of an Optimum: Let us assume that $x^{*}(t)$ is the optimum attained for the function $x(t)$ . Take some admissible function $x_{a}(t) = x^{*}(t) + \delta x(t)$ close to $x^{*}(t)$ , where $\delta x(t)$ is the variation of $x^{*}(t)$ as shown in Figure 2.4. The function $x_{a}(t)$ should also satisfy the boundary conditions (2.3.2) and hence it is necessary that

$$\delta x (t _ {0}) = \delta x (t _ {f}) = 0. \tag {2.3.3}$$

![](image/83e6f874bebc64da320698ae5be8dc45aa35e6ffcbb547c09d919919b110e962.jpg)

<details>
<summary>line</summary>

| t | x*(t) | x*(t)+δx(t) |
| --- | --- | --- |
| t₀ | x₀ | x₀ |
| t_f | x_f | x_f |
</details>

Figure 2.4 Fixed-End Time and Fixed-End State System

\- Step 2: Variations and Increment: Let us first define the increment as
