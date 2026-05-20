# Antiwindup for the Input-Output Form

The corresponding construction can also be carried out for controllers characterized by input-output models. Consider a controller described by

$$R (q) u (k) = T (q) u _ {c} (k) - S (q) y (k) \tag {9.11}$$

where R, S, and T are polynomials in the forward-shift operator. The problem is to rewrite the equation so that it looks like a dynamic system with the observer dynamics driven by three inputs, the command signal $u_{c}$ , the process output y, and the control signal u. This is accomplished as follows.

Let $A_{aw}(q)$ be the desired characteristic polynomial of the antiwindup observer. Adding $A_{aw}(q)u(k)$ to both sides of (9.11) gives

$$A _ {c w} u = T u _ {c} - S y + (A _ {a w} - R) u$$

![](image/93a484311f9f9e5ae1df9b13deb2f74e77d4ac463101d60025805a9a4e5fc906.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    subgraph (a)
        A["u_c"] --> B["T"]
        C["y"] --> D["-S"]
        B --> E["Σ"]
        D --> E
        E --> F["1/R"]
        F --> G["u"]
    end
    subgraph (b)
        H["u_c"] --> I["T"]
        J["y"] --> K["-S"]
        L["Σ"] --> M["1/A_ow"]
        K --> M
        M --> N["v"]
        N --> O["Δ"]
        O --> P["u"]
        Q["A_ow-R"] --> R
    end
```
</details>

Figure 9.7 Block diagram of the controller of (9.11) and the modification in (9.12) that avoids windup.

A controller with antiwindup compensation is then given by

$$A _ {a w} v = T u _ {c} - S y + (A _ {a w} - R) u \tag {9.12}u = \text { sat } v$$

This controller is equivalent to (9.11) when it does not saturate. When the control variable saturates, it can be interpreted as an observer with dynamics given by polynomial $A_{ow}$ .

A block diagram of the linear controller of (9.11) and the nonlinear modification of (9.12) that avoids windup is shown in Fig. 9.7. A particularly simple case is that of a deadbeat observer, that is, $A_{ww}^{*} = 1$ . The controller can then be written as

$$u (k) = \operatorname{sat} \left(T ^ {*} (q ^ {- 1}) u _ {c} (k) - S ^ {*} (q ^ {- 1}) y (k) + \left(1 - R ^ {*} (q ^ {- 1})\right) u (k)\right) \tag {9.13}$$

An example illustrates the implementation.
