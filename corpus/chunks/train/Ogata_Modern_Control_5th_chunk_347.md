$$T _ {1} = \left(R _ {1} + R _ {3}\right) C _ {1}, \quad \frac {T _ {1}}{\gamma} = R _ {1} C _ {1}, \quad T _ {2} = R _ {2} C _ {2}, \quad \beta T _ {2} = \left(R _ {2} + R _ {4}\right) C _ {2}$$

Then Equation (6–21) becomes

$$\frac {E _ {o} (s)}{E _ {i} (s)} = K _ {c} \frac {\beta}{\gamma} \left(\frac {T _ {1} s + 1}{\frac {T _ {1}}{\gamma} s + 1}\right) \left(\frac {T _ {2} s + 1}{\beta T _ {2} s + 1}\right) = K _ {c} \frac {\left(s + \frac {1}{T _ {1}}\right) \left(s + \frac {1}{T _ {2}}\right)}{\left(s + \frac {\gamma}{T _ {1}}\right) \left(s + \frac {1}{\beta T _ {2}}\right)} \tag {6-22}$$

where

$$\gamma = \frac {R _ {1} + R _ {3}}{R _ {1}} > 1, \quad \beta = \frac {R _ {2} + R _ {4}}{R _ {2}} > 1, \quad K _ {c} = \frac {R _ {2} R _ {4} R _ {6}}{R _ {1} R _ {3} R _ {5}} \frac {R _ {1} + R _ {3}}{R _ {2} + R _ {4}}$$

Note that g is often chosen to be equal to $\beta .$

Lag–lead Compensation Techniques Based on the Root-Locus Approach.

Consider the system shown in Figure 6–54.Assume that we use the lag–lead compensator:

$$G _ {c} (s) = K _ {c} \frac {\beta}{\gamma} \frac {(T _ {1} s + 1) (T _ {2} s + 1)}{\left(\frac {T _ {1}}{\gamma} s + 1\right) (\beta T _ {2} s + 1)} = K _ {c} \left(\frac {s + \frac {1}{T _ {1}}}{s + \frac {\gamma}{T _ {1}}}\right) \left(\frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{\beta T _ {2}}}\right) \tag {6-23}$$

where $\beta > 1$ and $\gamma > 1$ (Consider. $K _ { c }$ to belong to the lead portion of the lag–lead compensator.)

In designing lag–lead compensators, we consider two cases where $\gamma \neq \beta$ and $\gamma = \beta .$

Case 1. $\gamma \neq \beta .$ In this case, the design process is a combination of the design of the. lead compensator and that of the lag compensator.The design procedure for the lag–lead compensator follows:

1. From the given performance specifications, determine the desired location for the dominant closed-loop poles.   
2. Using the uncompensated open-loop transfer function $G ( s )$ , determine the angle deficiency $\phi$ if the dominant closed-loop poles are to be at the desired location.The phase-lead portion of the lag–lead compensator must contribute this angle $\phi .$ .   
3. Assuming that we later choose $T _ { 2 }$ sufficiently large so that the magnitude of the lag portion

$$
\left| \begin{array}{c} s _ {1} + \frac {1}{T _ {2}} \\ \hline s _ {1} + \frac {1}{\beta T _ {2}} \end{array} \right|
$$

![](image/5172827e4abe717ebef57c2efba50d997ea5abc711a1090ff48d096a37780e93.jpg)

<details>
<summary>flowchart</summary>
