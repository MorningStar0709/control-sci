# 6.2.2 Additional Necessary Conditions

In their celebrated works [109], Pontryagin and his co-workers also obtained additional necessary conditions for constrained optimal control systems. These are stated below without proof [109].

1. If the final time $t_f$ is fixed and the Hamiltonian $\mathcal{H}$ does not depend on time $t$ explicitly, then the Hamiltonian $\mathcal{H}$ must be constant when evaluated along the optimal trajectory; that is

$$\mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t)) = \text { constant } = C _ {1} \forall t \in [ t _ {0}, t _ {f} ]. \tag {6.2.30}$$

![](image/ff85022209d2c7b85f5818b57fcf41a5ab392ff19ec1298b25b3aab48775e4f6.jpg)

<details>
<summary>line</summary>

| u | H(u) |
| --- | --- |
| -1 | 7 |
| 0 | 0 |
| 1 | -2 |
| 2 | -2 |
| 3 | -2 |
| 4 | -1 |
| 5 | 2 |
| 6 | 7 |
</details>

Figure 6.2 Illustration of Constrained (Admissible) Controls

2. If the final time $t_{f}$ is free or not specified priori and the Hamiltonian does not depend explicitly on time t, then the Hamiltonian must be identically zero when evaluated along the optimal trajectory; that is,

$$\mathcal {H} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t)) = 0 \forall t \in [ t _ {0}, t _ {f} ] \tag {6.2.31}$$

Further treatment of constrained optimal control systems is carried out in Chapter 7. According to Gregory and Lin [61] the credit for formulating the optimal control problem for the first time in 1950 is given to M. R. Hestenes [64], the detailed proof of the problem was given by a group of Russian mathematicians led by Pontryagin and hence called the Pontryagin Minimum Principle (PMP) [109]. The PMP is the heart of the optimal control theory. However, the original proof given by Pontryagin et al. is highly rigorous and lengthy. There are several books devoting lengthy proof of PMP such as Athans and Falb [6], Lee and Markus [86] and Machki and Strauss [97]. Also see recent books (Pinch [108] and Hocking [66]) for a simplified treatment of the proof.
