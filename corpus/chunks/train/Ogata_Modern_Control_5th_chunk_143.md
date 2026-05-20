Consider the pneumatic controller shown in Figure 4–15(a).The operation of this controller is as follows: The bellows denoted by I is connected to the control pressure source without any restriction. The bellows denoted by II is connected to the control pressure source through a restriction. Let us assume a small step change in the actuating error.This will cause the back pressure in the nozzle to change instantaneously.Thus a change in the control pressure $p _ { c }$ also occurs instantaneously. Due to the restriction of the valve in the path to bellows II, there will be a pressure drop across the valve. As time goes on, air will flow across the valve in such a way that the change in pressure in bellows II attains the value $p _ { c }$ . Thus bellows II will expand or contract as time elapses in such a way as to move the flapper an additional amount in the direction of the original displacement e.This will cause the back pressure $p _ { c }$ in the nozzle to change continuously, as shown in Figure 4–15(b).

![](image/55ef8622e7728c75a0a0da11552a15ce61e3273abcb03d786d42008e8f7d8362.jpg)

<details>
<summary>text_image</summary>

P_s
R
C
I
II
e
X̄ + x
a
b
P̄_c + p_c
</details>

(a)

![](image/25e916b9b91d45f47306b16edcf87a41ca582f50d66a4d2cbd2887f9ad1250a1.jpg)  
(b)

![](image/2fc44b52424f089bb28da24e99d47b98a8210266f98eaa43e7139f4240391fff.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E["s"] --> B["b/(a+b)"] --> A["+/-"] --> C["+/-"] --> X["s"]
    X["s"] --> K["K"] --> Pc["s"]
    Pc["s"] --> A2["A/(k_s)"] --> RCs1["1/(RCs+1)"] --> A3["A/(k_s)"] --> C2["+/-"]
    C2 --> A4["a/(a+b)"] --> A5["a/(a+b)"] --> A6["A/(k_s)"]
    A6 --> C2
    C2 -->|feedback| A4
```
</details>

(c)

![](image/fa7789ef37b65eea7230d55f9d87d421abde2ed6ca01c1f1ca8a1059334fa526.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E["s"] --> B["b/(a+b)"] --> Add1["+"]
    Add1 --> X["s"]
    X["s"] --> K["K"]
    K --> Pc["s"]
    Pc --> D["1/(RCs+1)"]
    D --> Add2["+"]
    Add2 --> A["a/(a+b)/A/ks"]
    A --> Add1
    Add1 --> B
    Add2 --> B
```
</details>

(d)

Note that the integral control action in the controller takes the form of slowly canceling the feedback that the proportional control originally provided.
