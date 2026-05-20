5.42 dc servo, simplified model In Problem 2.4 (Chapter 2), a simplified model of the servo of Example 2.1 was derived, using $L = 0$ . This model is to be used as a design model for a control system.

a. If $P(s)$ is the true model and $P_0(s)$ is the simplified model, calculate the multiplicative uncertainty $\Delta(s)$ , where $P = (1 + \Delta)P_0$ .   
b. Compute $\ell(j\omega) = |\Delta(j\omega)|$ , and estimate the bandwidth limit of a control system that has been designed using $P_0$ .

![](image/385d0bdf1331c573c47a9340c13c71a41b8232e91e27ae329ef4b7e0fc1fe0af.jpg)

5.43 In some robotic manipulators, feedback loops using operational amplifiers control the armature currents of the dc motors that drive the joints. Figure 5.35 has such a current-control loop as an inner loop (the constants are those of Example 2.1 in Chapter 2). Because of the relatively fast electrical phenomena, this inner loop maintains $i(t)$ near $i_d(t)$ , provided $\omega(t)$ and $i_d(t)$ are relatively slow. The approximation $i \approx i_d$ is made for the design of the outer-loop controller, which is greatly simplified since the plant model becomes $\theta = (4.438 / s^2)i_d$ . We wish to explore the range of validity of that simplification.

![](image/ddc3f33dd7f6af91d7dd3b54380eef21e3111d6a4f87ed86acc5461cc338fd0f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["θd"] --> B["+"]
    B --> C["PD"]
    C --> D["i_d"]
    D --> E["+"]
    E --> F["3(s + 24)/s"]
    F --> G["v"]
    G --> H["20"]
    H --> I["+"]
    I --> J["1/(s + 24)"]
    J --> K["i"]
    K --> L["4.438/s"]
    L --> M["w"]
    M --> N["1/s"]
    N --> O["θ"]
    O --> P["Feedback to PD"]
    P --> Q["-"]
    Q --> R["+"]
    R --> S["12"]
    S --> T["+"]
    T --> U["1/s"]
    U --> V["θ"]
```
</details>

Figure 5.35 Joint control system for a robot

a. Calculate the transfer function $\theta / i_d$ .   
b. The simplified model $\theta/i_{d}=4.438/s^{2}$ is to be used. Proceed as in Example 5.20 to calculate $\Delta(s)$ , where $(1+\Delta)(4.438/s^{2})=$ true transfer function $\theta/i_{d}$ . Calculate $\ell(j\omega)=|\Delta(j\omega)|$ . Estimate the bandwidth limit on the outer-loop control system if this simplification is used in the design of the outer loop.

![](image/6c3e7a8509dd9ed32a6764597f065ec51f003c1a4dd16c3fb47e22ca8249218c.jpg)

5.44 Servo with flexible shaft In the model of Problem 2.5 (Chapter 2) for the servo with flexible shaft, the compliance parameter $K$ has a nominal value of $500\mathrm{Nm / rad}$ . This parameter is poorly known, and we wish to estimate the bandwidth limit due to uncertainty. We assume that $K$ may vary by $\pm x\%$ . The plant input is $v$ , and the output is $\theta_{2}$ .

a. Compute $\ell(j\omega)$ for $x = 1\%$ , $10\%$ , and $50\%$ .   
b. Using the results of part (a), estimate the bandwidth limit in each case. Explain why these limits are conservative.
