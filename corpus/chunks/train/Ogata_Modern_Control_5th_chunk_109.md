$$\left(b _ {1} s + k _ {1}\right) X _ {i} (s) = \left(b _ {1} s + k _ {1} + b _ {2} s - b _ {2} s \frac {b _ {2} s}{b _ {2} s + k _ {2}}\right) X _ {o} (s)$$

Hence the transfer function $X _ { o } ( s ) / X _ { i } ( s )$ can be obtained as

$$\frac {X _ {o} (s)}{X _ {i} (s)} = \frac {\left(\frac {b _ {1}}{k _ {1}} s + 1\right) \left(\frac {b _ {2}}{k _ {2}} s + 1\right)}{\left(\frac {b _ {1}}{k _ {1}} s + 1\right) \left(\frac {b _ {2}}{k _ {2}} s + 1\right) + \frac {b _ {2}}{k _ {1}} s}$$

For the electrical system shown in Figure 3–23(b), the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ is found to be

$$
\begin{array}{l} \frac {E _ {o} (s)}{E _ {i} (s)} = \frac {R _ {1} + \frac {1}{C _ {1} s}}{\frac {1}{\left(1 / R _ {2}\right) + C _ {2} s} + R _ {1} + \frac {1}{C _ {1} s}} \\ = \frac {\left(R _ {1} C _ {1} s + 1\right) \left(R _ {2} C _ {2} s + 1\right)}{\left(R _ {1} C _ {1} s + 1\right) \left(R _ {2} C _ {2} s + 1\right) + R _ {2} C _ {1} s} \\ \end{array}
$$

A comparison of the transfer functions shows that the systems shown in Figures 3–23(a) and (b) are analogous.

A–3–5. Obtain the transfer functions $E _ { o } ( s ) / E _ { i } ( s )$ of the bridged T networks shown in Figures 3–24(a) and (b).

Solution. The bridged T networks shown can both be represented by the network of Figure 3–25(a), where we used complex impedances.This network may be modified to that shown in Figure 3–25(b).

In Figure 3–25(b), note that

$$I _ {1} = I _ {2} + I _ {3}, \quad I _ {2} Z _ {1} = (Z _ {3} + Z _ {4}) I _ {3}$$

![](image/c4d3293883377547ae43b4d438d99329f3961370d60921ef8467707b69d8b1bc.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors and capacitors labeled R, C1, C2, ei, eo
</details>

(a)

![](image/9f3e462c068ba65b1c145ba7b8598847dbb45210ff7f2a1da941483bb14378b2.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors R1 and R2, capacitors C, and input/output terminals ei and eo
</details>

(b)

![](image/5d93a91b7a1f149b1f6c5709059f1b75b81926c88ed3b188081434a770f0b0c4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["i1"] --> B["Node"]
    B --> C["Z1"]
    C --> D["Node"]
    D --> E["Z3"]
    E --> F["Node"]
    F --> G["e0"]
    H["I1"] --> I["Node"]
    I --> J["Z2"]
    J --> K["I1"]
    L["I2"] --> M["Node"]
    M --> N["Z1"]
    N --> O["Node"]
    O --> P["Z3"]
    P --> Q["Node"]
    Q --> R["e0"]
    S["I3"] --> T["Z4"]
    T --> U["Node"]
    U --> V["Z3"]
    V --> W["Node"]
    W --> X["e0"]
```
</details>

(a)
