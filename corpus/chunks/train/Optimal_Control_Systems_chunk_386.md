```mermaid
graph TD
    A["λ(t)=-A' λ(t)"] -->|λ*(t)| B["-B'"]
    B -->|-q*(t)| C["+1"]
    C --> D["u*(t)"]
    D --> E["ẋ(t)=Ax(t)+Bu(t)"]
    E --> F["x*(t)"]
    F --> G["Plant"]
    H["Stop Iteration"] --> I{x(tf)=0?}
    J["Start Iteration/Change λ(0)"] --> I
    I -->|Yes| K["λ(0)"]
    I -->|No| L["λ(t)"]
    K --> M["Relay"]
    L --> M
    M --> N["x(0)"]
```
</details>

Figure 7.5 Open-Loop Structure for Time-Optimal Control System

(a) The adjoint system (7.1.19) has unstable modes for a stable system (7.1.10). This makes the already an iterative procedure much more tedious.

(b) We all know the obvious disadvantages of the open-loop implementation of a control system.

One should try for closed-loop implementation of the time-optimal control system, which is discussed next.

2. Closed-Loop Structure: Intuitively, we can feel the relation between the control $\mathbf{u}^{*}(t)$ and the state $\mathbf{x}^{*}(t)$ recalling the results of Chapters 3 and 4 where we used Riccati transformation $\lambda^{*}(t) = \mathbf{P}(t)\mathbf{x}^{*}(t)$ to express the optimal control $\mathbf{u}^{*}(t)$ , which was a function of the costate $\lambda^{*}(t)$ , as a function of the state $\mathbf{x}^{*}(t)$ . Thus, we assume that at any time there is a time-optimal control $\mathbf{u}^{*}(t)$ as a function of the state $\mathbf{x}^{*}(t)$ . That is, there is a switching function $\mathbf{h}(\mathbf{x}^{*}(t))$ such that

$$\boxed {\mathbf {u} ^ {*} (t) = - S G N \left\{\mathbf {h} \left(\mathbf {x} ^ {*} (t)\right) \right\}} \tag {7.1.42}$$

where an analytical and/or computational algorithm

$$\mathbf {h} (\mathbf {x} ^ {*} (t)) = \mathbf {B} ^ {\prime} \boldsymbol {\lambda} ^ {*} (\mathbf {x} ^ {*} (t)). \tag {7.1.43}$$

needs to be developed as shown in the example to follow. Then, the optimal control law (7.1.42) is implemented as shown in Figure 7.6. The relay implements the optimal control depending on its input which in turn is decided by the feedback of the states. The determination of the switching functions $\mathbf{h}[\mathbf{x}^{*}(t)]$ is the important aspect of the implementation of the control law. In the next section, we demonstrate the way we try to obtain the closed-loop structure for time-optimal control system of a second order (double integral) system.
