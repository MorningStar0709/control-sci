Minimum-variance control may result in large control signals. One way to decrease the variation of the control signal is to generalize the loss function such that it also contains a penalty on the control signal. Linear quadratic controllers are of this type; a minor drawback with linear quadratic self-tuning regulators is the computational burden. One way to simplify the problems is to use a loss function of the form

$$E \left\{\left(P ^ {*} (q ^ {- 1}) y (t + d _ {0})\right) ^ {2} + \left(Q ^ {*} (q ^ {- 1}) u (t)\right) ^ {2} \mid \mathcal {Y} _ {t} \right\}$$

where

$$\mathcal {Y} _ {t} = \{y (t), y (t - 1), \dots , y (0), u (t), u (t - 1), \dots , u (0) \}$$

that is, the data available at time t. The resulting controller is sometimes called a generalized minimum-variance controller. This controller can be interpreted in the same framework as above. To illustrate this, assume that $P^{*} = 1$ and that $Q^{*} = \sqrt{\rho}$ . This gives the loss function

$$E \left\{y ^ {2} (t + d _ {0}) + \rho u ^ {2} (t) \mid \mathcal {Y} _ {t} \right\} \tag {4.36}$$

Notice that the loss function depends only on the output y at time $t + d_{0}$ , that is, at only one time instant. Loss functions of the form (4.36) are sometimes called one-stage loss functions.

![](image/67e4950415bcf1dcdb119e54780f724801c6425bfac3935473a8baa3d2d29212.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph_Original_system["Original system"]
        A1["A* y = q^(-d₀) B* u + C* e"] -->|e| A2["A* y = q^(-d₀) B* u + C* e"]
        A2 -->|u| A3["-S* / (R* + ρ/ r₀ C*)"]
        A3 -->|y| A4["y"]
    end
    subgraph_Augmented_system["Augmented system"]
        B1["A* y = q^(-d₀) B* u + C* e"] -->|e| B2["A* y = q^(-d₀) B* u + C* e"]
        B2 -->|u| B3["ρ/ r₀ q^(-d₀)"]
        B3 -->|y| B4["Σ"]
        B4 -->|yₐ| B5["y_a"]
    end
    style Original_system fill:#f9f,stroke:#333
    style Augmented_system fill:#bbf,stroke:#333
```
</details>

Figure 4.9 Equivalent systems.

Assume that the process is governed by Eq. (4.1). By using the representation of the process dynamics given by Eq. (4.21) it can be shown that the control law that minimizes Eq. (4.36) is

$$\left(R ^ {*} + \frac {\rho}{r _ {0}} C ^ {*}\right) u (t) = - S ^ {*} y (t) \tag {4.37}$$

where

$$R ^ {*} = R _ {1} ^ {*} B ^ {*}$$

and $R^{*}$ and $S^{*}$ are given by Eq. (4.16).
