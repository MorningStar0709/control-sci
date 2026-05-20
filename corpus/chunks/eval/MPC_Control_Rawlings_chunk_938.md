# B.2 Stability and Asymptotic Stability

In this section we consider the stability properties of the autonomous system $x ^ { + } = f ( x )$ ; we assume that $f ( \cdot )$ is locally bounded, and that the set A is closed and positive invariant for $x ^ { + } = f ( x )$ unless otherwise stated.

Definition B.4 (Local stability). The (closed positive invariant) set A is locally stable for $x ^ { + } = f ( x )$ if, for all $\varepsilon > 0$ , there exists a $\delta > 0$ such that $| x | _ { \mathcal { A } } < \delta$ implies $| \phi ( i ; x ) | _ { \mathcal { A } } < \varepsilon$ for all $i \in \mathbb { I } _ { \geq 0 }$ .

See Figure B.1 for an illustration of this definition when $\mathcal { A } = \{ 0 \}$ ; in this case we speak of stability of the origin.

Definition B.5 (Global attraction). The (closed positive invariant) set A is globally attractive for the system $x ^ { + } = f ( x ) \mathrm { ~ i f ~ } | \phi ( i ; x ) | _ { \mathcal { A } } \to 0$ as $i  \infty$ for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ .

Definition B.6 (Global asymptotic stability (GAS)). The (closed positive invariant) set A is globally asymptotically stable (GAS) for $x ^ { + } = f ( x )$ if it is locally stable and globally attractive.

It is possible for the origin to be globally attractive but not locally stable. Consider a second order system

$$x ^ {+} = A x + \phi (x)$$

![](image/d4559ca5e7c144f1fca6599e7da7ac0543922a9d4159b0d08ef965db1a73ae05.jpg)

<details>
<summary>text_image</summary>

Bε(0)
x
0
Bδ(0)
</details>

Figure B.1: Stability of the origin.
