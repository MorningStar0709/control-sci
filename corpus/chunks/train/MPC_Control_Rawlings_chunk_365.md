It also follows from (3.11), (3.12) and (3.15) that $V _ { N } ^ { 0 } ( \cdot )$ and $R _ { c }$ satisfy Definition B.37 so that $V _ { N } ^ { 0 } ( \cdot )$ is an ISS-Lyapunov function in $R _ { c }$ for the uncertain system $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w ) , w \in \mathbb { W }$ . By Lemma B.38, the system $x ^ { + } = f ( x , \kappa _ { N } ( x ) , w ) , w \in \mathbb { W }$ is ISS in $R _ { c }$ satisfying, therefore, for some $\beta ( \cdot ) \in \mathcal { K } \mathcal { L } _ { \infty }$ , some $\sigma ( \cdot ) \in \mathcal { K }$ ,

$$\left| \phi (i; x, \mathbf {w} _ {i}) \right| \leq \beta (\left| x \right|, i) + \sigma (\left\| \mathbf {w} _ {i} \right\|) \leq \beta (\left| x \right|, i) + \sigma (e)$$

for all $i \in \mathbb { I } _ { \geq 0 }$ where $\phi ( i ; x , \mathbf { w } _ { i } )$ is the solution at time i if the initial state at time 0 is x and the disturbance sequence is $\mathbf { w } _ { i } : = \{ w ( 0 ) , w ( 1 ) , \ldots ,$ $w ( i - 1 ) \}$ .

The next section describes how DP may be used, in principle, to achieve robust receding horizon control (RHC). The purpose of this section is to provide some insight into the problem of robust control;

![](image/8737a50a34406a88d28b34edbebb94fd294235d3fa037b2bf0084231b32d4c1c.jpg)

<details>
<summary>text_image</summary>

R_c
x
R_b
X_N
</details>

Figure 3.2: The sets $\boldsymbol { \chi } _ { N }$ , $R _ { b }$ , and $R _ { c }$ .

the section does not show how to obtain robust model predictive controllers that are implementable. Readers whose main concern is implementable robust MPC may prefer to proceed directly to Section 3.4.
