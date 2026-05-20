# 5–4 HIGHER-ORDER SYSTEMS

In this section we shall present a transient-response analysis of higher-order systems in general terms. It will be seen that the response of a higher-order system is the sum of the responses of first-order and second-order systems.

Transient Response of Higher-Order Systems. Consider the system shown in Figure 5–16. The closed-loop transfer function is

$$\frac {C (s)}{R (s)} = \frac {G (s)}{1 + G (s) H (s)} \tag {5-31}$$

In general, $G ( s )$ and $H ( s )$ are given as ratios of polynomials in s, or

$$G (s) = \frac {p (s)}{q (s)} \quad \text { and } \quad H (s) = \frac {n (s)}{d (s)}$$

where $p ( s ) , q ( s ) , n ( s )$ , and $d ( s )$ are polynomials in s. The closed-loop transfer function given by Equation (5–31) may then be written

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {p (s) d (s)}{q (s) d (s) + p (s) n (s)} \\ = \frac {b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \cdots + b _ {m - 1} s + b _ {m}}{a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} \quad (m \leq n) \\ \end{array}
$$

The transient response of this system to any given input can be obtained by a computer simulation. (See Section 5–5.) If an analytical expression for the transient response is desired, then it is necessary to factor the denominator polynomial. [MATLAB may be used for finding the roots of the denominator polynomial. Use the command roots(den).] Once the numerator and the denominator have been factored, $C ( s ) / R ( s )$ can be written in the form

$$\frac {C (s)}{R (s)} = \frac {K (s + z _ {1}) (s + z _ {2}) \cdots (s + z _ {m})}{(s + p _ {1}) (s + p _ {2}) \cdots (s + p _ {n})} \tag {5-32}$$

Let us examine the response behavior of this system to a unit-step input. Consider first the case where the closed-loop poles are all real and distinct. For a unit-step input, Equation (5–32) can be written

$$C (s) = \frac {a}{s} + \sum_ {i = 1} ^ {n} \frac {a _ {i}}{s + p _ {i}} \tag {5-33}$$

where $a _ { i }$ is the residue of the pole at $s = - p _ { i }$ . (If the system involves multiple poles, then $C ( s )$ will have multiple-pole terms.) [The partial-fraction expansion of $C ( s )$ , as given by Equation (5–33), can be obtained easily with MATLAB. Use the residue command. (See Appendix B.)]

If all closed-loop poles lie in the left-half s plane, the relative magnitudes of the residues determine the relative importance of the components in the expanded form of

![](image/0e439f08b9f3f08ac0bb108aa50900f9451bffc2adde00debfd18eae5ca2bad4.jpg)

<details>
<summary>flowchart</summary>
