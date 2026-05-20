When the output is fed back to the summing point for comparison with the input, it is necessary to convert the form of the output signal to that of the input signal. For example, in a temperature control system, the output signal is usually the controlled temperature. The output signal, which has the dimension of temperature, must be converted to a force or position or voltage before it can be compared with the input signal. This conversion is accomplished by the feedback element whose transfer function is H(s), as shown in Figure 2–4.The role of the feedback element is to modify the output before it is compared with the input. (In most cases the feedback element is a sensor that measures the output of the plant. The output of the sensor is compared with the system input, and the actuating error signal is generated.) In the present example, the feedback signal that is fed back to the summing point for comparison with the input is $B ( s ) = H ( s ) C ( s )$ .

![](image/6618e36c0605574f707d2214b21c8439990f75cb57560bf7121c740be6238d7b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["E(s)"]
    C --> D["G(s)"]
    D --> E["C(s)"]
    E --> F["Feedback Loop"]
    F --> B
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
    style E fill:#cff,stroke:#333
    style F fill:#ffc,stroke:#333
```
</details>

Figure 2–3 Block diagram of a closed-loop system.

Figure 2–4 Closed-loop system.   
![](image/cb58c6237f6a2e1a3bf83b5e7f98d176b034518d9da449e508190df9cde72a30.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> +
    + --> E["s"]
    E["s"] --> G["s"]
    G["s"] --> C["s"]
    C["s"] --> H["s"]
    H["s"] --> B["s"]
    B["s"] --> +
    + --> +
    + --> -
    - --> +
    + --> +
```
</details>

Open-Loop Transfer Function and Feedforward Transfer Function. Referring to Figure 2–4, the ratio of the feedback signal $B ( s )$ to the actuating error signal $E ( s )$ is called the open-loop transfer function. That is,

$$\text { Open - loop transfer function } = \frac {B (s)}{E (s)} = G (s) H (s)$$

The ratio of the output $C ( s )$ to the actuating error signal $E ( s )$ is called the feedforward transfer function, so that

$$\text { Feedforward transfer function } = \frac {C (s)}{E (s)} = G (s)$$

If the feedback transfer function $H ( s )$ is unity, then the open-loop transfer function and the feedforward transfer function are the same.
