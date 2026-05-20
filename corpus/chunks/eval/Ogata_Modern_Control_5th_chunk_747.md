# MATLAB Program 10–3

% Response to initial condition:

$$A = [ 0 1 0; 0 0 1; - 1 - 5 - 6 ];\mathrm{B} = [ 0; 0; 1 ];K = [ 1 9 9 \quad 5 5 \quad 8 ];\mathrm{sys} = \mathrm{ss} (\mathrm {A- B ^ {*} K}, \mathrm{eye(3)}, \mathrm{eye(3)}, \mathrm{eye(3)});t = 0: 0. 0 1: 4;x = \text { initial } (\text { sys }, [ 1; 0; 0 ], t);x 1 = [ 1 0 0 ] ^ {*} x ^ {\prime};\mathrm{x} 2 = [ 0 \quad 1 \quad 0 ] ^ {*} \mathrm{x} ^ {\prime};\mathrm{x} 3 = [ 0 0 1 ] ^ {*} \mathrm{x} ^ {\prime};\text {subplot} (3, 1, 1); \text {plot} (t, x 1), \text {grid}\text { title } (^ {\prime} \text { Response to Initial Condition } ^ {\prime})\text {ylabel} (^ {\prime} \text {state variable x1} ^ {\prime})\text {subplot} (3, 1, 2); \text {plot} (t, x 2), \text {grid}\text {ylabel} (^ {\prime} \text {state variable x2} ^ {\prime})\text {subplot} (3, 1, 3); \text {plot} (t, x 3), \text {grid}\text { xlabel('t (sec)') }\text {ylabel} \left(^ {\prime} \text {state variable x3} ^ {\prime}\right)$$

Figure 10–3 Response to initial condition.   
Response to Initial Condition   
![](image/77e52b18a5b65ae63589e8f0b629884497a192bfa2338113a71305744e640411.jpg)

<details>
<summary>line</summary>

| x | state variable x₁ |
| --- | --- |
| 0.0 | 1.0 |
| 0.5 | 0.2 |
| 1.0 | -0.2 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
| 3.5 | 0.0 |
| 4.0 | 0.0 |
</details>

![](image/750ada637889f3eed7765274d7319097fe2972da661081d2dbaca11253678d88.jpg)

<details>
<summary>line</summary>

| x | state variable x₂ |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | -2.5 |
| 1.0 | 0.5 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
| 3.5 | 0.0 |
| 4.0 | 0.0 |
</details>

![](image/25ca9e5675ffbb672f62aeb514c2cbaaf71a188ffb04940c0eb2cc5bf6f845cb.jpg)

<details>
<summary>line</summary>

| t (sec) | state variable x₃ |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 5.0 |
| 1.0 | 2.0 |
| 1.5 | -1.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
| 3.5 | 0.0 |
| 4.0 | 0.0 |
</details>

In this section we shall discuss the pole-placement approach to the design of type 1 servo systems. Here we shall limit our systems each to have a scalar control signal u and a scalar output y.

In what follows we shall first discuss a problem of designing a type 1 servo system when the plant involves an integrator.Then we shall discuss the design of a type 1 servo system when the plant has no integrator.

Design of Type 1 Servo System when the Plant Has An Integrator. Assume that the plant is defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u \tag {10-19}y = \mathbf {C x} \tag {10-20}$$
