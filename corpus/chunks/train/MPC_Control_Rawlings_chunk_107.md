The state and the additional integrating disturbance are estimated from the plant measurement using a Kalman filter designed for the augmented system. The variances of the stochastic disturbances w and v may be treated as adjustable parameters or found from inputoutput measurements (Odelson, Rajamani, and Rawlings, 2006). The estimator provides ${ \hat { x } } ( k )$ and $\hat { d } ( k )$ at each time k. The best forecast of the steady-state disturbance using (1.43) is simply

$$\hat {d} _ {s} = \hat {d} (k)$$

The steady-state target problem is therefore modified to account for the nonzero disturbance $\hat { d } _ { s }$

$$\min _ {x _ {s}, u _ {s}} \frac {1}{2} \left(\left| u _ {s} - u _ {\mathrm{sp}} \right| _ {R _ {s}} ^ {2} + \left| C x _ {s} + C _ {d} \hat {d} _ {s} - y _ {\mathrm{sp}} \right| _ {Q _ {s}} ^ {2}\right) \tag {1.46a}$$

![](image/390b46636f5398bee9de9e112fe615b7b04b184b4002e1115fcbe5ca179c67a9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["target selector"] --> B["regulator"]
    A --> C["estimator"]
    B --> D["plant"]
    C --> D
    D --> E["y"]
    F["x_s, u_s, x̂"] --> B
    G["y_sp, u_sp, r_sp, (Q_s, R_s)"] --> A
    H["\tilde{x}^+ = A\underline{x} + B\underline{u}(Q,R)"] --> B
    I["\hat{x}, \hat{d}"] --> C
    J["\left[ \begin{array}{c} \hat{x} \\ \hat{d} \end{array} \right"]^+ = \begin{bmatrix} A & B_d \\ 0 & I \end{bmatrix} \begin{bmatrix} \hat{x} \\ \hat{d} \end{bmatrix} + \begin{bmatrix} B \\ 0 \end{bmatrix} u+] --> K["\left[ \begin{array}{c} L_x \\ L_d \end{array} \right"] \left( y - \left[" C C_d \right"] \begin{bmatrix} \hat{x} \\ \hat{d} \end{bmatrix} \right)]
    K --> L["\hat{x}, \hat{d}"]
    L --> M["\hat{x}"]
```
</details>

Figure 1.5: MPC controller consisting of: receding horizon regulator, state estimator, and target selector.

subject to:

$$
\left[ \begin{array}{c c} I - A & - B \\ H C & 0 \end{array} \right] \left[ \begin{array}{l} x _ {s} \\ u _ {s} \end{array} \right] = \left[ \begin{array}{c} B _ {d} \hat {d} _ {s} \\ r _ {\mathrm{sp}} - H C _ {d} \hat {d} _ {s} \end{array} \right] \tag {1.46b}
E u _ {s} \leq e \tag {1.46c}F C x _ {s} \leq f - F C _ {d} \hat {d} _ {s} \tag {1.46d}
$$

Comparing (1.42) to (1.46), we see the disturbance model affects the steady-state target determination in four ways.
