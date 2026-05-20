# 5.4 Steady-State Regulator System

Here, we let $k_{f}$ tend to $\infty$ and this necessitates that we assume the time-invariant case. Thus, the linear time-invariant plant becomes

$$x (k + 1) = \mathbf {A} x (k) + \mathbf {B} u (k) \tag {5.4.1}$$

and the performance index becomes

$$J = \frac {1}{2} \sum_ {k = k _ {0}} ^ {\infty} \left[ \mathbf {x} ^ {* \prime} (k) \mathbf {Q} \mathbf {x} (k) + \mathbf {u} ^ {* \prime} (k) \mathbf {R} \mathbf {u} ^ {*} (k) \right]. \tag {5.4.2}$$

As the final time $k_{f}$ tends to $\infty$ , we have the Riccati matrix $\mathbf{P}(k)$ attaining a steady-state value $\bar{P}$ in (5.3.11). That is,

$$\mathbf {P} (k) = \mathbf {P} (k + 1) = \bar {\mathbf {P}} \tag {5.4.3}$$

![](image/53de718704301b131d3b24f46c66d26019cc5ebc36b0eb47f0ee3e3d06c66797.jpg)

<details>
<summary>line</summary>

| k | x₁(k) | x₂(k) |
| --- | --- | --- |
| 0 | 5.0 | 3.0 |
| 1 | 2.9 | -0.3 |
| 2 | 1.1 | -0.6 |
| 3 | 0.3 | -0.4 |
| 4 | 0.0 | -0.1 |
| 5 | 0.0 | 0.0 |
| 6 | 0.0 | 0.0 |
| 7 | 0.0 | 0.0 |
| 8 | 0.0 | 0.0 |
| 9 | 0.0 | 0.0 |
| 10 | 0.0 | 0.0 |
</details>

Figure 5.4 Optimal Control and States for Example 5.3

resulting in the algebraic Riccati equation (ARE) as

$$\boxed {\bar {\mathbf {P}} = \mathbf {A} ^ {\prime} \bar {\mathbf {P}} \left[ \mathbf {I} + \mathbf {B R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \right] ^ {- 1} \mathbf {A} + \mathbf {Q}} \tag {5.4.4}$$

or (5.3.12) as

$$\bar {\mathbf {P}} = \mathbf {A} ^ {\prime} \left[ \bar {\mathbf {P}} ^ {- 1} + \mathbf {E} \right] ^ {- 1} \mathbf {A} + \mathbf {Q}$$

where, $\mathbf{E} = \mathbf{B}\mathbf{R}^{-1}\mathbf{B}'$ . The feedback optimal control (5.3.15) becomes

$$\boxed {\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {A} ^ {- T} [ \bar {\mathbf {P}} - \mathbf {Q} ] \mathbf {x} ^ {*} (k) = - \bar {\mathbf {L}} \mathbf {x} ^ {*} (k)} \tag {5.4.5}$$

where, the Kalman gain (5.3.17) becomes

$$\boxed {\bar {\mathbf {L}} = \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {A} ^ {- T} [ \bar {\mathbf {P}} - \mathbf {Q} ]} \tag {5.4.6}$$

![](image/b577db1927b342dbf0247b9b178f809da8375ebc2f865f39203eb50c4e735f2e.jpg)

<details>
<summary>line</summary>

| k | Optimal Control |
| --- | --- |
| 0 | -4.2 |
| 1 | -1.0 |
| 2 | 0.0 |
| 3 | 0.1 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

Figure 5.5 Optimal Control and States for Example 5.3

and $A^{-T}$ is the inverse of $A'$ .
