# 10.3.1 Robust Stability

The most well-known use of $\mu$ as a robustness analysis tool is in the frequency domain. Suppose $G ( s )$ is a stable, real rational, multi-input, multioutput transfer function of a linear system. For clarity, assume $G$ has $q _ { 1 }$ inputs and $p _ { 1 }$ outputs. Let $\pmb { \Delta }$ be a block structure, as in equation (10.1), and assume that the dimensions are such that $\pmb { \Delta } \subset \mathbb { C } ^ { q _ { 1 } \times p _ { 1 } }$ . We want to consider feedback perturbations to $G$ that are themselves dynamical systems with the block diagonal structure of the set $\Delta$ .

Let $\mathcal { M } \left( \Delta \right)$ denote the set of all block diagonal and stable rational transfer functions that have block structures such as $\pmb { \Delta }$ .

$$\mathcal {M} (\pmb {\Delta}) := \left\{\Delta (\cdot) \in \mathcal {R H} _ {\infty}: \Delta (s _ {o}) \in \pmb {\Delta} \mathrm{forall} s _ {o} \in \overline {{\mathbb {C}}} _ {+} \right\}$$

Theorem 10.7 Let $\beta > 0$ . The loop shown below is well-posed and internally stable for all $\Delta ( \cdot ) \in \mathcal { M } ( \Delta )$ with $\begin{array} { r } { \| \Delta \| _ { \infty } < \frac { 1 } { \beta } } \end{array}$ if and only $i f$

![](image/d9f33f9b3d61ab30c10c2c0d3a6cd7cd9a0cbd705fcc0ef4f340386ece06e1f8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    w1 -->|+| sum1
    sum1 --> e1
    e1 --> delta["Δ"]
    delta --> sum2
    sum2 -->|+| w2
    w2 --> Gs["G(s)"]
    Gs --> e2
    e2 --> sum1
    subgraph Gamma_G fill:#f9f,stroke:#333
    end
    note[" sup_{ω∈R} μ_Δ(G(jω)) ≤ β. "]
```
</details>

Proof. (⇐=) Suppose $\begin{array} { r } { \operatorname* { s u p } _ { s \in \overline { { \mathbb { C } } } _ { + } } \ \mu _ { \Delta } ( G ( s ) ) \leq \beta } \end{array}$ . Then det $( I - G ( s ) \Delta ( s ) ) \neq 0$ for all $s \in \overline { { \mathbb { C } } } _ { + } \cup \{ \infty \}$ whenever $\| \Delta \| _ { \infty } < 1 / \beta$ (i.e., the system is robustly stable). Now it is sufficient to show that

$$\sup _ {s \in \overline {{\mathbb {C}}} _ {+}} \mu_ {\boldsymbol {\Delta}} (G (s)) = \sup _ {\omega \in \mathbb {R}} \mu_ {\boldsymbol {\Delta}} (G (j \omega)).$$

It is clear that

$$\sup _ {s \in \overline {{\mathbb {C}}} _ {+}} \mu_ {\Delta} (G (s)) = \sup _ {s \in \mathbb {C} _ {+}} \mu_ {\Delta} (G (s)) \geq \sup _ {\omega} \mu_ {\Delta} (G (j \omega)).$$
