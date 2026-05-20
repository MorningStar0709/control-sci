The observer is a subsystem to reconstruct the state vector of the plant. The mathematical model of the observer is basically the same as that of the plant, except that we include an additional term that includes the estimation error to compensate for inaccuracies in matrices A and B and the lack of the initial error. The estimation error or observation error is the difference between the measured output and the estimated output.The initial error is the difference between the initial state and the initial estimated state. Thus, we define the mathematical model of the observer to be

$$
\begin{array}{l} \dot {\widetilde {\mathbf {x}}} = \mathbf {A} \widetilde {\mathbf {x}} + \mathbf {B} u + \mathbf {K} _ {e} (y - \mathbf {C} \widetilde {\mathbf {x}}) \\ = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \widetilde {\mathbf {x}} + \mathbf {B} u + \mathbf {K} _ {e} y \tag {10-57} \\ \end{array}
$$

where is the estimated state and is the estimated output.The inputs to the observerC x- xare the output y and the control input u. Matrix K , which is called the observer gain matrix, is a weighting matrix to the correction term involving the difference between the measured output y and the estimated output $\mathbf { C } \widetilde { \mathbf { x } }$ This term continuously corrects. the model output and improves the performance of the observer. Figure 10–11 shows the block diagram of the system and the full-order state observer.

Figure 10–11 Block diagram of system and full-order state observer, when input u and output y are scalars.   
![](image/e5a4024ebe24da79dac8845c355b8a5e2d7a3fae4cc8bb92a5b4641e6d7f3e58.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u --> B1["B"]
    u --> B2["B"]
    B1 --> add1["+"]
    add1 --> int1["f"]
    int1 --> x["x"]
    x --> C["C"]
    C --> y["y"]
    y --> A["A"]
    A --> add1
    x --> int1
    x --> C
    C --> y
    y --> Ke["Ke"]
    Ke --> add2["+"]
    add2 --> int2["f"]
    int2 --> x2["x̃"]
    x2 --> C2["C"]
    C2 --> y2["ỹ"]
    y2 --> A2["A"]
    A2 --> add3["+"]
    add3 --> int3["f"]
    int3 --> x3["x̃"]
    x3 --> C3["C"]
    C3 --> y3["ỹ"]
    y3 --> Ke
```
</details>

Full-order state observer

Full-Order State Observer. The order of the state observer that will be discussed here is the same as that of the plant. Assume that the plant is defined by Equations (10–55) and (10–56) and the observer model is defined by Equation (10–57).

To obtain the observer error equation, let us subtract Equation (10–57) from Equation (10–55):
