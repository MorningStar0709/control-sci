<table><tr><td>G</td><td>H</td><td></td><td>Pi</td></tr><tr><td>80</td><td>4</td><td colspan="2"> $\frac{80}{1+4\times80} = \frac{80}{321} = 0.24922$ </td></tr><tr><td>88</td><td>4</td><td colspan="2"> $\frac{88}{1+4\times88} = 0.24929$ </td></tr></table>

Now we compute $\Delta P _ { i }$ by subtracting the numerical results (note that we needed to use 6 signicant gures to get a non-zero result).

$$\Delta P _ {i} = 0. 2 4 9 2 9 - 0. 2 4 9 2 2 = 0. 0 0 0 0 7 = 7. 0 \times 1 0 ^ {- 5}$$

Then, using eqn. 6.3,

$$S _ {i j} = \frac {7 \times 1 0 ^ {- 5} / 0 . 2 4 9 2 2}{8 / 8 0} = 2. 8 1 \times 1 0 ^ {- 3} = 0. 3$$

Since sensitivity values are normalized by the nominal values of parameter and performance, we can judge them on an absolute scale where $S _ { i j } = 1 0 0 \%$ indicates strong sensitivity. In this case we can see that sensitivity of closed loop gain to G is small.

![](image/7259a4f46dff0b25e25f42dac0decf30d808ebaae34151dd17023a0ff002af30.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X -->|+| A["Sum"]
    A -->|e| B["G"]
    B --> C["Sum"]
    C --> D["y"]
    D --> E["H"]
    E -->|-| A
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
```
</details>

Figure 6.6: A closed loop system with a disturbance.
