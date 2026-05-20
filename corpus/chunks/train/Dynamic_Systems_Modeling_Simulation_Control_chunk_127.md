R_a
L_a
e_in(t)
+
-
I_a
e_b
Armature circuit
Motor torque,
T_m
θ
Load torque,
T_L
Rotor, J
Viscous friction, b
</details>

Figure 3.19 Schematic diagram of a DC motor.

Figure 3.19 shows a schematic diagram of the DC motor. The armature circuit is composed of the voltage source $e _ { \mathrm { i n } } ( t )$ , armature coil inductance $L _ { a }$ (due to the windings), armature resistance $R _ { a } ,$ , and backemf $e _ { b }$ . Note that the back emf is represented by a modified voltage-source symbol with positive and negative terminals that oppose the positive (clockwise) flow of armature current $I _ { a }$ . The mechanical component of the DC motor is shown to the right of the armature circuit and includes the moment of inertia for the rotor $J ,$ viscous friction coefficient $^ { b , }$ motor torque $T _ { m }$ (from the current–magnetism interaction), and load torque $T _ { L } ,$ . Note that positive angular rotation of the rotor is clockwise and corresponds to positive armature current $I _ { a }$ and positive motor torque $T _ { m }$ .

We can derive the complete mathematical model of the DC motor by applying Kirchhoff’s laws to the armature circuit and Newton’s laws to the mechanical rotor. To begin, we use Kirchhoff’s voltage law around the loop, moving clockwise

$$- e _ {R} - e _ {L} - e _ {b} + e _ {\mathrm{in}} (t) = 0$$

The reader should note that the first three voltage terms are voltage drops as the assumed positive current flow is from the positive to negative terminals for the resistor, inductor, and back emf. Next, we substitute the appropriate element laws for voltage drop across a resistor $( e _ { R } = R _ { a } I _ { a } )$ , voltage across an inductor $( e _ { L } = L _ { a } \dot { I } _ { a } )$ , and back emf $( e _ { b } = K _ { b } \dot { \theta } )$ to yield

$$L _ {a} \dot {I} _ {a} + R _ {a} I _ {a} + K _ {b} \dot {\theta} = e _ {\mathrm{in}} (t) \tag {3.87}$$

The mathematical model of the mechanical component is derived using the methods developed in Chapter 2. Figure 3.20 shows the free-body diagram of the mechanical armature rotor with motor torque $( T _ { m } = K _ { m } I _ { a } )$ , viscous friction torque $( b \dot { \theta } )$ , and load torque $( T _ { L } )$ . Summing torques on the rotor (with a positive clockwise convention) and applying Newton’s second law yields

$$ⓧ \sum T = K _ {m} I _ {a} - T _ {L} - b \dot {\theta} = J \ddot {\theta} \tag {3.88}$$

![](image/c648a9abbcc7afb08286504f17309db41c71f6dea17dc796af861bf434d9b03e.jpg)

<details>
<summary>flowchart</summary>
