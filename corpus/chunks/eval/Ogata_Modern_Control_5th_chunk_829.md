```mermaid
graph LR
    r --> |+| sum
    sum --> e --> Ks["K(s)"] --> Gs["G(s)"] --> y
    y --> |feedback| sum
```
</details>

![](image/ca79ac45bc75cb3c314cc8a6a4bc7105247769cbcceda3d9f6c1ca6d0a595d92.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    w --> A["+"]
    u --> B["G"]
    u --> C["-"]
    u --> D["K"]
    A --> E["+"]
    B --> F["-"]
    C --> G["+"]
    D --> H["K"]
    E --> I["z1"]
    F --> J["z2"]
    G --> K["y"]
    H --> L["y"]
    I --> M["z1"]
    J --> N["z2"]
    K --> O["y"]
    L --> P["y"]
    M --> Q["w"]
    N --> R["w"]
    O --> S["w"]
    P --> T["w"]
    Q --> U["WmI"]
    R --> V["WsI"]
```
</details>

Figure 10–45   
(a) Generalized plant diagram; (b) simplfied version of the generalized plant diagram shown in (a).

![](image/b356e1de2952963da1daf9dea0d21faa7f4c263f26b93d85f00d21eb9cba188c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    z --> P
    P --> w
    P --> u
    u --> K
    K --> y
    y --> P
```
</details>

(b)

Finding Transfer Function $z ( s ) / w ( s )$ from a Generalized Plant Diagram. Consider the generalized plant diagram shown in Figure 10–46.

In this diagram $w ( s )$ is the exogenous disturbance and $u ( s )$ is the manipulated variable. $z ( s )$ is the controlled variable and $y ( s )$ is the observed variable.

Consider this control system consisting of the generalized plant $P ( s )$ and the controller K(s).The equation that relates the outputs $z ( s )$ and $y ( s )$ and the inputs $w ( s )$ and $u ( s )$ of the generalized plant $P ( s )$ is

$$
\left[ \begin{array}{c} z (s) \\ y (s) \end{array} \right] = \left[ \begin{array}{c c} P _ {1 1} & P _ {1 2} \\ P _ {2 1} & P _ {2 2} \end{array} \right] \left[ \begin{array}{c} w (s) \\ u (s) \end{array} \right]
$$

The equation that relates $u ( s )$ and $y ( s )$ is given by

$$u (s) = K (s) y (s)$$

Define the transfer function that relates the controlled variable $\mathbf { \boldsymbol { z } } ( \mathbf { \boldsymbol { s } } )$ to the exogenous disturbance $w ( s )$ as $\Phi ( s )$ . Then

$$z (s) = \Phi (s) w (s)$$

Figure 10–46

A generalized plant diagram.

![](image/cb57cb2bc52ada4fc4e5cd26f05aaa83b22da2656ffd1f2227a52ac253119f9d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    z --> P11["P₁₁"]
    z --> P21["P₂₁"]
    P11 --> P12["P₁₂"]
    P21 --> P22["P₂₂"]
    P12 --> P11
    P22 --> P22
    P11 --> u
    P21 --> u
    P12 --> u
    P22 --> u
    u --> Ks["K(s)"]
    Ks --> P11
    Ks --> P21
    Ks --> P22
```
</details>

Note that can be determined as follows: Since£(s)
