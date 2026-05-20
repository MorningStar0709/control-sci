# PID Controllers

It is likely that PID controllers are the most common controllers used in industry. Their applications (to name a few) include motion control, hydraulic control systems, chemical processing plants, and guidance and control of aerospace vehicles. Figure 10.13 shows a PID controller in a feedback control system. We see that the PID controller takes the feedback error signal e(t) and produces three control signals that are summed together to create the control input signal u(t) to the plant. The PID control logic is

$$u (t) = K _ {P} e (t) + K _ {I} \int e (t) d t + K _ {D} \dot {e} (t) \tag {10.11}$$

![](image/027690e7d11d8981e1cf0b2786b9e818749ed66f15198ce83eb1abf53ca8e5b6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r_t["r(t)"] --> add1((+))
    add1 --> e_t["e(t)"]
    e_t --> proportional_control["K_P"]
    proportional_control --> add2((+))
    add2 --> integrator["Integral control"]
    integrator --> add3((+))
    add3 --> Gp_s["G_p(s)"]
    Gp_s --> y_t["y(t)"]
    y_t --> sensor["H(s)"]
    sensor --> add1
    add1 --> minus1(-)
    minus1 --> add2
    add2 --> plant["G_p(s)"]
    plant --> y_t
    PID["PID controller"] --> add3
    PID --> add4
    PID --> Kp["K_P"]
    PID --> KI["K_I/s"]
    PID --> KDs["K_D s"]
    Kp --> add2
    KDs --> add3
    KI --> add2
    KDs --> add3
```
</details>

Figure 10.13 PID controller in a closed-loop system.

Equation (10.11) and Fig. 10.13 show that the composite control signal $u ( t )$ is the sum of three signals that are proportional to the error e(t), its time integral, and its time derivative (the reader should recall that multiplying a signal by 1/s is equivalent to integration and multiplying a signal by s is equivalent to differentiation). The three proportionality constants (“gains”) in Eq. (10.11) and Fig. 10.13 are called the proportional gain $K _ { P } ,$ , the integral gain $K _ { I } ,$ , and the derivative gain $K _ { D }$ . Adjusting each individual gain changes the emphasis of the PID controller. In general, the effect or objective of each term of the PID controller can be summarized as listed:
