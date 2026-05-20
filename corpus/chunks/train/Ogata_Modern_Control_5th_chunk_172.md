Note : The sum of gain block and summation points be calculated by adding a factor to the sum of gains from s - t - 1.
Note : The_sum_of_gain_block_and_summation_points_be_calculated_by_adding_a_function["k_s / (T_d * s + 1)"] = (k_s / (T_i * s + 1)) * (k_s / (T_d * s + 1)).
```
</details>

(a)   
Figure 4–31   
(a) Block diagram of the pneumatic controller shown in Figure 4–30; (b) simplified block diagram.

![](image/7d41144550c16665a3a47c1d26dce262f104ba91b774d53ba6bc1da765065e51.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["E(s)"] --> B["b/(a+b)"]
    B --> C["+"]
    C --> D["X(s)"]
    D --> E["K"]
    E --> F["Pc(s)"]
    F --> G["aATi s/(a+b)ks(Ti s+1)(Td s+1)"]
    G --> C
```
</details>

(b)

Figure 4–32 (a) Overlapped spool valve; (b) underlapped spool valve.   
![](image/6cba65eaf56073dfe18c4f37721e9f0130c53d9a2fceec37e60c02c5039f4a7c.jpg)

<details>
<summary>text_image</summary>

x
x₀/2
x₀/2
High
pressure
Low
pressure
</details>

(a)

![](image/b510de375ec9557ea46d11ab25159c0ec677e4bf115750b8342d39860ae62036.jpg)

<details>
<summary>text_image</summary>

x
x₀/2
x₀/2
High
pressure
Low
pressure
</details>

(b)

If the resistance $R _ { i }$ is removed, or $R _ { i } = 0 ,$ , the action becomes that of a narrow-band proportional, or two-position, controller. (Note that the actions of two feedback bellows cancel each other, and there is no feedback.)

A–4–6. Actual spool valves are either overlapped or underlapped because of manufacturing tolerances. Consider the overlapped and underlapped spool valves shown in Figures 4–32(a) and (b). Sketch curves relating the uncovered port area A versus displacement x.

Solution. For the overlapped valve, a dead zone exists between $- { \frac { 1 } { 2 } } x _ { 0 }$ and $\begin{array} { r } { \frac { 1 } { 2 } x _ { 0 } , \mathrm { o r } - \frac { 1 } { 2 } x _ { 0 } < x < \frac { 1 } { 2 } x _ { 0 } } \end{array}$ . The curve for uncovered port area A versus displacement x is shown in Figure 4–33(a). Such an overlapped valve is unfit as a control valve.

For the underlapped valve, the curve for port area A versus displacement x is shown in Figure 4–33(b). The effective curve for the underlapped region has a higher slope, meaning a higher sensitivity. Valves used for controls are usually underlapped.
