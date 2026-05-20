Let us derive the transfer function between the displacement z and displacement y. Define the pressures existing on the right and left sides of the piston as $P _ { 1 } ( { \mathrm { l b } _ { \mathrm { f } } } / { \mathrm { i n } } . ^ { 2 } )$ and $P _ { 2 } ( \mathrm { l b } _ { \mathrm { f } } / \mathrm { i n } . ^ { 2 } )$ respectively. Suppose that the inertia force involved is negligible. Then the, force acting on the piston must balance the spring force. Thus

$$A \left(P _ {1} - P _ {2}\right) = k z$$

where A=piston area, in.2

$k = \mathrm { s p r i n g \ c o n s t a n t } , \mathrm { l b _ { f } / i n } .$

The flow rate q is given by

$$q = \frac {P _ {1} - P _ {2}}{R}$$

where q=flow rate through the restriction, lbsec

R=resistance to flow at the restriction, $\scriptstyle { \mathrm { l b } _ { \mathrm { f } } \mathrm { - s e c } / \mathrm { i n } . ^ { 2 } - \mathrm { l b } }$

Since the flow through the restriction during dt seconds must equal the change in the mass of oil to the left of the piston during the same dt seconds, we obtain

$$q d t = A \rho (d y - d z)$$

where $\rho = \mathrm { d e n s i t y } , \mathrm { l b } / \mathrm { i n } . ^ { 3 }$ . (We assume that the fluid is incompressible or $\rho = { \mathrm { c o n s t a n t . } } )$ This last equation can be rewritten as

$$\frac {d y}{d t} - \frac {d z}{d t} = \frac {q}{A \rho} = \frac {P _ {1} - P _ {2}}{R A \rho} = \frac {k z}{R A ^ {2} \rho}$$

![](image/c871a91eb32ee7c9c5ca49a56cd83372ea5518aa066670344e93950240cb4fb8.jpg)

<details>
<summary>text_image</summary>

q
R
P2
P1
A
k
y
z
</details>

(a)

![](image/d8f5f6a55ca6a136c28dc3c423b6b756da2c5ab0cd73d50c6249a2ea1f1d963b.jpg)

<details>
<summary>text_image</summary>

y
z
t
</details>

(b)

![](image/a015624a2eae8fdb7d76eb3373be5c665b744d7b4bde41b56db735daf0a74f34.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    Ys["Y(s)"] --> adder["+"]
    adder --> Zs["Z(s)"]
    Zs -->|T = RA²ρ/k| transfer["1/Ts"]
    transfer --> adder
```
</details>

(c)   
Figure 4–21 (a) Dashpot; (b) step change in y and the corresponding change in z plotted versus t; (c) block diagram of the dashpot.

or

$$\frac {d y}{d t} = \frac {d z}{d t} + \frac {k z}{R A ^ {2} \rho}$$

Taking the Laplace transforms of both sides of this last equation, assuming zero initial conditions, we obtain

$$s Y (s) = s Z (s) + \frac {k}{R A ^ {2} \rho} Z (s)$$

The transfer function of this system thus becomes

$$\frac {Z (s)}{Y (s)} = \frac {s}{s + \frac {k}{R A ^ {2} \rho}}$$
