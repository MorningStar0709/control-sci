# 16.1 Robust Stabilization of Coprime Factors

In this section, we use the $\mathcal { H } _ { \infty }$ control theory developed in previous chapters to solve the robust stabilization of a left coprime factor perturbed plant given by

$$P _ {\Delta} = (\tilde {M} + \tilde {\Delta} _ {M}) ^ {- 1} (\tilde {N} + \tilde {\Delta} _ {N})$$

with $\tilde { M } , \tilde { N } , \tilde { \Delta } _ { M } , \tilde { \Delta } _ { N } \in \mathcal { R H } _ { \infty }$ and $\left\| \left[ \begin{array} { l l } { \tilde { \Delta } _ { N } } & { \tilde { \Delta } _ { M } } \end{array} \right] \right\| _ { \infty } < \epsilon$ (see Figure 16.1). The transfer matrices $( \tilde { M } , \tilde { N } )$ are assumed to be a left coprime factorization of $P \ ( \mathrm { i . e . , } \ P = \tilde { M } ^ { - 1 } \tilde { N } )$ , and K internally stabilizes the nominal system.

It has been shown in Chapter 8 that the system is robustly stable iff

$$
\left\| \left[ \begin{array}{c} K \\ I \end{array} \right] (I + P K) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} \leq 1 / \epsilon .
$$

Finding a controller such that the above norm condition holds is an $\mathcal { H } _ { \infty }$ norm minimization problem that can be solved using $\mathcal { H } _ { \infty }$ theory developed in previous chapters.

![](image/15fd4ab09377733d6406121f3dc2aa3e835ae3d6d98a0fe98572bdfbc4e4f42e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> |r| A["•"]
    A --> B["K"]
    B --> C["Ñ"]
    C --> D["•"]
    D --> E["M̃⁻¹"]
    E --> y
    z1 --> D
    Δ̃_N --> D
    Δ̃_M --> D
    w --> D
    z2 --> E
    w --> D
    - --> D
    - --> A
```
</details>

Figure 16.1: Left coprime factor perturbed systems

Suppose P has a stabilizable and detectable state-space realization given by

$$
P = \left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right]
$$

and let L be a matrix such that $A + L C$ is stable. Then a left coprime factorization of $P = \tilde { M } ^ { - 1 } \tilde { N }$ is given by

$$
\left[ \begin{array}{c c} \tilde {N} & \tilde {M} \end{array} \right] = \left[ \begin{array}{c c c} A + L C & B + L D & L \\ \hline Z C & Z D & Z \end{array} \right]
$$

where $Z$ can be any nonsingular matrix. In particular, we shall choose $Z = ( I +$ $D D ^ { * } ) ^ { - 1 / 2 } \mathrm { i f } P = \tilde { M } ^ { - 1 } \tilde { N }$ is chosen to be a normalized left coprime factorization. Denote

$$\hat {K} = - K.$$

Then the system diagram can be put in an LFT form, as in Figure 16.2, with the generalized plant
