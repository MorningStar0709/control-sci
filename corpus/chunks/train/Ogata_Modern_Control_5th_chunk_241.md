![](image/5d7add22f25822da5a68944b1a476778ecdaf1ef62f1a3c4ef20fa60e263efc7.jpg)

<details>
<summary>line</summary>

| t | u(t) |
| --- | --- |
| 0 | 0.8 |
| ∞ | 0.0 |
</details>

Figure 5–37   
Proportional control system.   
![](image/e36aecb1d81e97f97b075cacfcb3cb27316e548ebc8964ae99f638afa923f4d9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["E(s)"]
    C --> D["K"]
    D --> E["1/(Ts + 1)"]
    E --> F["C(s)"]
    F --> G["Feedback"]
    G --> B
    H["Proportional controller"] --> B
    I["Plant"] --> E
```
</details>

Proportional Control of Systems. We shall show that the proportional control of a system without an integrator will result in a steady-state error with a step input. We shall then show that such an error can be eliminated if integral control action is included in the controller.

Consider the system shown in Figure 5–37. Let us obtain the steady-state error in the unit-step response of the system. Define

$$G (s) = \frac {K}{T s + 1}$$

Since

$$\frac {E (s)}{R (s)} = \frac {R (s) - C (s)}{R (s)} = 1 - \frac {C (s)}{R (s)} = \frac {1}{1 + G (s)}$$

the error E(s) is given by

$$E (s) = \frac {1}{1 + G (s)} R (s) = \frac {1}{1 + \frac {K}{T s + 1}} R (s)$$

For the unit-step input R(s)=1/s, we have

$$E (s) = \frac {T s + 1}{T s + 1 + K} \frac {1}{s}$$

The steady-state error is

$$e _ {\mathrm{ss}} = \lim _ {t \rightarrow \infty} e (t) = \lim _ {s \rightarrow 0} s E (s) = \lim _ {s \rightarrow 0} \frac {T s + 1}{T s + 1 + K} = \frac {1}{K + 1}$$

Such a system without an integrator in the feedforward path always has a steady-state error in the step response. Such a steady-state error is called an offset. Figure 5–38 shows the unit-step response and the offset.

![](image/0fc5ea92d07f202ca3a4279acd14d986f4f3916574ba05688f145b9e0d054c10.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| 0 | 0 |
| >1 | 1 |
</details>

Figure 5–38   
Unit-step response and offset.

Figure 5–39   
Integral control system.   
![](image/6e5da1b71f79a12ca01bb64de2a40ef74aadec9e2b3cd0627ab3149fa8e6cec1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> +
    + --> E["s"]
    E["s"] --> K["K/s"]
    K["K/s"] --> 1["1/(Ts+1)"]
    1["1/(Ts+1)"] --> C["s"]
    C["s"] --> +
    + --> -
    - --> +
    - --> -
    - --> +
```
</details>

Integral Control of Systems. Consider the system shown in Figure 5–39. The controller is an integral controller. The closed-loop transfer function of the system is
