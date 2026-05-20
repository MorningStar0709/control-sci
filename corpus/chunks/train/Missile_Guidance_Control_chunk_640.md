where $\alpha _ { X }$ is an angle of the X-axis above the horizontal, $\psi$ is the launch azimuth angle, and $\varphi _ { L P }$ is the launch point latitude. For discussion purposes, a two-stage missile will be assumed. The drag coefficient $C _ { D }$ is strictly a function of both the total angle of attack and Mach number. In the present discussion, the angle-of-attack dependence is neglected, and the Mach number dependence is linearized. With a constant speed of sound $( V _ { S } \cong 1 , 0 0 0 ~ \mathrm { f t / s e c } )$ , $C _ { D }$ becomes a function of $V _ { R }$ , as illustrated in Figure 6.33.

Next, an expression is needed to compute the missile’s along-range and crossrange impact dispersion. Recall the differential equation for the velocity-to-begained, (6.178):

$$\frac {d \mathbf {V} g}{d t} = - \mathbf {a} _ {T} - Q \mathbf {V} _ {g}, \tag {6.178}$$

![](image/8caed020340ea3afec364e4b239790552f076f118dd9b66709eaf3a08cd9fb06.jpg)

<details>
<summary>line</summary>

| Point | Description | Description |
| --- | --- | --- |
| C_D0 | Constant C_D0 | Constant C_D0 |
| C_D1 | Constant C_D1 | Constant C_D1 / dC_D1/δV_R |
| C_D2 | Constant C_D2 | Constant C_D2 / dC_D2/V_R |
</details>

Fig. 6.33. Staging concept.

where $\mathbf { a } _ { T }$ is the gravity-free acceleration. Now we can write this equation in component form as follows:

$$\frac {d V _ {g x}}{d t} = - \frac {d ^ {2} x _ {T}}{d t ^ {2}} - (Q _ {x x} + K _ {q} t) V _ {g x} - Q _ {x z} V _ {g z},\frac {d V _ {g y}}{d t} = - \frac {d ^ {2} y _ {T}}{d t ^ {2}} - Q _ {y x} V _ {g x},\frac {d V _ {g z}}{d t} = - \left[ \left(\frac {d ^ {2} z _ {T}}{d t ^ {2}}\right) - m _ {\ddot {z}} \left(\frac {d ^ {2} z _ {T}}{d t ^ {2}}\right) \right],$$

where

$$Q _ {x x} = \text { linear function of time },K _ {q} = \text { a trajectory constant }.$$

The $Q _ { x z }$ term is a step function, becoming zero at a preset time, and $V _ { g z }$ is given by

$$V _ {g z} = V _ {g z 1} + \int_ {0} ^ {t} \left(\frac {d V _ {g z}}{d t}\right) d t + V _ {g z 0},$$

where $V _ { g z 1 }$ steps from zero to a predetermined constant, and $V _ { g z 0 }$ is a prescribed constant. The along-range and cross-range errors $\Delta R$ and $\Delta C$ , attributed to launch and propulsion disturbances, have been found to vary linearly (i.e., to within a sufficient order of accuracy) with the $Q$ elements. Thus,

$$\Delta R = (\partial \Delta R / \partial Q _ {x x}) Q _ {x x} + \Delta R _ {o},\Delta C R = (\partial \Delta C R / \partial Q _ {x x}) Q _ {x x} + (\partial \Delta C R / \partial Q _ {y x}) Q _ {y x} + \Delta C R _ {o}.$$

The impact dispersion is just the root sum square of the along- and cross-range errors. Differentiating the dispersion function with respect to the $Q$ parameters in question and equating this to zero affords the solution of the optimum values of $Q _ { x x }$ and $Q _ { y x }$ .
