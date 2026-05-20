where $p _ { e }$ is defined by Equation (4–20). The controller shown in Figure 4–10 is a proportional controller.The value of gain $K _ { p }$ increases as k approaches unity. Note that the value of k depends on the diameters of the orifices in the inlet and outlet pipes of the feedback chamber. (The value of k approaches unity as the resistance to flow in the orifice of the inlet pipe is made smaller.)

Pneumatic Actuating Valves. One characteristic of pneumatic controls is that they almost exclusively employ pneumatic actuating valves.A pneumatic actuating valve can provide a large power output. (Since a pneumatic actuator requires a large power input to produce a large power output, it is necessary that a sufficient quantity of pressurized air be available.) In practical pneumatic actuating valves, the valve characteristics may not be linear; that is, the flow may not be directly proportional to the valve stem position, and also there may be other nonlinear effects, such as hysteresis.

Consider the schematic diagram of a pneumatic actuating valve shown in Figure 4–11. Assume that the area of the diaphragm is A. Assume also that when the actuating error is zero, the control pressure is equal to $\overline { { P } } _ { c }$ and the valve displacement is equal to $\breve { \bar { X } }$ .

In the following analysis, we shall consider small variations in the variables and linearize the pneumatic actuating valve. Let us define the small variation in the control pressure and the corresponding valve displacement to be $p _ { c }$ and x, respectively. Since a small change in the pneumatic pressure force applied to the diaphragm repositions the load, consisting of the spring, viscous friction, and mass, the force-balance equation becomes

$$A p _ {c} = m \ddot {x} + b \dot {x} + k x$$

where m=mass of the valve and valve stem

b=viscous-friction coefficient

k=spring constant

If the force due to the mass and viscous friction are negligibly small, then this last equation can be simplified to

$$A p _ {c} = k x$$

The transfer function between x and $p _ { c }$ thus becomes

$$\frac {X (s)}{P _ {c} (s)} = \frac {A}{k} = K _ {c}$$

![](image/1d243587ced0757306e3ca60ed15090e65dd1a4ab7c6b1b06721d8d27f0469fe.jpg)

<details>
<summary>text_image</summary>

P̅c + pc
C
A
Q̅ + qi
k
X̅ + x
</details>

Figure 4–11 Schematic diagram of a pneumatic actuating valve.
