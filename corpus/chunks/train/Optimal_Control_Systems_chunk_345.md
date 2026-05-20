$J_{02}=0.5u^{2}(0)+0.5x^{2}(0)+J_{12}^{*}(x(1))$ A strikeout (—→) indicates the value is not admissible.</td></tr></table>

![](image/459829fe7a40c351de28360c3fab55e5191fc5dc25a7b901a3478f0b45672e42.jpg)

<details>
<summary>line</summary>

| x(k) | j* | u* |
| --- | --- | --- |
| 3.25 | 0 | -1 |
| 2.25 | 1 | -0.5 |
| 2.0 | 2 | -0.5 |
| 1.125 | 2 | -0.5 |
| 1.875 | 0 | -1 |
| 1.75 | 1 | -0.5 |
| 0.75 | 0 | -0.5 |
| 0.5 | 1 | -0.5 |
| 0.125 | 2 | -0.5 |
| 0.25 | 0 | -0.5 |
| 0.25 | 1 | -0.5 |
| 0 | 0 | -0.5 |
| 0 | 1 | -0.5 |
| 0 | 2 | -0.5 |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 2 | 0 |
</details>

Figure 6.7 Dynamic Programming Framework of Optimal State Feedback Control

Then, for $x(1)=2.0$ and $u(1)=-0.5$ , when we try to use the state equation (6.3.5) to find the $x(2)=x(1)+u(1)$ , we get $x(2)=1.5$ which, although is not an allowable quantized value, is within the constraint (limit). Hence, we cannot simply calculate the quantity $J_{2}=0.5x^{2}(2)$ as $J_{2}=0.5(1.5)^{2}=1.125$ , instead using the interpolation we calculate it as

$$
\begin{array}{l} J _ {2} = 0. 5 [ x (2) = 1. 5 ] ^ {2} \\ = 0. 5 [ x (2) = 1 ] ^ {2} + \frac {0 . 5 [ x (2) = 2 ] ^ {2} - 0 . 5 [ x (2) = 1 ] ^ {2}}{2} \\ = 0. 5 + \frac {2 - 0 . 5}{2} = 1. 2 5. \tag {6.3.14} \\ \end{array}
$$

We notice that the dynamic programming technique is a computationally intensive method especially with increase in the order and the number of stages of the system. However, with the tremendous advances in high-speed computational tools since Bellman $[15]$ branded this increased computational burden inherent in dynamic programming as “curse of dimensionality,” the “curse” may be a “boon” due to the special advantages of dynamic programming in treating both linear and nonlinear systems with ease and in handling the constraints on states and/or controls.
