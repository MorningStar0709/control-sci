$$x _ {1} = e _ {o}x _ {2} = \dot {e} _ {o}$$

and the input and output variables by

$$u = e _ {i}y = e _ {o} = x _ {1}$$

we obtain

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \frac {1}{L C} & - \frac {R}{L} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ \frac {1}{L C} \end{array} \right] u
$$

and

$$
y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

These two equations give a mathematical model of the system in state space.

Transfer Functions of Cascaded Elements. Many feedback systems have components that load each other. Consider the system shown in Figure 3–8. Assume that $e _ { i }$ is the input and $e _ { o }$ is the output. The capacitances $C _ { 1 }$ and $C _ { 2 }$ are not charged initially.

![](image/2c8f7482fa01884fbcc1c50a6b83cbd368b726c7f09a1fa51024ba7aa4d505a5.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors, capacitors, and current labels
</details>

Figure 3–8 Electrical system.

It will be shown that the second stage of the circuit $( R _ { 2 } C _ { 2 }$ portion) produces a loading effect on the first stage $( R _ { 1 } C _ { 1 }$ portion). The equations for this system are

$$\frac {1}{C _ {1}} \int \left(i _ {1} - i _ {2}\right) d t + R _ {1} i _ {1} = e _ {i} \tag {3-27}$$

and

$$\frac {1}{C _ {1}} \int (i _ {2} - i _ {1}) d t + R _ {2} i _ {2} + \frac {1}{C _ {2}} \int i _ {2} d t = 0 \tag {3-28}\frac {1}{C _ {2}} \int i _ {2} d t = e _ {o} \tag {3-29}$$

Taking the Laplace transforms of Equations (3–27) through (3–29), respectively, using zero initial conditions, we obtain

$$\frac {1}{C _ {1} s} \left[ I _ {1} (s) - I _ {2} (s) \right] + R _ {1} I _ {1} (s) = E _ {i} (s) \tag {3-30}\frac {1}{C _ {1} s} \left[ I _ {2} (s) - I _ {1} (s) \right] + R _ {2} I _ {2} (s) + \frac {1}{C _ {2} s} I _ {2} (s) = 0 \tag {3-31}\frac {1}{C _ {2} s} I _ {2} (s) = E _ {o} (s) \tag {3-32}$$

Eliminating $I _ { 1 } ( s )$ from Equations (3–30) and (3–31) and writing $E _ { i } ( s )$ in terms of $I _ { 2 } ( s )$ , we find the transfer function between $E _ { o } ( s )$ and $E _ { i } ( { \bf s } )$ to be

$$
\begin{array}{l} \frac {E _ {o} (s)}{E _ {i} (s)} = \frac {1}{(R _ {1} C _ {1} s + 1) (R _ {2} C _ {2} s + 1) + R _ {1} C _ {2} s} \\ = \frac {1}{R _ {1} C _ {1} R _ {2} C _ {2} s ^ {2} + (R _ {1} C _ {1} + R _ {2} C _ {2} + R _ {1} C _ {2}) s + 1} \tag {3-33} \\ \end{array}
$$
