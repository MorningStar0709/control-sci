# Proportional-derivative controller

Shifting the closed-loop root branches in Fig. 10.41 to the left will improve the transient response by speeding up the response and adding damping. Adding an open-loop zero to the forward path will act as a “sink” and “attract” the branches. Therefore, inserting an open-loop zero to the left of the open-loop pole at $s = - 0 . 3$ will shift the branches left. A PD controller will add an open-loop zero. To begin, let us test the following PD controller with an open-loop zero at s = –3

$$G _ {C} (s) = K (s + 3) = K _ {P} + K _ {D} s \tag {10.48}$$

If we compare the PD controller in Eq. (10.48) to the “standard” format of Eq. (10.45), we see that the control gain K is equal to the derivative gain $K _ { D }$ and that 3K is equal to the proportional gain $K _ { P }$ (therefore, the openloop zero is located at $s = - K _ { P } / K _ { D } = - \bar { 3 } ,$ ). The open-loop transfer function consists of the PD controller and the mechanical system plant (with actuator gain $K _ { A } = 2 \mathrm { N } / \mathrm { V } )$ .

$$G (s) H (s) = \frac {2 (s + 3)}{s ^ {2} + 0 . 3 s} \tag {10.49}$$

Hence, the following MATLAB commands will create the root-locus plot presented in Fig. 10.42:

$$> > \text { sysGH } = \text { tf } (2 * [ 1 3 ], [ 1 0. 3 0 ])$$

% create G(s)H(s) with PD controller

$$> > \text { rlocus(sysGH) }$$

% create and draw the root locus
