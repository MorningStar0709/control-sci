$$\min _ {K} \inf _ {D, D ^ {- 1} \in \mathcal {H} _ {\infty}} \left\| D \mathcal {F} _ {\ell} (G, K) D ^ {- 1} \right\| _ {\infty} \tag {10.33}$$

by iteratively solving for K and D. This is the so-called D-K iteration. The stable and minimum phase scaling matrix $D ( s )$ is chosen such that $D ( s ) \Delta ( s ) = \Delta ( s ) D ( s )$ . [Note that $D ( s )$ is not necessarily belonging to D since $D ( s )$ is not necessarily Hermitian, see Remark 10.2.] For a fixed scaling transfer matrix D, minK $\cdot \left\| D \mathcal { F } _ { \ell } ( G , \dot { K } ) D ^ { - 1 } \right\| _ { \infty }$ is a standard $\mathcal { H } _ { \infty }$ optimization problem that will be solved later in this book. For a given stabilizing controller K, inf $D , D ^ { - 1 } \in \mathcal { H } _ { \infty } \ \left\| D \mathcal { F } _ { \ell } ( G , K ) D ^ { - 1 } \right\| _ { \infty }$ is a standard convex optimization problem and it can be solved pointwise in the frequency domain:

$$\sup _ {\omega} \inf _ {D _ {\omega} \in \mathcal {D}} \overline {{\sigma}} \left[ D _ {\omega} \mathcal {F} _ {\ell} (G, K) (j \omega) D _ {\omega} ^ {- 1} \right].$$

Indeed,

$$\inf _ {D, D ^ {- 1} \in \mathcal {H} _ {\infty}} \left\| D \mathcal {F} _ {\ell} (G, K) D ^ {- 1} \right\| _ {\infty} = \sup _ {\omega} \inf _ {D _ {\omega} \in \mathcal {D}} \overline {{\sigma}} \left[ D _ {\omega} \mathcal {F} _ {\ell} (G, K) (j \omega) D _ {\omega} ^ {- 1} \right].$$

This follows intuitively from the following arguments: The left-hand side is always no smaller than the right-hand side, and, on the other hand, given $D _ { \omega } \in \mathcal { D } .$ , there is always a real-rational function $D ( s )$ , stable with stable inverse, such that the Hermitian positive definite factor in the polar decomposition of $D ( j \omega )$ uniformly approximates $D _ { \omega }$ over ω in R. In particular, in the case of scalar blocks, the magnitude $| D ( j \omega ) |$ uniformly approximates $D _ { \omega }$ over R.

Note that when $S = 0$ (no scalar blocks),

$$D _ {\omega} = \operatorname{diag} (d _ {1} ^ {\omega} I, \dots , d _ {F - 1} ^ {\omega} I, I) \in \mathcal {D},$$

which is a block diagonal scaling matrix applied pointwise across frequency to the frequency response $\mathcal { F } _ { \ell } ( G , K ) ( j \omega )$ .

![](image/a50bb675b916334dad427624415ed051d3f6a273cb1f67b3f4e96decd7e7a6af.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    D --> G
    G --> D^-1
    D^-1 --> G
    G --> K
    K --> G
```
</details>

Figure 10.9: µ synthesis via scaling
