Computing the solenoid inductor voltage $e _ { L }$ is more complicated than the inductor voltage for the DC motor because solenoid inductance changes with the plunger position. Therefore, we use Eq. (3.9) to equate the solenoid inductor voltage to the time derivative of magnetic flux linkage

$$\dot {\lambda} = e _ {L} \tag {3.94}$$

where flux linkage is defined by Eq. (3.8) as the product of inductance and current, or $\lambda = L ( x ) I$ . Because both inductance and current can change with time, the time derivative of the flux linkage is

$$\dot {\lambda} = \frac {d L}{d t} I + L \frac {d I}{d t} \tag {3.95}$$

Using the chain rule to expand $d L / d t ,$ , Eq. (3.95) becomes

$$\dot {\lambda} = \frac {d L}{d x} \frac {d x}{d t} I + L \frac {d I}{d t} \tag {3.96}$$

or, using the compact notation

$$\dot {\lambda} = L _ {x} \dot {x} I + L (x) \dot {I} \tag {3.97}$$

where $L _ { x }$ is the short-hand notation for the derivative $d L / d x .$ . Using Eq. (3.91), the derivative dL∕dx is

$$L _ {x} \equiv \frac {d L}{d x} = \frac {L _ {0}}{d (1 - (x / d)) ^ {2}} \tag {3.98}$$

Finally, we can substitute Eq. (3.97) into Kirchhoff’s loop equation (3.93) for inductor voltage $e _ { L }$ along with resistor voltage drop $e _ { R } = R I$ to yield the mathematical model of the solenoid circuit

$$L (x) \dot {I} + R I = e _ {\text { in }} (t) - L _ {x} \dot {x} I \tag {3.99}$$

Note that the right-hand-side term $L _ { x } { \dot { x } } I$ in Eq. (3.99) acts like the back-emf term in the DC motor modeling equation (3.89a): when the actuator mass moves with positive velocity toward the center of the coil, it induces a negative voltage that decreases the net voltage in the circuit. Furthermore, the induced voltage $L _ { x } { \dot { x } } I$ for the solenoid is nonlinear whereas the back emf of the DC motor is a linear term $( K _ { b } \dot { \theta } )$ .

The mathematical model of the mechanical component of the solenoid actuator is derived using the methods developed in Chapter 2. Figure 3.24 shows the free-body diagram of the armature–valve mass with electromagnetic force $( F _ { \mathrm { e m } } )$ , viscous friction force (bẋ ), and return spring force (kx). We have assumed that no preload force (initial compression) exists in the return spring and hence there is no wall-contact force. Summing forces on the mass and applying Newton’s second law yields

![](image/7c2252fefd71521a8636f37b2d70837c0a10baaf61d6c66f26d9ec7f522a1dfa.jpg)

<details>
<summary>text_image</summary>
