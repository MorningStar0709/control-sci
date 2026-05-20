where the dry friction force $F _ { \mathrm { d r y } } = \mu _ { k } N _ { C }$ is proportional to the clamping force $N _ { C }$ (produced by the vertical PZT stack) that acts normal to the slide mass $m _ { 2 }$ . The reader should note that the signum function sgn is used in Eq. (2.31) to determine the direction (or sign) of the friction force $F _ { f }$ . If $\dot { x } _ { 1 } - \dot { x } _ { 2 } > 0$ (e.g., clamp mass $m _ { 1 }$ is moving to the right at a faster rate than mass $m _ { 2 } )$ then the arrows for friction force $F _ { f }$ are shown correctly in Fig. 2.21. However, Eq. (2.31) will correctly compute the friction force if $\dot { x } _ { 1 } - \dot { x } _ { 2 } < 0$ and mass $m _ { 2 }$ is moving faster than mass $m _ { 1 }$ .

When the clamp mass $m _ { 1 }$ is released $( N _ { C } = 0 )$ and not in contact with the slide mass, the friction force is zero. Typically, the PZT actuator force $F _ { \mathrm { P Z T } }$ is set to zero during the release phase, and the stiffness force of the extended actuator returns the clamp mass $m _ { 1 }$ to its equilibrium position $( x _ { 1 } = 0 )$ . Using $F _ { \mathrm { P Z T } } = 0$ and $F _ { f } = 0$ , Eqs. (2.29) and (2.30) become

No contact (release): $m _ { 1 } { \ddot { x } } _ { 1 } + b { \dot { x } } _ { 1 } + k x _ { 1 } = 0$ (2.32)

$$m _ {2} \ddot {x} _ {2} = 0 \tag {2.33}$$

In summary, the mathematical model of the PZT actuator system is composed of two sets of modeling equations

$\mathrm { S l i d i n g ~ m o t i o n } ; N _ { C } > 0 \qquad m _ { 1 } \ddot { x } _ { 1 } + b \dot { x } _ { 1 } + k x _ { 1 } = F _ { \mathrm { P Z T } } - \mu _ { k } N _ { C } \mathrm { s g n } ( \dot { x } _ { 1 } - \dot { x } _ { 2 } )$ (2.34a)

$$m _ {2} \ddot {x} _ {2} = \mu_ {k} N _ {C} \operatorname{sgn} \left(\dot {x} _ {1} - \dot {x} _ {2}\right) \tag {2.34b}$$

$\mathrm { N o ~ c o n t a c t ~ ( r e l e a s e ) } ; \qquad \quad m _ { 1 } \ddot { x } _ { 1 } + b \dot { x } _ { 1 } + k x _ { 1 } = 0$ (2.35a)

$N _ { C } = 0 { \mathrm { ~ a n d ~ } } F _ { \mathrm { P Z T } } = 0 \qquad m _ { 2 } { \ddot { x } } _ { 2 } = 0$ (2.35b)

Equation sets (2.34) and (2.35) constitute the complete mathematical model of the PZT actuator. The complete system is nonlinear because of the dry friction force. Numerical integration of the system model is the only practical method for obtaining the system’s response due to the nonlinear sliding friction. Furthermore, a numerical simulation must continuously monitor the normal clamping force $N _ { C }$ between the two masses and PZT actuator force $F _ { \mathrm { P Z T } }$ in order to switch to the appropriate set of ODEs that govern the system dynamics.
