# 3.7.4 The Canonical Decomposition

In the diagonal form, the state variables can be divided into four categories:

- Controllable and observable $(\mathbf{w}_i^T B \neq \mathbf{0}, C\mathbf{v}_i \neq \mathbf{0})$   
- Uncontrollable and observable $(\mathbf{w}_i^T B = \mathbf{0}, C\mathbf{v}_i \neq \mathbf{0})$   
- Controllable and unobservable $(\mathbf{w}_i^T B \neq \mathbf{0}, C\mathbf{v}_i = \mathbf{0})$   
- Uncontrollable and unobservable $(\mathbf{w}_i^T B = \mathbf{0}, C\mathbf{v}_i = \mathbf{0})$

This decomposition, called the canonical decomposition, is illustrated in Figure 3.10. Figures 3.11, 3.12, and 3.13 show the more general structure of this decomposition, which is applicable in the general case of multiple eigenvalues. Figure 3.11 illustrates the decomposition into controllable and uncontrollable parts. In Figure 3.12 the system is split into observable and unobservable parts. Figure 3.13 combines Figures 3.11 and 3.12 in the sense that the controllable and uncontrollable blocks are both further divided into observable and unobservable parts. Note that there is no path, direct or through a block, from the input to either of the uncontrollable blocks. Similarly, the unobservable blocks have no path to the output.

![](image/59391a3cae694b25d0da3e6436de8c8d5814885ac245a74c07618c7ecb421739.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A[".5"] --> B["1/s"]
    B --> C["z2"]
    C --> D["1/s"]
    D --> E["z1"]
    E --> F["1"]
    F --> G["+"]
    G --> H["x"]
    I[".0565"] --> J["1/(s-4.4272)"]
    J --> K["z3"]
    K --> L["2"]
    L --> M["+"]
    M --> N["θ"]
    O["-.0565"] --> P["1/(s+4.4272)"]
    P --> Q["z4"]
    Q --> R["2"]
    R --> S["+"]
    S --> T["θ"]
    U["F"] --> V[".5"]
    V --> W[".0565"]
    X["+"] --> Y["+"]
    Y --> Z["x"]
```
</details>

Figure 3.9 Block diagram for the Jordan form of the pendulum-and-cart system

The transfer function of the system is that of the controllable and observable block; the other three blocks have no influence. To see this, recall that the transfer function is the transform of the zero-state response. If the initial state is zero, the two uncontrollable blocks remain in the zero state and have zero effect on y. The state of the controllable, unobservable block does move away from zero under the influence of the input, but that has no effect on the output because that block has no connection to y. That leaves only the controllable, observable block.
