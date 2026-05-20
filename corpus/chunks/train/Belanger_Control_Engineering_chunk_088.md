# Example 3.4 (Sprung Beam)

Calculate eigenvalues and eigenvectors for the beam on springs of Example 2.10 in Chapter 2 (see Fig. 3.4) with D = 0, L = 1 m, M = 2 kg, J = .167 kg m $^{2}$ , K = 50 N/m. Study the motion that results when the initial state is a linear combination of the real and imaginary parts of a complex eigenvector.

Solution From Example 2.10, the state equations, with zero input, are

$$
\frac {d}{d t} \left[ \begin{array}{c} y \\ v \\ \theta \\ \omega \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - 5 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 1 5 0 & 0 \end{array} \right] \left[ \begin{array}{c} y \\ v \\ \theta \\ \omega \end{array} \right].
$$

To calculate eigenvalues, compute

$$
\det \left[ \begin{array}{c c c c} s & - 1 & 0 & 0 \\ 5 0 & s & 0 & 0 \\ 0 & 0 & s & - 1 \\ 0 & 0 & 1 5 0 & s \end{array} \right] = (s ^ {2} + 5 0) (s ^ {2} + 1 5 0).
$$

The eigenvalues are:

$$s = \pm j \sqrt {5 0}s = \pm j \sqrt {1 5 0}.$$

Now we compute the eigenvectors. For $s = j\sqrt{50}$ , write

$$
\left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - 5 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & - 1 5 0 & 0 \end{array} \right] \left[ \begin{array}{c} v _ {1 1} \\ v _ {1 2} \\ v _ {1 3} \\ v _ {1 4} \end{array} \right] = j \sqrt {5 0} \left[ \begin{array}{c} v _ {1 1} \\ v _ {1 2} \\ v _ {1 3} \\ v _ {1 4} \end{array} \right].
$$

![](image/e6578130c691085331854f82c3c43fb25800f3168a462bc75ad35e15874ab66c.jpg)

<details>
<summary>text_image</summary>

Equilibrium
CG Position
z
θ
</details>

Figure 3.4 A sprung beam

This generates the equations

$$v _ {1 2} = j \sqrt {5 0} v _ {1 1}- 5 0 v _ {1 1} = j \sqrt {5 0} v _ {1 2}v _ {1 4} = j \sqrt {5 0} v _ {1 3}- 1 5 0 v _ {1 3} = j \sqrt {5 0} v _ {1 4}.$$

The second equation is simply the first, times $j\sqrt{50}$ ; therefore, $v_{12} = j\sqrt{50}v_{11}$ . Insertion of $v_{14}$ from the third equation into the fourth yields

$$- 1 5 0 v _ {1 3} = - 5 0 v _ {1 3}$$

which can hold only if $v_{13} = 0$ . So, $v_{13} = v_{14} = 0$ and the eigenvector is

$$
\mathbf {v} _ {1} = \alpha \left[ \begin{array}{c} 1 \\ j \sqrt {5 0} \\ 0 \\ 0 \end{array} \right]
$$

with $\alpha$ any real or complex constant.

It is easy to show that the eigenvector corresponding to $-j\sqrt{50}$ is $\mathbf{v}_1^*$ . The eigenvector corresponding to $j\sqrt{150}$ is

$$
\mathbf {v} _ {2} = \beta \left[ \begin{array}{c} 0 \\ 0 \\ 1 \\ j \sqrt {1 5 0} \end{array} \right]
$$

with $v_{2}^{*}$ corresponding to $-j\sqrt{150}$ .
