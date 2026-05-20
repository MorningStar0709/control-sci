<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E["s"] --> B["b/(a + b)"]
    B --> C["+"]
    C --> X["s"]
    X["s"] --> K["K"]
    K --> Pc["Pc(s)"]
    Pc --> A["A/(ks)"]
    A --> D["a/(a + b)"]
    D --> C
    C -->|-| C
```
</details>

(b)   
Figure 4–13   
(a) Pneumatic proportional controller; (b) block diagram of the controller.

Consider the pneumatic controller shown in Figure 4–13(a). Considering small changes in the variables, we can draw a block diagram of this controller as shown in Figure 4–13(b). From the block diagram we see that the controller is of proportional type.

We shall now show that the addition of a restriction in the negative feedback path will modify the proportional controller to a proportional-plus-derivative controller, or a PD controller.

Consider the pneumatic controller shown in Figure 4–14(a).Assuming again small changes in the actuating error, nozzle–flapper distance, and control pressure, we can summarize the operation of this controller as follows: Let us first assume a small step change in e.

![](image/e0b4da6b217030f88fc745af52a266dc5bff3e44203d7bfb72e5d92efdf88ff2.jpg)

<details>
<summary>text_image</summary>

P_s
\bar{X} + x
e
a
b
R
C
\bar{P}_c + p_c
</details>

(a)

![](image/06f5137acf6f24d3fd2fc35d49c85c4af14aef43de77ae99e3406e4150dc374e.jpg)

<details>
<summary>text_image</summary>

e
x
pc
t
</details>

(b)   
Figure 4–14   
(a) Pneumatic proportional-plusderivative controller; (b) step change in e and the corresponding changes in x and $p _ { c }$ plotted versus t; (c) block diagram of the controller.

![](image/8d96444202ef20920a302c517f83ede8717b11807d461a8731eb7b3c007da68f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E["s"] --> A["b/(a+b)"] --> B["+"]
    B --> X["s"]
    X["s"] --> K["K"]
    K --> P["c(s)"]
    P --> B
    B --> C["a/(a+b)"] --> D["A/k_s"] --> E["1/(RCs+1)"]
    E --> C
```
</details>

(c)
