# EXAMPLE 2–2

![](image/eaa2ea63086a95b34a088a93aa251c7d01e95ac2dbf9a3a2aa52f6598e7426fb.jpg)

<details>
<summary>text_image</summary>

k
u(t)
m
y(t)
b
</details>

Figure 2–15 Mechanical system.

Consider the mechanical system shown in Figure 2–15. We assume that the system is linear. The external force $u ( t )$ is the input to the system, and the displacement $y ( t )$ of the mass is the output. The displacement $y ( t )$ is measured from the equilibrium position in the absence of the external force. This system is a single-input, single-output system.

From the diagram, the system equation is

$$m \ddot {y} + b \dot {y} + k y = u \tag {2-16}$$

This system is of second order. This means that the system involves two integrators. Let us define state variables $x _ { 1 } ( t )$ and $x _ { 2 } ( t )$ as

$$x _ {1} (t) = y (t)x _ {2} (t) = \dot {y} (t)$$

Then we obtain

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = \frac {1}{m} (- k y - b \dot {y}) + \frac {1}{m} u$$

or

$$\dot {x} _ {1} = x _ {2} \tag {2-17}\dot {x} _ {2} = - \frac {k}{m} x _ {1} - \frac {b}{m} x _ {2} + \frac {1}{m} u \tag {2-18}$$

The output equation is

$$y = x _ {1} \tag {2-19}$$

Figure 2–16 Block diagram of the mechanical system shown in Figure 2–15.   
![](image/1803d63da7b3bf84a48445c782d183623081d04eae0a06a682a6879c91a78fc6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    u --> A["1/m"]
    A --> B["+"]
    B --> C["∫"]
    C --> D["x2"]
    D --> E["∫"]
    E --> F["x1 = y"]
    F --> G["k/m"]
    G --> H["+"]
    H --> I["b/m"]
    I --> J["∫"]
    J --> K["x2"]
    K --> L["∫"]
    L --> M["x1 = y"]
    M --> N["k/m"]
    N --> O["+"]
    O --> P["b/m"]
    P --> Q["∫"]
    Q --> R["x2"]
    R --> S["∫"]
    S --> T["x1 = y"]
```
</details>

In a vector-matrix form, Equations (2–17) and (2–18) can be written as

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \frac {k}{m} & - \frac {b}{m} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ \frac {1}{m} \end{array} \right] u \tag {2-20}
$$

The output equation, Equation (2–19), can be written as

$$
y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] \tag {2-21}
$$

Equation (2–20) is a state equation and Equation (2–21) is an output equation for the system. They are in the standard form:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x} + D u$$

where
