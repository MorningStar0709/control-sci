# 9.2 Basic Principle

We have studied two simple examples of the use of LFTs and, in particular, their role in modeling uncertainty. The basic principle at work here in writing a matrix LFT is often referred to as “pulling out the $\Delta { \mathit { } s } ^ { \prime \prime }$ . We will try to illustrate this with another picture. Consider a structure with four substructures interconnected in some known way, as shown in Figure 9.4. This diagram can be redrawn as a standard one via “pulling out the $\Delta { \ ' } _ { \mathrm { s } } { \ ' }$ in Figure 9.5.

Now the matrix M of the LFT can be obtained by computing the corresponding transfer matrix in the shadowed box.

We shall illustrate the preceding principle with an example. Consider an input/output relation

$$z = \frac {a + b \delta_ {2} + c \delta_ {1} \delta_ {2} ^ {2}}{1 + d \delta_ {1} \delta_ {2} + e \delta_ {1} ^ {2}} w =: G w$$

where $a , b , c , d ,$ and e are given constants or transfer functions. We would like to write $G$ as an LFT in terms of $\delta _ { 1 }$ and $\delta _ { 2 }$ . We shall do this in three steps:

1. Draw a block diagram for the input/output relation with each $\delta$ separated as shown in Figure 9.6.

![](image/25e2aff17c87fb2d993fcf9f237d1c764832b10b3cbc50055a023d544d6bea31.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Δ₁"] --> B["Δ₂"]
    C["Δ₃"] --> D["K"]
    style A fill:#f9f,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#f9f,stroke:#333
```
</details>

Figure 9.4: Multiple source of uncertain structure

![](image/eb187a0f69deca3707556e385d23813efd97a4320d89cea1c0be5cce97d48543.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Δ1"] --> B["Δ2"]
    B --> C["Δ3"]
    C --> D["K"]
    D --> E["Process Block"]
    E --> F["Δ3"]
    F --> G["Δ2"]
    G --> H["Δ1"]
    H --> I["Output"]
    style A fill:#f9f,stroke:#333
    style B fill:#f9f,stroke:#333
    style C fill:#f9f,stroke:#333
    style D fill:#ccf,stroke:#333
    style E fill:#cfc,stroke:#333
    style F fill:#cfc,stroke:#333
    style G fill:#cfc,stroke:#333
    style H fill:#cfc,stroke:#333
    style I fill:#cfc,stroke:#333
```
</details>

Figure 9.5: Pulling out the $\Delta \mathrm { { s } }$

![](image/6fc54a42cf66ae334baa8b4b395e89e40cfa7906189b5e422f13516005347198.jpg)

<details>
<summary>flowchart</summary>
