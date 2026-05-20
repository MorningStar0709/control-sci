![](image/1361fa4309f4d3e11e332f51901729e7f486eb043a36242d70a4f1faa90aef12.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistor, capacitor, and current direction labels
</details>

(a)

![](image/9348d1ab2e01b3bc3251acb55f1c2fae3de2f0654e3c2db6b7418f704d2e3c2c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["E_i(s)"] --> B["+"]
    B --> C["1/R"]
    C --> D["I(s)"]
    D --> E["E_o(s)"]
    E --> B
```
</details>

(b)

![](image/e8fba90e24637d1ce5ba261e4d27aecabdd3eab08a504dff79cf8c9e8139f961.jpg)

![](image/67b306aa7f8dcdf25d0bd74bb9a5c3c98c4e23993662bf30836d12382f99e1c3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Ei(s)"] --> B["+"]
    B --> C["1/R"]
    C --> D["I(s)"]
    D --> E["1/Cs"]
    E --> F["Eo(s)"]
    F --> G["Feedback"]
    G --> B
```
</details>

(d)

A complicated block diagram involving many feedback loops can be simplified by a step-by-step rearrangement. Simplification of the block diagram by rearrangements considerably reduces the labor needed for subsequent mathematical analysis. It should be noted, however, that as the block diagram is simplified, the transfer functions in new blocks become more complex because new poles and new zeros are generated.
