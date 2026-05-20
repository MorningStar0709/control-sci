$$\lambda^ {2} \left\| D ^ {\frac {1}{2}} x \right\| ^ {2} = \left\| Q D ^ {\frac {1}{2}} M x \right\| ^ {2} \leq \left\| D ^ {\frac {1}{2}} M x \right\| ^ {2}.$$

Hence

$$x ^ {*} (M ^ {*} D M - \lambda^ {2} D) x \geq 0.$$

Next, let $G \in { \mathcal { G } }$ and note that $Q ^ { * } G = Q G = G Q ;$ ; then

$$
\begin{array}{l} x ^ {*} G M x = \left(\frac {1}{\lambda} Q M x\right) ^ {*} G M x = \frac {1}{\lambda} x ^ {*} M ^ {*} Q ^ {*} G M x = \frac {1}{\lambda} x ^ {*} M ^ {*} Q G M x \\ = \frac {1}{\lambda} x ^ {*} M ^ {*} G Q M x = \frac {1}{\lambda} x ^ {*} M ^ {*} G (Q M x) = x ^ {*} M ^ {*} G x. \\ \end{array}
$$

That is,

$$x ^ {*} (G M - M ^ {*} G) x = 0.$$

Note that $j ( G M - M ^ { * } G )$ is a Hermitian matrix, so it follows that for such x

$$x ^ {*} (M ^ {*} D M + j (G M - M ^ {*} G) - \lambda^ {2} D) x \geq 0.$$

It is now easy to see that if we have $D \in { \mathcal { D } } , G \in { \mathcal { G } }$ and $0 \leq \beta \in \mathbb { R }$ such that

$$M ^ {*} D M + j (G M - M ^ {*} G) - \beta^ {2} D \leq 0$$

then $| \lambda | \leq \beta ,$ and hence $\mu _ { \Delta } ( M ) \leq \beta .$

This upper bound has an interesting interpretation: covering the uncertainties on the real axis using possibly off-axis disks. To illustrate, let $M \in \mathbb { C }$ be a scalar and $\Delta \in [ - 1 , 1 ]$ . We can cover this real interval using a disk as shown in Figure 18.2.

The off-axis disk can be expressed as

$$j \frac {G}{\beta} + \sqrt {1 + \left(\frac {G}{\beta}\right) ^ {2}} \tilde {\Delta}, \quad \tilde {\Delta} \in \mathbb {C}, | \tilde {\Delta} | \leq 1.$$

![](image/e3e47776a3ebed39e85850eabd0bba497f68ddb9011bd2e5109648ba38c675d7.jpg)

<details>
<summary>text_image</summary>

Im
j
-1 1 Re
-j
</details>

Centered Disk

![](image/42be48cbd9739165865062a1fc47ba514d6ad3138a57335b5ac2a141e0654b93.jpg)

<details>
<summary>text_image</summary>

Im
-j G/β
-1 1 Re
</details>

Off-Axis Disk   
Figure 18.2: Covering real parameters with disks

Hence $1 - \Delta \frac { M } { \beta } \neq 0$ for all $\Delta \in [ - 1 , 1 ]$ is guaranteed if
