$$\mathbf {u} _ {n} ^ {*} (t) = - \mathbf {q} ^ {*} (t) = \mathbf {u} ^ {*} (t) \text { if } | \mathbf {q} ^ {*} (t) | \leq 1 \tag {7.5.33}$$

where $\mathbf{u}^{*}(t)$ refers to constrained control. Thus, if $\mathbf{q}^{*}(t) \leq 1$ , the constrained optimal control $\mathbf{u}^{*}(t)$ and the unconstrained optimal control $\mathbf{u}^{*}(t)$ are the same.

5. For the constrained energy-optimal control system, using optimal control (7.5.31), the state and costate system (7.5.7)

becomes

$$\dot {\mathbf {x}} ^ {*} (t) = \mathbf {A} \mathbf {x} ^ {*} (t) - \mathbf {B} S A T \left\{\mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t) \right\}\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \mathbf {A} ^ {\prime} \boldsymbol {\lambda} ^ {*} (t). \tag {7.5.34}$$

We notice that this is a set of 2n nonlinear differential equations and can only be solved by using numerical simulations.

\- Step 5: Implementation: The implementation of the energy-optimal control law (7.5.31) can be performed in open-loop or closed-loop configuration. In the open-loop case (Figure 7.38), it becomes iterative to try different values of initial conditions for $\lambda(0)$ to satisfy the final condition of driving the state to origin. On the other hand, the closed-loop case shown in Figure 7.39 becomes more attractive.

![](image/1a76b650ff3272790b9c5ea857509f7efd207aecaebeb9ddfdb5263b875168d3.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["λ(t)=-A' λ(t)"] --> B["λ*(t)"]
    B --> C["-R'-B'"]
    C --> D["-q*(t)"]
    D --> E["Saturation"]
    E --> F["u*(t)"]
    F --> G["ẋ(t)=Ax(t)+Bu(t)"]
    G --> H["x*(t)"]
    I["Start Iteration/Change λ(0)"] --> J{Is x(tf)=0?}
    J -->|Yes| K["Stop Iteration"]
    J -->|No| L["λ(0)"]
    K --> M["Open-Loop Energy-Optimal Controller"]
    L --> M
    M --> N["Plant"]
```
</details>

Figure 7.38 Open-Loop Implementation of Energy-Optimal Control System

A more general constrained minimum-energy control system is where the performance measure (7.5.3) contains additional weighting terms $\mathbf{x}^{\prime}(t)\mathbf{Q}(t)\mathbf{x}(t)$ and $2\mathbf{x}(t)\mathbf{S}(t)\mathbf{u}(t)$ [6].
