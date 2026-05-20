# 6–4 ROOT-LOCUS PLOTS OF POSITIVE FEEDBACK SYSTEMS

Root Loci for Positive-Feedback Systems.\* In a complex control system, there may be a positive-feedback inner loop as shown in Figure 6–30. Such a loop is usually stabilized by the outer loop. In what follows, we shall be concerned only with the positivefeedback inner loop. The closed-loop transfer function of the inner loop is

$$\frac {C (s)}{R (s)} = \frac {G (s)}{1 - G (s) H (s)}$$

The characteristic equation is

$$1 - G (s) H (s) = 0 \tag {6-17}$$

Figure 6–30 Control system.   
![](image/73aeb5983d0d16cbcc0066f538383379a6eb4817e97e6f43f43e6a37bb988d6d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["G₁(s)"]
    B --> C["R(s)"]
    C --> D["+"]
    D --> E["G(s)"]
    E --> F["C(s)"]
    F --> G["H(s)"]
    G --> H["H₁(s)"]
    H --> I["Feedback to A"]
    I --> A
```
</details>

This equation can be solved in a manner similar to the development of the root-locus method for negative-feedback systems presented in Section 6–2. The angle condition, however, must be altered.

Equation (6–17) can be rewritten as

$$G (s) H (s) = 1$$

which is equivalent to the following two equations:

$$\underline {{{G (s) H (s)}}} = 0 ^ {\circ} \pm k 3 6 0 ^ {\circ} \quad (k = 0, 1, 2, \dots)| G (s) H (s) | = 1$$

For the positive-feedback case, the total sum of all angles from the open-loop poles and zeros must be equal to $0 ^ { \circ } \pm k 3 6 0 ^ { \circ }$ Thus the root locus follows a. $0 ^ { \circ }$ locus in contrast to the 180° locus considered previously. The magnitude condition remains unaltered.

To illustrate the root-locus plot for the positive-feedback system, we shall use the following transfer functions G(s) and H(s) as an example.

$$G (s) = \frac {K (s + 2)}{(s + 3) (s ^ {2} + 2 s + 2)}, \quad H (s) = 1$$

The gain K is assumed to be positive.

The general rules for constructing root loci for negative-feedback systems given in Section 6–2 must be modified in the following way:

Rule 2 is Modified as Follows: If the total number of real poles and real zeros to the right of a test point on the real axis is even, then this test point lies on the root locus.

Rule 3 is Modified as Follows:

$$\text { Angles of asymptotes } = \frac {\pm k 3 6 0 ^ {\circ}}{n - m} \quad (k = 0, 1, 2, \dots)$$

where number of finite poles of  n = $G ( s ) H ( s )$

$$m = \text { number of finite zeros of } G (s) H (s)$$
