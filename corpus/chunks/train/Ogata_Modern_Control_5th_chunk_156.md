Let us define $R A ^ { 2 } \rho / k = T$ . (Note that $R A ^ { 2 } \rho / k$ has the dimension of time.) Then

$$\frac {Z (s)}{Y (s)} = \frac {T s}{T s + 1} = \frac {1}{1 + \frac {1}{T s}}$$

Clearly, the dashpot is a differentiating element. Figure 4–21(c) shows a block diagram representation for this system.

Obtaining Hydraulic Proportional-Plus-Integral Control Action. Figure 4–22(a) shows a schematic diagram of a hydraulic proportional-plus-integral controller.A block diagram of this controller is shown in Figure 4–22(b). The transfer function $Y ( s ) / E ( s )$ is given by

$$\frac {Y (s)}{E (s)} = \frac {\frac {b}{a + b} \frac {K}{s}}{1 + \frac {K a}{a + b} \frac {T}{T s + 1}}$$

![](image/f6774dff9afef85dcd1924ec9f890169073e4826e826ce9132cd546215269666.jpg)

<details>
<summary>text_image</summary>

Oil under pressure
Spring constant = k
a
b
Area = A
Density of oil = ρ
Resistance = R
(a)
</details>

![](image/f8ae332f6bf148b628d4e1bd221a2986f65cb8654fb030c55fe3ededa87df4e4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["E(s)"] --> B["b/(a+b)"]
    B --> C["+"]
    C --> D["X(s)"]
    D --> E["K/s"]
    E --> F["Y(s)"]
    F --> G["Z(s)"]
    G --> H["a/(a+b)"]
    H --> C
    C --> I["Ts/(Ts+1)"]
    I --> J["Feedback"]
    J --> C
```
</details>

Figure 4–22 (a) Schematic diagram of a hydraulic proportional-plus-integral controller; (b) block diagram of the controller.

In such a controller, under normal operation $\big | K a T / \big [ ( a + b ) ( T s + 1 ) \big ] \big | \gg 1$ with the, result that

$$\frac {Y (s)}{E (s)} = K _ {p} \bigg (1 + \frac {1}{T _ {i} s} \bigg)$$

where

$$K _ {p} = \frac {b}{a}, \qquad T _ {i} = T = \frac {R A ^ {2} \rho}{k}$$

Thus the controller shown in Figure 4–22(a) is a proportional-plus-integral controller (PI controller).

Obtaining Hydraulic Proportional-Plus-Derivative Control Action. Figure 4–23(a) shows a schematic diagram of a hydraulic proportional-plus-derivative controller. The cylinders are fixed in space and the pistons can move. For this system, notice that

$$k (y - z) = A \left(P _ {2} - P _ {1}\right)q = \frac {P _ {2} - P _ {1}}{R}q d t = \rho A d z$$

Hence

$$y = z + \frac {A}{k} q R = z + \frac {R A ^ {2} \rho}{k} \frac {d z}{d t}$$

or

$$\frac {Z (s)}{Y (s)} = \frac {1}{T s + 1}$$

![](image/873bed9ba00f276e233ab0f370025f2f1412db7ec903b9983cc8e7cac2e6289e.jpg)

<details>
<summary>text_image</summary>

e
a
x
b
z
R
P2 P1
q
k
Area = A
y
Density of oil = ρ
</details>

(a)
