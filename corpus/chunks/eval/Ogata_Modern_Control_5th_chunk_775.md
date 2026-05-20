$$\dot {\widetilde {\mathbf {x}}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C} - \mathbf {B K}\right) \widetilde {\mathbf {x}} + \mathbf {K} _ {e} y$$

or

$$
\begin{array}{l} \left[ \begin{array}{c} \tilde {\dot {x}} _ {1} \\ \tilde {\dot {x}} _ {2} \end{array} \right] = \left\{\left[ \begin{array}{c c} 0 & 1 \\ 2 0. 6 & 0 \end{array} \right] - \left[ \begin{array}{c} 1 6 \\ 8 4. 6 \end{array} \right] [ 1 \quad 0 ] - \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] [ 2 9. 6 \quad 3. 6 ] \right\} \left[ \begin{array}{c} \tilde {x} _ {1} \\ \tilde {x} _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 6 \\ 8 4. 6 \end{array} \right] y \\ = \left[ \begin{array}{c c} - 1 6 & 1 \\ - 9 3. 6 & - 3. 6 \end{array} \right] \left[ \begin{array}{c} \widetilde {x} _ {1} \\ \widetilde {x} _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 6 \\ 8 4. 6 \end{array} \right] y \\ \end{array}
$$

The block diagram of the system with observed-state feedback is shown in Figure 10–14(a).

![](image/2607586d1c1de441bbccc2c86a98a3d9b61b6f61dc00c29f9e20ea4cd648afec.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph_Block_A["Block A"]
        A1["0/1"] --> Add1["+"]
        Add1 --> S1["f"]
        S1 --> C1["1 0"]
        C1 --> y["y"]
        A2["0/20.6 0"] --> Add1
        Add1 --> S2["f"]
        S2 --> C2["1 0"]
        C2 --> y["y"]
        Add2["0/3.6"] --> Add2
        Add2 --> S3["f"]
        S3 --> C3["1 0"]
        C3 --> y["y"]
        Add3["0/20.6 0"] --> Add3
        Add3 --> S4["f"]
        S4 --> C4["1 0"]
        C4 --> y["y"]
    end
    subgraph_Block_B["Block B"]
        B1["0/1"] --> Add4["+"]
        Add4 --> S5["f"]
        S5 --> C5["1 0"]
        C5 --> y["y"]
        Add5["0/84.6"] --> Add5
        Add5 --> S6["f"]
        S6 --> C6["1 0"]
        C6 --> y["y"]
    end
    x["x"] --> S1
    x --> S2
    x --> S3
    x --> S4
    x --> S5
    x --> S6
    x --> S7
    x --> S8
    x --> S9
    x --> S10
    x --> S11
    x --> S12
    x --> S13
    x --> S14
    x --> S15
    x --> S16
    x --> S17
    x --> S18
    x --> S19
    x --> S20
    x --> S21
    x --> S22
    x --> S23
    x --> S24
    x --> S25
    x --> S26
    x --> S27
    x --> S28
    x --> S29
    x --> S30
    u["u"] --> Add4
    -x̃[x̃] --> Add4
    -K["-K"] --> Add4
    +X["+"] --> Add5
    +Y["+"] --> Add5
    +Z["+"] --> Add5
    +X["+"] --> Add6
    +Y["+"] --> Add6
    +Z["+"] --> Add6
```
</details>

Figure 10–14 (a) Block diagram of system with observed-state feedback; (b) block diagram of transferfunction system.   
![](image/d137a89c098e66964ea4013c7f4797e5134876b7d627228c15f1103232199c3d.jpg)

<details>
<summary>flowchart</summary>
