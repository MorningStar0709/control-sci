where, the new function $\mathbf{h}(t)$ satisfies [3, 6]

$$
\begin{array}{l} \dot {\mathbf {h}} (t) = - \frac {1}{2} \mathbf {g} ^ {\prime} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \mathbf {g} (t) - \frac {1}{2} \mathbf {z} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {z} (t) \\ = - \frac {1}{2} \mathbf {g} ^ {\prime} (t) \mathbf {E} (t) \mathbf {g} (t) - \frac {1}{2} \mathbf {z} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {z} (t) \tag {4.1.27} \\ \end{array}
$$

with final condition

$$\mathbf {h} (t _ {f}) = - \mathbf {z} ^ {\prime} (t _ {f}) \mathbf {P} (t _ {f}) \mathbf {z} (t _ {f}). \tag {4.1.28}$$

For further details on this, see $[3, 6, 89, 90]$ . We now summarize the tracking system.

![](image/aa8b3bbd77f193467e8f26dc13fd845bfdc47a6a5aa813a2c37f69f04d5433df.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u*(t)"] --> B["B(t)"]
    B --> C["+"]
    C --> D["∫"]
    D --> E["x*(t)"]
    E --> F["C(t)"]
    F --> G["y*(t)"]
    G --> H["A(t)"]
    H --> I["Plant"]
    I --> J["Closed-Loop Optimal Controller"]
    J --> K["R⁻¹(t)B'(t)"]
    K --> L["+"]
    L --> M["P(t)x*(t)"]
    M --> N["P(t)"]
    N --> O["Off-Line Simulation of P(t) and g(t)"]
    O --> P["Desired z(t)"]
    P --> Q["g(t)"]
    Q --> K
```
</details>

Figure 4.1 Implementation of the Optimal Tracking System
