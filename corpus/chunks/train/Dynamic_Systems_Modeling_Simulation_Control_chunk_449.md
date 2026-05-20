# Example 8.10

Figure 8.2 shows the 1-DOF rotational mechanical system studied in Example 7.8. Determine the dynamic response ??(t) if the disk is initially at rest $( \mathrm { i . e . , ~ } \dot { \theta } ( 0 ) = 0 )$ ) with an initial angular position $\theta ( 0 ) = 0 . 1$ rad and the input torque is a step function $T _ { \mathrm { i n } } ( t ) = 2 . 5 U ( t ) \mathrm { N - m }$ .

Using the numerical parameters from Example 7.8 (moment of inertia $J = 0 . 2 \mathrm { k g } – \mathrm { m } ^ { 2 }$ , friction coefficient $b = 1 . 6 \mathrm { N - m - s / r a d }$ , and torsional spring constant k = 65 N-m/rad) the mathematical model is

$$0. 2 \ddot {\theta} + 1. 6 \dot {\theta} + 6 5 \theta = T _ {\text { in }} (t) \tag {8.26}$$

Taking the Laplace transform of each term on the left- and right-hand sides of the I/O equation (8.26) yields

$\mathrm { L e f t - h a n d ~ s i d e : ~ } \ \mathcal { L } \{ 0 . 2 \ddot { \theta } \} = 0 . 2 \big ( s ^ { 2 } \Theta ( s ) - s \theta ( 0 ) - \dot { \theta } ( 0 ) \big )$

$$\mathscr {L} \{1. 6 \dot {\theta} \} = 1. 6 (s \Theta (s) - \theta (0))\mathscr {L} \{6 5 \theta \} = 6 5 \Theta (s)$$

Right-hand side (step input): ℒ{Tin(t)} = 2.5 $\mathcal { L } \{ T _ { \mathrm { i n } } ( t ) \} = \frac { 2 . 5 } { s }$

![](image/6cf9c0f2903bcc57abd0e5c7b7583d265666435eb2aa6f2ac0ad86ee0eeeee01.jpg)

<details>
<summary>text_image</summary>

Tin(t) = 2.5U(t) N-m
J = 0.2 kg-m²
Flexible shaft,
k = 65 N-m/rad
θ
</details>

$\mathsf { F r i c t i o n } , b = 1 . 6 \mathrm { N } \mathrm { - m } \mathrm { - s } / \mathrm { r a d }$   
Figure 8.2 1-DOF rotational mechanical system for Example 8.10.

After substituting initial conditions $\theta ( 0 ) = 0 . 1$ rad and $\dot { \theta } ( 0 ) = 0$ and collecting all left- and right-hand-side Laplace transforms we obtain

$$(0. 2 s ^ {2} + 1. 6 s + 6 5) \Theta (s) - 0. 0 2 s - 0. 1 6 = \frac {2 . 5}{s} \tag {8.27}$$

or

$$(0. 2 s ^ {2} + 1. 6 s + 6 5) \Theta (s) = \frac {0 . 0 2 s ^ {2} + 0 . 1 6 s + 2 . 5}{s} \tag {8.28}$$

Solving Eq. (8.28) for the Laplace transform $\Theta ( s )$ yields

$$\Theta (s) = \frac {0 . 0 2 s ^ {2} + 0 . 1 6 s + 2 . 5}{s (0 . 2 s ^ {2} + 1 . 6 s + 6 5)} \tag {8.29}$$

Dividing all terms by 0.2 yields

$$\Theta (s) = \frac {0 . 1 s ^ {2} + 0 . 8 s + 1 2 . 5}{s (s ^ {2} + 8 s + 3 2 5)} \tag {8.30}$$

The three poles of $\Theta ( s )$ are $s = 0$ and $s = - 4 \pm j 1 7 . 5 7 8 4$ . Because two poles are complex conjugate pairs, we can “complete the square” and rewrite the corresponding second-order polynomial as

$$s ^ {2} + 8 s + 3 2 5 = (s + 4) ^ {2} + 1 7. 5 7 8 4 ^ {2}$$

Therefore, the partial-fraction expansion of Eq. (8.30) is
