(1) $\| M _ { 1 1 } \| _ { \infty } \leq 1$ implies stability, but not conversely, because this test ignores the ∞known block diagonal structure of the uncertainties and is equivalent to regarding $\Delta$ as unstructured. This can be arbitrarily conservative in that stable systems can have arbitrarily large $\| M _ { 1 1 } \| _ { \infty }$ .

![](image/b24309f2d4b19984a369d18ad18e424d1932e6db9eb333d67c89039988492931.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Δ_F(s)"] --> B["..."]
    B --> C["δ_1(s)I"]
    C --> D["M_{11}(s)"]
    D --> E["..."]
    E --> F["..."]
    F --> A
```
</details>

Figure 10.4: Robust stability analysis framework

(2) Test for each $\delta _ { i } ~ ( \Delta _ { j } )$ individually (assuming no uncertainty in other channels). This test can be arbitrarily optimistic because it ignores interaction between the $\delta _ { i } ~ ( \Delta _ { j } )$ . This optimism is also clearly shown in the spinning body example in Section 8.6.

The difference between the stability margins (or bounds on $\Delta )$ obtained in (1) and (2) can be arbitrarily far apart. Only when the margins are close can conclusions be made about the general case with structured uncertainty.

The exact stability and performance analysis for systems with structured uncertainty requires a new matrix function called the structured singular value (SSV), which is denoted by µ.
