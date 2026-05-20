# Example 2.4 (Level Control)

Description: A tank of uniform cross section is fed at the top by a flow subject to variations. Liquid is withdrawn from the bottom by a control valve. The valve is adjusted to vary the outflow in order to maintain a constant level. (See Fig. 2.11.) The outlet pressure is atmospheric.

Inputs and Outputs: The control input is the valve position u. The disturbance input is the flow $F_{in}$ . The output is the level, $\ell$ .

Basic Principles: Over a given time interval, the difference between the volumes of liquid flowing in and flowing out of the tank is translated into a change in level. As for the valve, it is an orifice of area proportional to u, the position of the valve spool. The volumetric flow through an orifice is theoretically equal to $S\sqrt{(2\Delta P)/\rho}$ , where S is the area of the orifice, $\rho$ is the liquid density, and $\Delta P$ is the pressure across the orifice [3]. In actual fact, this expression must be multiplied by a coefficient somewhat less than 1, the orifice coefficient. A valve is basically a device with an orifice of variable area. In a linear valve, the orifice area is proportional to the displacement of a piston. The displacement is called the stroke.

Objectives: Derive a model, and simulate for the following conditions.

Solution Let A be the cross-sectional area of the tank. Over a small time interval $\Delta t$ , the volume of liquid flowing in is $F_{in} \Delta t$ , and the volume flowing out is $F_{out} \Delta t$ . The change in the volume of the liquid is also given by $A \Delta \ell$ , where $\Delta \ell$ is the change in level. Thus,

$$A \Delta \ell = F _ {\text { in }} \Delta t - F _ {\text { out }} \Delta t.$$

Dividing by $\Delta t$ and passing to the limit,

$$A \frac {d \ell}{d t} = F _ {\mathrm{in}} - F _ {\mathrm{out}}. \tag {2.28}$$

The flow through the valve is given by $c'u\sqrt{(2\Delta P)/\rho}$ , where $c'$ is a constant comprising both the constant of proportionality between u and S and the orifice coefficient. The pressure at the bottom of the tank is $\rho g\ell$ , where $\rho$ is the density of the liquid; that is, the pressure is the weight of a column of height $\ell$ and unit area. Therefore,

![](image/56bc6a960397b99f5bb54222a85f3cedb63ad98649a4f80b40e8b3fc6a138327.jpg)

<details>
<summary>text_image</summary>

Fin
u
Fout
</details>

Figure 2.11 Tank with valve pertaining to level control
