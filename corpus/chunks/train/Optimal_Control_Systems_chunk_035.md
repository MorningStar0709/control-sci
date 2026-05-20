# 1.1 Classical and Modern Control

The classical (conventional) control theory concerned with single input and single output (SISO) is mainly based on Laplace transforms theory and its use in system representation in block diagram form. From Figure 1.1, we see that

$$\frac {Y (s)}{R (s)} = \frac {G (s)}{1 + G (s) H (s)} \tag {1.1.1}$$

![](image/5e679b4f5584caaae84a41f86ad8e68ac801af34267b5d73be27773c026915f3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Reference Input R(s)"] --> B((+))
    B --> C["Error Signal E(s)"]
    C --> D["Compensator Gc(s)"]
    D --> E["Control Input U(s)"]
    E --> F["Plant Gp(s)"]
    F --> G["Output Y(s)"]
    G --> H["Feedback H(s)"]
    H --> B
```
</details>

Figure 1.1 Classical Control Configuration

where $s$ is Laplace variable and we used

$$G (s) = G _ {c} (s) G _ {p} (s). \tag {1.1.2}$$

Note that

1. the input $u(t)$ to the plant is determined by the error $e(t)$ and the compensator, and   
2. all the variables are not readily available for feedback. In most cases only one output variable is available for feedback.

The modern control theory concerned with multiple inputs and multiple outputs (MIMO) is based on state variable representation in terms of a set of first order differential (or difference) equations. Here, the system (plant) is characterized by state variables, say, in linear, time-invariant form as

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \tag {1.1.3}\mathbf {y} (t) = \mathbf {C x} (t) + \mathbf {D u} (t) \tag {1.1.4}$$

where, dot denotes differentiation with respect to (w.r.t.) t, $\mathbf{x}(t)$ , $\mathbf{u}(t)$ , and $\mathbf{y}(t)$ are n, r, and m dimensional state, control, and output vectors respectively, and A is nxn state, B is nxr input, C is mxn output, and D is mxr transfer matrices. Similarly, a nonlinear system is characterized by

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {1.1.5}\mathbf {y} (t) = \mathbf {g} (\mathbf {x} (t), \mathbf {u} (t), t). \tag {1.1.6}$$

The modern theory dictates that all the state variables should be fed back after suitable weighting. We see from Figure 1.2 that in modern control configuration,
