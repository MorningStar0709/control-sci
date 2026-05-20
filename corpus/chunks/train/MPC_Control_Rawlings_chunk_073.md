# Example 1.1: Sum of quadratic functions

Consider the two quadratic functions given by

$$V _ {1} (x) = (1 / 2) (x - a) ^ {\prime} A (x - a) \quad V _ {2} (x) = (1 / 2) (x - b) ^ {\prime} B (x - b)$$

in which A, $B > 0$ are positive definite matrices and a and b are nvectors locating the minimum of each function. Figure 1.3 displays the ellipses defined by the level sets $V _ { 1 } ( x ) = 1 / 4$ and $V _ { 2 } ( x ) = 1 / 4$ for the following data

![](image/6c59a6b3f2fe2032ac434be46a84bc2ac75f031e8d3ce87b76ebc26f06040345.jpg)

<details>
<summary>scatter</summary>

| Point | x1 | x2 |
| --- | --- | --- |
| a | -1.0 | 0.0 |
| v | 0.0 | 0.0 |
| b | 1.0 | 1.0 |
</details>

Figure 1.3: Two quadratic functions and their sum; $V ( x ) = V _ { 1 } ( x ) +$ $V _ { 2 } ( x )$ .

$$
A = \left[ \begin{array}{c c} 1. 2 5 & 0. 7 5 \\ 0. 7 5 & 1. 2 5 \end{array} \right] \qquad a = \left[ \begin{array}{c} - 1 \\ 0 \end{array} \right]

B = \left[ \begin{array}{l l} 1. 5 & - 0. 5 \\ - 0. 5 & 1. 5 \end{array} \right] \qquad b = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right]
$$

(a) Show that the sum $V ( x ) = V _ { 1 } ( x ) + V _ { 2 } ( x )$ is also quadratic

$$V (x) = (1 / 2) (x - v) ^ {\prime} H (x - v) + \text { constant }$$

in which

$$H = A + B \quad v = H ^ {- 1} (A a + B b)$$

and verify the three ellipses given in Figure 1.3.

(b) Consider a generalization useful in the discussion of the upcoming state estimation problem. Let

$$V _ {1} (x) = (1 / 2) (x - a) ^ {\prime} A (x - a) \quad V _ {2} (x) = (1 / 2) (C x - b) ^ {\prime} B (C x - b)$$

Derive the formulas for H and v for this case.

(c) Use the matrix inversion lemma (see Exercise 1.12) and show that V (x) can be expressed also in an inverse form, which is useful in state estimation problems

$$V (x) = (1 / 2) (x - v) ^ {\prime} \tilde {H} ^ {- 1} (x - v) + \text { constant }\tilde {H} = A ^ {- 1} - A ^ {- 1} C ^ {\prime} (C A ^ {- 1} C ^ {\prime} + B ^ {- 1}) ^ {- 1} C A ^ {- 1}\nu = a + A ^ {- 1} C ^ {\prime} \left(C A ^ {- 1} C ^ {\prime} + B ^ {- 1}\right) ^ {- 1} (b - C a)$$
