where ?? is the magnetic flux linkage (Wb) and $a _ { 3 }$ and $a _ { 1 }$ are constants. This nonlinear current model accounts for back emf and the variable inductance because of the displacement of the armature mass. Vaughan and Gamble also developed the empirical equation for electromagnetic force:

$$F _ {\mathrm{em}} (\lambda) = c _ {6} \lambda^ {6} + c _ {4} \lambda^ {4} + c _ {2} \lambda^ {2} (\mathrm{N})$$

where $c _ { 6 } , c _ { 4 }$ , and $c _ { 2 }$ are empirical constants from experiments. Derive the complete mathematical model of the electromechanical actuator. Assume that the return spring is undeflected when x = 0 and the electromagnetic force is zero.

![](image/8c3c7d723a008bb9ac59a3824e09e71da654f5672cddf35523f35a4792bc6c20.jpg)

<details>
<summary>text_image</summary>

R
+
e_in(t)
-
I_L = f(\u03b1)
L
Armature circuit
</details>

![](image/e368797d5a7f4eda838a1420f986fbad064a56b5796753bc9127ab15024bc32b.jpg)

<details>
<summary>text_image</summary>

x
Fem
m
Return spring,
k
Viscous friction, b
Armature + valve mass
</details>

Figure P3.32

3.33 Magnetic levitation (“maglev”) is used to suspend and propel trains without contact with a rail. Magnetic levitation is also used to support rotating bearings for high-performance machines in order to eliminate friction and the need for lubrication [7]. A laboratory experiment demonstrating magnetic levitation is shown in Fig. P3.33. The current-carrying coil produces an electromagnet that provides an attraction force $F _ { \mathrm { e m } }$ on the metal ball

$$F _ {\mathrm{em}} = \frac {K _ {F} I ^ {2}}{(d - x) ^ {2}}$$

where $K _ { F }$ is a “force constant” (units of $\mathrm { N - m } ^ { 2 } / \mathrm { A } ^ { 2 } )$ that depends on the number of coil wraps, material properties of the electromagnetic core, and geometry of the electromagnet [7]. Position x of the ball is measured upward from a fixed at-rest position and distance d is a constant equal to the nominal air-gap distance from the electromagnet tip and the ball for a nominal coil current.

![](image/09a682cd8323dbf2c0e3bdada0a9e1c8410007d11d12f6310c61f3b7efe8aed1.jpg)

<details>
<summary>text_image</summary>

Electromagnet
Coil, L
R
+ e_in(t)
- 
Nominal air gap, d (for x = 0)
Metal ball, m
x
</details>

Figure P3.33

Derive the complete mathematical model of the magnetic levitation system where voltage source $e _ { \mathrm { i n } } ( t )$ is the input variable.

3.34 Consider a comb-drive MEMS actuator with the following physical dimensions:

Comb width w = 5 μm

Gap between fingers $d = 2 \mu \mathrm { m }$

86 fingers

Source voltage $e _ { \mathrm { i n } } { = } 3 0 \mathrm { V } \mathrm { ( c o n s t a n t ) }$

Actuator stiffness $k { = } 0 . 0 4 \mathrm { N } / \mathrm { m }$

Compute the displacement of the comb drive in microns at “steady state” where $e _ { C } = e _ { \mathrm { i n } }$ and the comb mass is not accelerating and stationary $( \mathrm { i . e . , } \ddot { x } = \dot { x } = 0 )$ .
