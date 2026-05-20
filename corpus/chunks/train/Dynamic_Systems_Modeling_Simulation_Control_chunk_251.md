# Standard Block-Diagram Components

Figure 5.8 shows the multiplication of input signal u by the constant (or gain) K to produce the output signal y. Simulink uses a triangle-shaped block for a gain, since it is the traditional symbol for an operational amplifier (“op amp”) used to boost electrical signals.

Figure 5.9 shows three blocks that represent the time integration of input signal u. Figure 5.9b shows integration as the inverse of the differential or D operator, while Fig. 5.9c uses the transfer function 1∕s to denote integration. Simulink uses the 1∕s block in Fig. 5.9c to represent integration. The initial value of the integrator output, y(0), can be set in the Simulink environment (see Chapter 6 and Appendix C).

Figure 5.10 shows a transfer function block that represents an I/O differential equation. For example, if the transfer function G(s) in Fig. 5.10 is

$$G (s) = \frac {3 s + 2}{s ^ {2} + 4 s + 2 0} \tag {5.111}$$

![](image/257c4937856e30fbb0f8cf98937518bc14bdd4964454728130480f6603099103.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input signal, u"] --> B["K"]
    B --> C["Output signal, y = Ku"]
```
</details>

Figure 5.8 Gain block.

![](image/fd2eba3a7cc7af2db4fc3618dfa5a71297f4fe0b3a3822b0dbb112c178423705.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input signal, u"] --> B["∫"]
    B --> C["Output signal, y = u dt + y(0)"]
```
</details>

![](image/19db7d5ca556db425c212491ffafce83161ebda8c9f618a19505df87931098da.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input signal, u"] --> B["1/D"]
    B --> C["Output signal, y = ∫udt + y(0)"]
```
</details>

![](image/43fe560fb7c2b7e1188729524493db54cf11f972c5ea56cca6b43c509a0b3d6d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input signal, u"] --> B["1/s"]
    B --> C["Output signal, y = u dt + y(0)"]
```
</details>

Figure 5.9 Integrator blocks: (a) integral symbol, (b) D-operator symbol, and (c) transfer-function symbol.

![](image/aa2ee21b62584104505d76e3e9b2927410588236e9e9b1111ab9ebc38d57f93b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input signal, u"] --> B["G(s)"]
    B --> C["Output signal, y"]
```
</details>

Figure 5.10 Transfer function block.

![](image/29ae6f8f9be5fe5435add8e7a6746c0ec010b5360c726260a031d2d139201ef5.jpg)
