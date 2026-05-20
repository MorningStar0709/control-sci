# 5.4.3 Controlling x and xˆ

As before, we use MPC to control the state estimator and the system $x ^ { + } = A x + B u$ by controlling the nominal system

$$z ^ {+} = A z + B \nu$$

![](image/08f3d79161145b00f055c4b462dcca536a58aefc10900bc3116640a7680a13ee.jpg)

<details>
<summary>text_image</summary>

e
S(i)
Φ(i)
Σ(i)
x̃
</details>

Figure 5.3: The sets Φ(i), Σ(i) and $\mathbb { S } ( i )$ .

and setting $u = \nu + K e , e : = \hat { x } - z$ . With this control, the composite system whose state is $\phi : = ( \tilde { x } , e )$ satisfies

$$\tilde {x} ^ {+} = A _ {L} \tilde {x} + w - L v \qquad w \in \mathbb {W}e ^ {+} = A _ {K} e + L C \tilde {x} + L v \qquad v \in \mathbb {N}$$

where $A _ { K } : = A + B K$ . The difference equations for the composite system may be written in the more compact form

$$\phi^ {+} = \tilde {A} \phi + \tilde {B} \psi$$

where the composite state $\phi : = ( \tilde { x } , e )$ lies in $\mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ and the bounded disturbance $\psi : = ( w , \nu )$ lies in the constant compact set $\Psi : = \mathbb { W } \times \mathbb { N } ;$ ; the state matrix $\tilde { A }$ and the disturbance matrix $\tilde { B }$ are defined by

$$
\widetilde {A} = \left[ \begin{array}{c c} A _ {L} & 0 \\ L C & A _ {K} \end{array} \right] \qquad \widetilde {B} = \left[ \begin{array}{c c} I & - L \\ 0 & L \end{array} \right]
$$

We assume that K and L are such that $\rho ( A _ { K } ) < 1$ and $\rho ( A _ { L } ) < 1$ ; hence $\rho ( \tilde { \boldsymbol { A } } ) < 1$ . Consider the set sequence $\{ \Phi ( i ) \}$ defined by

$$\Phi (i + 1) = \tilde {A} \Phi (i) \oplus \tilde {B} \Psi$$
