# Problems

1. Make reasonable assumptions wherever necessary.

2. Use MATLAB $^{\text{©}}$ wherever possible to solve the problems and plot all the optimal controls and states for all problems. Provide the relevant MATLAB $^{\text{©}}$ $m$ files.

Problem 6.1 Prove the Pontryagin Minimum Principle based on the works of Athans and Falb [6], Lee and Markus [86], Machki and Strauss [97] and some of the recent works Pinch [108] and Hocking [66].

Problem 6.2 For the general case of the Example 6.2, develop a MATLAB $^{©}$ based program.

Problem 6.3 For a traveling salesperson, find out the cheapest route from city L to city N if the total costs between the intermediate cities are shown in Figure 6.8.

Problem 6.4 Consider a scalar example

$$x (k + 1) = x (k) + u (k) \tag {6.6.1}$$

and the performance criterion to be optimized as

$$
\begin{array}{l} J = \frac {1}{2} x ^ {2} (k _ {f}) + \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} u ^ {2} (k) \\ = \frac {1}{2} x ^ {2} \left(k _ {f}\right) + \frac {1}{2} u ^ {2} (0) + \frac {1}{2} u ^ {2} (1) \\ \end{array}
$$

where, for simplicity of calculations we take $k_{f} = 2$ . Let the constraints on the control be

$$
\begin{array}{l} - 1. 0 \leq u (k) \leq + 1. 0, k = 0, 1, 2 \quad \text {or} \\ u (k) = - 1. 0, \quad - 0. 5, \quad 0, \quad + 0. 5, \quad + 1. 0 \\ \end{array}
$$

and on the state be

$$
\begin{array}{l} 0. 0 \leq x (k) \leq + 1. 0, k = 0, 1 \quad \text {or} \\ x (k) = 0. 0, \quad 0. 5, \quad 1. 0, \quad 1. 5. \\ \end{array}
$$

Find the optimal control sequence $u^{*}(k)$ and the state $x^{*}(k)$ which minimize the performance criterion.

![](image/fd2e01ba04bfff0c25dc10599a6dc86e71b69ff5b6f81a7496abb102bb0222b2.jpg)

<details>
<summary>text_image</summary>

E
4 7
C 6 H
3 3 3
L F N
2 7 2 4
D I
8 5
G
</details>

Figure 6.8 Optimal Path from A to B

Problem 6.5 Find the Hamilton-Jacobi-Bellman equation for the system

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = - 2 x _ {2} (t) - 3 x _ {1} ^ {2} (t) + u (t)$$

with the performance index as

$$J = \frac {1}{2} \int_ {0} ^ {t _ {f}} \left(x _ {1} ^ {2} (t) + u ^ {2} (t)\right) d t.$$

Problem 6.6 Solve the Example 5.3 using dynamic programming approach.

Problem 6.7 For the D.C. motor speed control system described in Problem 1.1, find the HJB equation and hence the closed-loop optimal control to keep the speed at a constant value.

Problem 6.8 For the liquid-level control system described in Problem 1.2, find the HJB equation and hence the closed-loop optimal control to keep the liquid level constant at a particular value.

Problem 6.9 For the mechanical control system described in Problem 1.4, find the HJB equation and hence the closed-loop optimal control to keep the states at a constant value.

Problem 6.10 For the automobile suspension system described in Problem 1.5, find the HJB equation and hence the closed-loop control.

@@@@@@@@@@
