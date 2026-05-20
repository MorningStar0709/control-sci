By substituting Equation (2–53) into Equation (2–52), we obtain

$$C _ {1} = G _ {1} \left[ R _ {1} - G _ {3} G _ {4} \left(R _ {2} - G _ {2} C _ {1}\right) \right] \tag {2-54}$$

By substituting Equation (2–52) into Equation (2–53), we get

$$C _ {2} = G _ {4} \left[ R _ {2} - G _ {2} G _ {1} \left(R _ {1} - G _ {3} C _ {2}\right) \right] \tag {2-55}$$

Solving Equation (2–54) for $C _ { 1 }$ , we obtain

$$C _ {1} = \frac {G _ {1} R _ {1} - G _ {1} G _ {3} G _ {4} R _ {2}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} \tag {2-56}$$

Solving Equation (2–55) for $C _ { 2 }$ gives

$$C _ {2} = \frac {- G _ {1} G _ {2} G _ {4} R _ {1} + G _ {4} R _ {2}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} \tag {2-57}$$

Equations (2–56) and (2–57) can be combined in the form of the transfer matrix as follows:

$$
\left[ \begin{array}{c} C _ {1} \\ C _ {2} \end{array} \right] = \left[ \begin{array}{c c} \frac {G _ {1}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} & - \frac {G _ {1} G _ {3} G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} \\ - \frac {G _ {1} G _ {2} G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} & \frac {G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} \end{array} \right] \left[ \begin{array}{c} R _ {1} \\ R _ {2} \end{array} \right]
$$

Then the transfer functions $C _ { 1 } ( s ) / R _ { 1 } ( s ) , C _ { 1 } ( s ) / R _ { 2 } ( s ) , C _ { 2 } ( s ) / R _ { 1 } ( s )$ and $C _ { 2 } ( s ) / R _ { 2 } ( s )$ can be obtained as follows:

$$
\begin{array}{l} \frac {C _ {1} (s)}{R _ {1} (s)} = \frac {G _ {1}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}}, \quad \frac {C _ {1} (s)}{R _ {2} (s)} = - \frac {G _ {1} G _ {3} G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} \\ \frac {C _ {2} (s)}{R _ {1} (s)} = - \frac {G _ {1} G _ {2} G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}}, \quad \frac {C _ {2} (s)}{R _ {2} (s)} = \frac {G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}} \\ \end{array}
$$

Note that Equations (2–56) and (2–57) give responses $C _ { 1 }$ and $C _ { 2 } .$ , respectively, when both inputs $R _ { 1 }$ and $R _ { 2 }$ are present.

Notice that when $R _ { 2 } ( s ) = 0 { } .$ , the original block diagram can be simplified to those shown in Figures 2–25(a) and $\mathbf { ( b ) }$ . Similarly, when $R _ { 1 } ( s ) = 0 { \mathrm { : } }$ , the original block diagram can be simplified to those shown in Figures 2–25(c) and (d). From these simplified block diagrams we can also obtain $C _ { 1 } ( s ) / R _ { 1 } ( s ) , C _ { 2 } ( s ) / R _ { 1 } ( s ) , C _ { 1 } ( s ) / R _ { 2 } ( s )$ , and $C _ { 2 } ( s ) / R _ { 2 } ( s )$ , as shown to the right of each corresponding block diagram.

![](image/f6ae6868bc55ec99a480d9bda8a2de5aed2f5b797f6d502b22c77fd6f0bc0379.jpg)

$$\frac {C _ {1}}{R _ {1}} = \frac {G _ {1}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}}\frac {C _ {2}}{R _ {1}} = \frac {- G _ {1} G _ {2} G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}}\frac {C _ {1}}{R _ {2}} = \frac {- G _ {1} G _ {3} G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}}$$

Figure 2–25 Simplified block diagrams and corresponding closed-loop transfer functions.

$$\frac {C _ {2}}{R _ {2}} = \frac {G _ {4}}{1 - G _ {1} G _ {2} G _ {3} G _ {4}}$$
