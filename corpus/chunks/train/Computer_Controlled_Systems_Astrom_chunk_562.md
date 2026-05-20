![](image/6bf9fb71d981a1fad949bae3d60992112db4f76767a8d2442c7b7ae3dc05eb79.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 5 | 0.2 |
| 10 | 0.8 |
| 15 | 1.2 |
| 20 | 1.1 |
| 25 | 1.0 |
| 30 | 1.0 |
| 35 | 1.0 |
| 40 | 1.0 |
| 45 | 1.0 |
| 50 | 1.0 |
| 55 | 1.0 |
| 60 | 1.0 |
| 65 | 1.0 |
| 70 | 1.0 |
| 75 | 1.0 |
| 80 | 1.0 |
| 85 | 1.0 |
| 90 | 1.0 |
| 95 | 1.0 |
| 100 | 1.0 |
</details>

![](image/cb440300ea7cc67a3a08b95e2bdc02e3e41cf73f885f863be8f1c25329c0ce7a.jpg)

<details>
<summary>scatter</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 5 | 0.3 |
| 10 | 1.2 |
| 15 | 1.0 |
| 20 | 0.9 |
| 25 | 1.1 |
| 30 | 1.0 |
| 35 | 1.0 |
| 40 | 1.0 |
| 45 | 1.0 |
| 50 | 1.0 |
| 55 | 1.0 |
</details>

![](image/be0736847c61e42f81d76d3df220381f3aca3660dbd3b949560ff9880e08b8e9.jpg)

<details>
<summary>scatter</summary>

| Time | Output |
| --- | --- |
| 0 | 0.5 |
| 5 | 1.2 |
| 10 | 0.8 |
| 15 | 1.5 |
| 20 | 0.6 |
| 25 | 1.3 |
| 30 | 0.9 |
| 35 | 1.1 |
| 40 | 0.7 |
| 45 | 1.4 |
| 50 | 0.8 |
| 55 | 1.2 |
| 60 | 0.9 |
| 65 | 1.3 |
| 70 | 0.7 |
| 75 | 1.1 |
| 80 | 0.8 |
</details>

Figure 9.13 The output of the system in Example 9.4 when $\delta = 0.2$ and (a) $K = 0.8$ , (b) $K = 1.2$ , and (c) $K = 1.6$ .

![](image/7439c92d9fb96bb40729a9abd64969829ab5320e86222c503dc90ef99d34a4ed.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["y"] --> B["π"]
    B --> C["Q"]
    D["a"] --> B
    E["e_a"] --> F["Σ"]
    G["y"] --> H["π"]
    H --> I["Σ"]
```
</details>

Figure 9.14 Linear models for multiplication with roundoff.

![](image/6a524289414723d3b0218675c3b93756112f3b34f778c1807cc4e00554f7a51c.jpg)  
Figure 9.15 Control of a double integrator with a quantized A-D converter. The sampling period is 1 s and the quantization level is 0.02. The middle curve shows the quantized as well as the unquantized output.
