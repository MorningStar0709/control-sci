![](image/ea035cf12fca108f0cb0c3b6e48108cb4ad90b0a688bebd470d0248939d3a333.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["E(s)"] --> B["b/(a+b)"]
    B --> C["+"]
    C --> D["X(s)"]
    D --> E["K/s"]
    E --> F["Y(s)"]
    F --> G["1/(Ts+1)"]
    G --> H["Z(s)"]
    H --> I["a/(a+b)"]
    I --> C
```
</details>

(b)   
Figure 4–23 (a) Schematic diagram of a hydraulic proportional-plus-derivative controller; (b) block diagram of the controller.

where

$$T = \frac {R A ^ {2} \rho}{k}$$

A block diagram for this system is shown in Figure 4–23(b). From the block diagram the transfer function $Y ( s ) / E ( s )$ can be obtained as

$$\frac {Y (s)}{E (s)} = \frac {\frac {b}{a + b} \frac {K}{s}}{1 + \frac {a}{a + b} \frac {K}{s} \frac {1}{T s + 1}}$$

Under normal operation we have $\big | a K / \big [ ( a + b ) s ( T s + 1 ) \big ] \big | \gg 1$ Hence.

$$\frac {Y (s)}{E (s)} = K _ {p} (1 + T s)$$

where

$$K _ {p} = \frac {b}{a}, \quad T = \frac {R A ^ {2} \rho}{k}$$

Thus the controller shown in Figure 4–23(a) is a proportional-plus-derivative controller (PD controller).

Obtaining Hydraulic Proportional-Plus-Integral-Plus-Derivative Control Action. Figure 4–24 shows a schematic diagram of a hydraulic proportional-plus-integral-plusderivative controller. It is a combination of the proportional-plus-integral controller and proportional-plus derivative controller.

If the two dashpots are identical except the piston shafts, the transfer function $Z ( s ) / Y ( s )$ can be obtained as follows:

$$\frac {Z (s)}{Y (s)} = \frac {T _ {1} s}{T _ {1} T _ {2} s ^ {2} + \left(T _ {1} + 2 T _ {2}\right) s + 1}$$

(For the derivation of this transfer function, refer to Problem A–4–9.)

Figure 4–24 Schematic diagram of a hydraulic proportional-plusintegral-plusderivative controller.   
![](image/aa274d0a72c438ea57f935d034c16d739cc7cbc4591dafde8ad442d026dc3205.jpg)

<details>
<summary>text_image</summary>

e
a
x
b
R
R
k₁
z
k₂
Area = A
y
</details>

Figure 4–25 Block diagram for the system shown in Figure 4–24.   
![](image/e28a80b16731889c6717df5cfc89680b4a249c1f07d9044f423fdfe8ac5f2460.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E["s"] --> A["\frac{b}{a + b}"]
    A --> B["+"]
    B --> C["X(s)"]
    C --> D["\frac{K}{s}"]
    D --> Y["s"]
    Y["s"] --> E["s"]
    E["s"] --> F["\frac{a}{a + b}"]
    F --> G["Z(s)"]
    G --> H["\frac{T_1 s}{T_1 T_2 s^2 + (T_1 + 2T_2)s + 1}"]
    H --> I["Feedback"]
    I --> B
```
</details>
