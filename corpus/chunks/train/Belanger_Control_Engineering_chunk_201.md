# Example 4.4 (Level Control)

In the level-control system of Example 2.8, the transfer function from the valve stroke u to the level is $\Delta\ell/\Delta u = (-2.0)/(s + .005)$ , and the transfer function relating the disturbance input to the level is $\Delta\ell/\Delta F_{in} = 1/(s + .005)$ . Design a feedforward compensator to cancel out the effect of the disturbance.

![](image/b39b8d91d6256b2990dd3058cafef7f15f46d56ff989ac500c4be3b4c71f53db.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["u"] --> B["P"]
    B --> C["y'"]
    C --> D["+"]
    D --> E["y"]
    F["w"] --> G["Pw"]
    G --> H["d"]
    H --> D
```
</details>

(a)

![](image/18c9c33035001ef5db804d4c98f4dfb0f80cc82638813a4e3fe9ed090c2c56c8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["y_d = -d"] --> B["F"]
    B --> C["P"]
    C --> D["y'"]
```
</details>

(b)

![](image/de8600e0be1a7a8016b745abb412a9603cb8f8c34e78300ca7f7ab9a2a576bf1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["+"] --> B["F"]
    B --> C["P"]
    C --> D["+"]
    D --> E["y"]
    F["d"] --> G["P_w"]
    G --> H["w"]
    H --> I["P_w"]
    I --> D
```
</details>

(c)   
Figure 4.14 Development of the feedforward system

Solution The plant is stable and minimum-phase, so we pick $H_{d}(s) = 1$ , and therefore

$$F (s) = \frac {s + . 0 0 5}{- 2}.$$

The final step is to generate $y_{d} = -d$ , or

$$y _ {d} = \frac {- 1}{s + . 0 0 5} \Delta F _ {\mathrm{in}}$$

and therefore

$$\Delta u = F (s) y _ {d} = \frac {1}{2} \Delta F _ {\mathrm{in}}.$$

In this simple case, feedforward control requires the valve to open immediately upon sensing a change of flow into the tank. If the models are exact, the compensation is perfect.
