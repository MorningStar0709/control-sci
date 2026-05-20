# EXAMPLE 6–9

Consider the control system of Example 6–8 again. Suppose that we use a lag–lead compensator of the form given by Equation (6–24), or

$$G _ {c} (s) = K _ {c} \frac {\left(s + \frac {1}{T _ {1}}\right) \left(s + \frac {1}{T _ {2}}\right)}{\left(s + \frac {\beta}{T _ {1}}\right) \left(s + \frac {1}{\beta T _ {2}}\right)} \quad (\beta > 1)$$

Assuming the specifications are the same as those given in Example 6–8, design a compensator $G _ { c } ( s )$ .

The desired locations for the dominant closed-loop poles are at

$$s = - 2. 5 0 \pm j 4. 3 3$$

The open-loop transfer function of the compensated system is

$$G _ {c} (s) G (s) = K _ {c} \frac {\left(s + \frac {1}{T _ {1}}\right) \left(s + \frac {1}{T _ {2}}\right)}{\left(s + \frac {\beta}{T _ {1}}\right) \left(s + \frac {1}{\beta T _ {2}}\right)} \cdot \frac {4}{s (s + 0 . 5)}$$

Since the requirement on the static velocity error constant $K _ { v }$ is $8 0 \mathrm { s e c } ^ { - 1 }$ , we have

$$K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) = \lim _ {s \rightarrow 0} K _ {c} \frac {4}{0 . 5} = 8 K _ {c} = 8 0$$

Thus

$$K _ {c} = 1 0$$

The time constant $T _ { 1 }$ and the value of $\beta$ are determined from

$$\left| \frac {s + \frac {1}{T _ {1}}}{s + \frac {\beta}{T _ {1}}} \right| \left| \frac {4 0}{s (s + 0 . 5)} \right| _ {s = - 2. 5 + j 4. 3 3} = \left| \frac {s + \frac {1}{T _ {1}}}{s + \frac {\beta}{T _ {1}}} \right| \frac {8}{4 . 7 7} = 1\left| \frac {s + \frac {1}{T _ {1}}}{s + \frac {\beta}{T _ {1}}} \right| _ {s = - 2. 5 + j 4. 3 3} = 5 5 ^ {\circ}$$

(The angle deficiency of $5 5 ^ { \circ }$ was obtained in Example 6–8.) Referring to Figure 6–58, we can easily locate points $A$ and B such that

$$\underline {{A P B}} = 5 5 ^ {\circ}, \quad \frac {\overline {{P A}}}{\overline {{P B}}} = \frac {4 . 7 7}{8}$$

(Use a graphical approach or a trigonometric approach.) The result is

$$\overline {{{{A O}}}} = 2. 3 8, \quad \overline {{{{B O}}}} = 8. 3 4$$

or

$$T _ {1} = \frac {1}{2 . 3 8} = 0. 4 2 0, \quad \beta = 8. 3 4 T _ {1} = 3. 5 0 3$$

The phase-lead portion of the lag–lead network thus becomes

$$1 0 \left(\frac {s + 2 . 3 8}{s + 8 . 3 4}\right)$$

For the phase-lag portion, we choose $T _ { 2 }$ such that it satisfies the conditions

$$\left| \frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{3 . 5 0 3 T _ {2}}} \right| _ {s = - 2. 5 0 + j 4. 3 3} \div 1, \quad - 5 ^ {\circ} < \left| \frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{3 . 5 0 3 T _ {2}}} \right| _ {s = - 2. 5 0 + j 4. 3 3} < 0 ^ {\circ}$$

![](image/d4c093b0f120a994aaf3ffcb8d7de1d14f939961b7db0901e819e549775d731e.jpg)
