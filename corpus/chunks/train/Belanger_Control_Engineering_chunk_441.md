$$
\begin{array}{l} \Delta \dot {\widehat {\mathbf {x}}} = A \Delta \widehat {\mathbf {x}} + B \Delta \mathbf {u} + G (\Delta \mathbf {y} - C \Delta \widehat {\mathbf {x}}) \\ = A \Delta \widehat {\mathbf {x}} - B K \Delta \widehat {\mathbf {x}} + G (\Delta \mathbf {y} - C \Delta \widehat {\mathbf {x}}) \\ \end{array}
$$

![](image/04f6f38e28281c7888266a585b956e68939ec33d4edfcb735540c3967965cc12.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    yd --> +
    + --> e["-Δy"]
    e --> Observer
    Observer --> Δx̂
    Δx̂ --> K
    K --> Δu
    Δu --> +
    + --> u
    u --> Plant
    Plant --> y
    yd --> -["-"]
    - --> +
    + --> u*
    u* --> +
```
</details>

Figure 7.24 Block diagram of an observer-based control system

or

$$\Delta \dot {\widehat {\mathbf {x}}} = (A - B K - G C) \Delta \widehat {\mathbf {x}} + G \Delta \mathbf {y} \tag {7.90}\Delta \mathbf {u} = - K \Delta \widehat {\mathbf {x}}. \tag {7.91}$$

Equations 7.90 and 7.91 are state equations. The corresponding transfer function equation is

$$\Delta \mathbf {u} (s) = - K (s I - A + B K + G C) ^ {- 1} G \Delta \mathbf {y} (s) \tag {7.92}$$

or, in terms of e rather than $\Delta y$ ,

$$\Delta \mathbf {u} (s) = K (s I - A + B K + G C) ^ {- 1} G \mathbf {e} (s). \tag {7.93}$$

If some of the states are directly measured, a reduced-order observer may be used. The measured states appear alongside $\Delta y$ , as additional inputs.
