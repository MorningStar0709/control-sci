# 9.5.1 PID Controller Basics

The Proportional-Integral-Derivative (PID) controller is a class of controllers which has two zeros and one pole at the origin. The PID controller is the most common controller in industry BY FAR. Design of the PID controller consists of deciding on the desired location of the two zeros and a single gain term, $\overset { \smile } { K } _ { D }$ .

The PID controller an be expressed in four(!) equivalent forms:

$$
\begin{array}{l} C (s) = K _ {P} + K _ {I} / s + K _ {D} s \\ = \frac {K _ {P} s + K _ {I} + K _ {D} s ^ {2}}{s} \\ = \frac {K _ {D} (s ^ {2} + \frac {K _ {P}}{K _ {D}} s + \frac {K _ {I}}{K _ {D}})}{s} \tag {9.7} \\ = \frac {K _ {D} (s + z _ {1}) (s + z _ {2})}{s} \\ \end{array}
$$

All three depend on three positive real gains for the engineer to design: $K _ { P } , K _ { I } , K _ { D }$ . Lower order forms of the PID controller with one or no zeros are also possible according to setting one of the three gains to zero (such as the PD and PI controllers). The zeros of the PID controller depend on all three gains as you can see from comparing the 3rd and 4th forms in Equation 9.7.

![](image/bc6469b2c403bf8d73ba2fb6c715d383cc3c10898df1f7746c902ddca3206921.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    X --> +1["+"]
    +1 --> e_t["e(t)"]
    e_t --> Kp["Kp"]
    e_t --> Ki_s["Ki/s"]
    e_t --> sKd["s/Kd"]
    Kp --> +2["+"]
    Ki_s --> +2
    sKd --> +2
    +2 --> u_t["u(t)"]
    u_t --> P["P"]
    P --> Y
    H = 1 --> e_t
    e_t --> -["-"]
```
</details>

Figure 9.8: The PID controller.

The zeros of the PID controller can pull the closed loop root-locus pole pathways, usually towards the left, which drives faster response and greater stability. The PID controller's pole at the origin can increase the system type and thus reduce steady state error.

The PID controller and a plant (P) are illustrated in Figure 9.8. Interpreting the block diagram,

$$C _ {P I D} (s) = \frac {U (s)}{E (s)} = K _ {P} + \frac {K _ {I}}{s} + K _ {D} s \tag {9.8}$$

and equivalently

$$C _ {P I D} (s) = \frac {K _ {P} s + K _ {i} + K _ {D} s ^ {2}}{s} = \frac {K _ {D} (s ^ {2} + \frac {K _ {P}}{K _ {D}} s + \frac {K _ {I}}{K _ {D}})}{s} \tag {9.9}$$

$K _ { P }$ is the proportional gain. Looking at the rst term of Equation 9.8, you can see that $K _ { P }$ directly multiplies the error (the input to the controller). If the other gains were zero, the control output, u, will be linearly proportional to error.

$$u (t) = K _ {P} e (t)$$
