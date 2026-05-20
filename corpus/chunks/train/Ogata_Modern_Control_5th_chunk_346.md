# 6–8 LAG–LEAD COMPENSATION

Lead compensation basically speeds up the response and increases the stability of the system. Lag compensation improves the steady-state accuracy of the system, but reduces the speed of the response.

If improvements in both transient response and steady-state response are desired, then both a lead compensator and a lag compensator may be used simultaneously. Rather than introducing both a lead compensator and a lag compensator as separate units, however, it is economical to use a single lag–lead compensator.

Lag–lead compensation combines the advantages of lag and lead compensations. Since the lag–lead compensator possesses two poles and two zeros, such a compensation increases the order of the system by 2, unless cancellation of pole(s) and zero(s) occurs in the compensated system.

Electronic Lag–Lead Compensator Using Operational Amplifiers. Figure 6–53 shows an electronic lag–lead compensator using operational amplifiers. The transfer function for this compensator may be obtained as follows: The complex impedance $Z _ { 1 }$ is given by

Figure 6–53 Lag–lead compensator.   
![](image/2b260cbe8b2c11416c11c74d4ae144ecc244113c6465c6ba84aee08c969fd6f6.jpg)

<details>
<summary>text_image</summary>

Z1
R1 C1
R3
Ei(s)
R2 C2
R4 Z2
+
-
E(s)
R5
R6
+
-
Eo(s)
Lag-lead network Sign inverter
</details>

$$\frac {1}{Z _ {1}} = \frac {1}{R _ {1} + \frac {1}{C _ {1} s}} + \frac {1}{R _ {3}}$$

or

$$Z _ {1} = \frac {\left(R _ {1} C _ {1} s + 1\right) R _ {3}}{\left(R _ {1} + R _ {3}\right) C _ {1} s + 1}$$

Similarly, complex impedance $Z _ { 2 }$ is given by

$$Z _ {2} = \frac {\left(R _ {2} C _ {2} s + 1\right) R _ {4}}{\left(R _ {2} + R _ {4}\right) C _ {2} s + 1}$$

Hence, we have

$$\frac {E (s)}{E _ {i} (s)} = - \frac {Z _ {2}}{Z _ {1}} = - \frac {R _ {4}}{R _ {3}} \frac {\left(R _ {1} + R _ {3}\right) C _ {1} s + 1}{R _ {1} C _ {1} s + 1} \cdot \frac {R _ {2} C _ {2} s + 1}{\left(R _ {2} + R _ {4}\right) C _ {2} s + 1}$$

The sign inverter has the transfer function

$$\frac {E _ {o} (s)}{E (s)} = - \frac {R _ {6}}{R _ {5}}$$

Thus the transfer function of the compensator shown in Figure 6–53 is

$$\frac {E _ {o} (s)}{E _ {i} (s)} = \frac {E _ {o} (s)}{E (s)} \frac {E (s)}{E _ {i} (s)} = \frac {R _ {4} R _ {6}}{R _ {3} R _ {5}} \left[ \frac {(R _ {1} + R _ {3}) C _ {1} s + 1}{R _ {1} C _ {1} s + 1} \right] \left[ \frac {R _ {2} C _ {2} s + 1}{(R _ {2} + R _ {4}) C _ {2} s + 1} \right] \tag {6-21}$$

Let us define
