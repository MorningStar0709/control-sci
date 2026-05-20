# Example 7.1

Consider a simple scalar system

$$\dot {x} (t) = a x (t) + u (t), \quad a < 0 \tag {7.5.35}$$

![](image/5084c5f37f3e2a76e7afce1f63b366b06e4a115f763e9e973bacea8b831b727a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["x*(t)"] --> B["Algorithm"]
    B --> C["h[x*(t)"]]
    C --> D["Saturation"]
    D --> E["u*(t)"]
    E --> F["\dot{x}(t)=Ax(t)+Bu(t)"]
    F --> G["x*(t)"]
    G --> H["Plant"]
    style A fill:#f9f,stroke:#333
    style G fill:#f9f,stroke:#333
    subgraph Closed-Loop Energy-Optimal Controller
        B
        C
        D
        E
        F
    end
    subgraph Plant
        G
    end
```
</details>

Figure 7.39 Closed-Loop Implementation of Energy-Optimal Control System

to be transferred from an arbitrary initial state $x(t = 0) = x_{0}$ to the origin that minimize the performance index

$$J = \int_ {0} ^ {t _ {f}} u ^ {2} (t) d t \tag {7.5.36}$$

where, the final time $t_f$ is free and the control $u(t)$ is constrained as

$$| u (t) | \leq 1. \tag {7.5.37}$$

Discuss the resulting optimal control system.

Solution: Comparing the system (7.5.35) and the performance measure (7.5.36) with the general formulations of the corresponding system (7.5.2) and the performance index (7.5.3), we easily see that $\mathbf{A}(t)=a,\mathbf{B}(t)=b=1,\mathbf{R}(t)=r=2$ . Then using the step-by-step procedure in the last section, we get the following.

\- Step 1: Form the Hamiltonian (7.5.6) as

$$\mathcal {H} (x (t), \lambda (t), u (t)) = \frac {1}{2} \mathrm{x} 2 u ^ {2} (t) + \lambda (t) a x (t) + \lambda (t) u (t). \tag {7.5.38}$$

\- Step 2: The state and costate relations (7.5.7) are

$$\dot {x} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \lambda}\right) _ {*} = a x ^ {*} (t) + u ^ {*} (t)\dot {\lambda} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial x}\right) _ {*} = - a \lambda^ {*} (t). \tag {7.5.39}$$

The solution of the costate function $\lambda^{*}(t)$ is easily seen to be

$$\lambda^ {*} (t) = \lambda (0) \epsilon^ {- a t}. \tag {7.5.40}$$

\- Step 3: The optimal control (7.5.30) becomes

$$
\begin{array}{l} u ^ {*} (t) = - \operatorname{sat} \left\{q _ {i} ^ {*} (t) \right\} \\ = - s a t \left\{r ^ {- 1} b \lambda^ {*} (t) \right\} \\ = - s a t \left\{0. 5 \lambda^ {*} (t) \right\}. \tag {7.5.41} \\ \end{array}
$$

In other words,
