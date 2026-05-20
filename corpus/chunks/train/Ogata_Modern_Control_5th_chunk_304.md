If the gain K of the open-loop transfer function is given in the problem, then by applying the magnitude condition, we can find the correct locations of the closed-loop poles for a given K on each branch of the root loci by a trial-and-error approach or by use of MATLAB, which will be presented in Section 6–3.

Comments on the Root-Locus Plots. It is noted that the characteristic equation of the negative feedback control system whose open-loop transfer function is

$$G (s) H (s) = \frac {K \left(s ^ {m} + b _ {1} s ^ {m - 1} + \cdots + b _ {m}\right)}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n}} \quad (n \geq m)$$

is an nth-degree algebraic equation in s. If the order of the numerator of $G ( s ) H ( s )$ is lower than that of the denominator by two or more (which means that there are two or more zeros at infinity), then the coefficient $a _ { 1 }$ is the negative sum of the roots of the equation and is independent of K. In such a case, if some of the roots move on the locus toward the left as K is increased, then the other roots must move toward the right as K is increased. This information is helpful in finding the general shape of the root loci.

It is also noted that a slight change in the pole–zero configuration may cause significant changes in the root-locus configurations. Figure 6–13 demonstrates the fact that a slight change in the location of a zero or pole will make the root-locus configuration look quite different.

![](image/39dabffec1c18391ac3b9f78d5cb2e052e1d131bf60c387162fa2687ad3c995d.jpg)

<details>
<summary>text_image</summary>

jω
σ
jω
σ
</details>

Figure 6–13 Root-locus plots.

Cancellation of Poles of $G ( s )$ with Zeros of H(s). It is important to note that if the denominator of $G ( s )$ and the numerator of $H ( s )$ involve common factors, then the corresponding open-loop poles and zeros will cancel each other, reducing the degree of the characteristic equation by one or more. For example, consider the system shown in Figure 6–14(a). (This system has velocity feedback.) By modifying the block diagram of Figure 6–14(a) to that shown in Figure 6–14(b), it is clearly seen that $G ( s )$ and $H ( s )$ have a common factor $s + 1$ . The closed-loop transfer function $C ( s ) / R ( s )$ is

$$\frac {C (s)}{R (s)} = \frac {K}{s (s + 1) (s + 2) + K (s + 1)}$$

The characteristic equation is

$$[ s (s + 2) + K ] (s + 1) = 0$$

Because of the cancellation of the terms $( s + 1 )$ appearing in $G ( s )$ and $H ( s )$ , however, we have
