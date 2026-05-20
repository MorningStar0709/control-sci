# 8.3 Stability under Unstructured Uncertainties

The small gain theorem in the last section will be used here to derive robust stability tests under various assumptions of model uncertainties. The modeling error $\Delta$ will again be assumed $\tan$ be stable. (Most of the robust stability tests discussed in the sequel can be generalized easily to the unstable $\Delta$ case with some mild assumptions on the number of unstable poles of the uncertain model; we encourage readers to fill in the details.) In addition, we assume that the modeling error $\Delta$ is suitably scaled with weighting functions $W _ { 1 }$ and $W _ { 2 } \ ( \mathrm { i . e . }$ , the uncertainty can be represented as $W _ { 1 } \Delta W _ { 2 } )$ .

![](image/0974315fabde9d9e46d0f3da33b1aa87aa81edd9f908ae77ce76cd11c09d01d5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input"] --> B((+))
    B --> C["K"]
    C --> D["Π"]
    D --> E["Output"]
    E --> F["Feedback"]
    F --> B
```
</details>

Figure 8.9: Unstructured robust stability analysis

We shall consider the standard setup shown in Figure 8.9, where Π is the set of uncertain plants with $P \in \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf } } } \mathbf { \mathbf { \mathbf { \mathbf } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf } } } \mathbf { \mathbf { \mathbf { \mathbf } } } } } }$ as the nominal plant and with K as the internally stabilizing controller for $P .$ The sensitivity and complementary sensitivity matrix functions are defined, as usual, as

$$S _ {o} = (I + P K) ^ {- 1}, T _ {o} = I - S _ {o}$$

and

$$S _ {i} = (I + K P) ^ {- 1}, T _ {i} = I - S _ {i}.$$

Recall that the closed-loop system is well-posed and internally stable if and only if

$$
\left[ \begin{array}{c c} I & K \\ - \Pi & I \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} (I + K \Pi) ^ {- 1} & - K (I + \Pi K) ^ {- 1} \\ (I + \Pi K) ^ {- 1} \Pi & (I + \Pi K) ^ {- 1} \end{array} \right] \in \mathcal {R H} _ {\infty}
$$

for all $\Pi \in \Pi .$
