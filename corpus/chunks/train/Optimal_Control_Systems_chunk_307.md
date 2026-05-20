# 5.6 Frequency-Domain Interpretation

This section is based on $[89]$ . In this section, we use frequency domain to derive some results from the classical control point of view for a linear, time-invariant, discrete-time, optimal control system with infinite-time case, described earlier in Section 5.4. For this, we know that the optimal control involves the solution of matrix algebraic Riccati equation. For ready reference, we reproduce here results of the time-invariant case described earlier in this chapter. For the plant

$$\mathbf {x} (k + 1) = \mathbf {A x} (k) + \mathbf {B u} (k), \tag {5.6.1}$$

the optimal feedback control is

$$\mathbf {u} ^ {*} (k) = - \bar {\mathbf {L}} \mathbf {x} ^ {*} (k) \tag {5.6.2}$$

![](image/0ebfb07e7cfb66fd306176800367d803d136a561257b1e0074787f9432715445.jpg)

<details>
<summary>line</summary>

| k | Riccati Coefficients |
| --- | --- |
| 0 | 1.0 |
| 1 | 1.0 |
| 2 | 1.0 |
| 3 | 1.0 |
| 4 | 1.0 |
| 5 | 1.0 |
| 6 | 1.0 |
| 7 | 1.0 |
| 8 | 1.0 |
| 9 | 1.0 |
| 10 | 1.0 |
</details>

Figure 5.13 Riccati Coefficients for Example 5.6

where,

$$\bar {\mathbf {L}} = \left[ \bar {\mathbf {B}} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} \right] ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {A}. \tag {5.6.3}$$

Rewriting the above by postmultiplying by $[B^{\prime}\bar{P}B + R]$

$$\left[ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} \right] \bar {\mathbf {L}} = \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {A}. \tag {5.6.4}$$

Here, $\bar{P}$ is the solution of the ARE

$$\bar {\mathbf {P}} = \mathbf {A} ^ {\prime} \left[ \bar {\mathbf {P}} - \bar {\mathbf {P}} \mathbf {B} \left[ \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {B} + \mathbf {R} \right] ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \right] \mathbf {A} + \mathbf {Q} \tag {5.6.5}$$

where, we assume that $[A,B]$ is stabilizable and $[A,\sqrt{Q}]$ is observable. With this optimal control (5.6.2), the optimal system becomes

$$\mathbf {x} ^ {*} (k + 1) = \left[ \mathbf {A} - \mathbf {B} \bar {\mathbf {L}} \right] \mathbf {x} ^ {*} (k) \tag {5.6.6}$$

and is asymptotically stable. Here, the open-loop characteristic polynomial of the system is

$$\boldsymbol {\Delta} _ {o} (z) = | z \mathbf {I} - \mathbf {A} | \tag {5.6.7}$$

![](image/b585828e95059219d958832bfd7b77bfe4fef3709aea0bb458e423d9f07f5690.jpg)

<details>
<summary>line</summary>
