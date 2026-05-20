Equation (4.52) clearly shows that when the spring preload force $F _ { \mathrm { P I } }$ L balances the differential pressure force $( P _ { c } - P _ { \mathrm { a t m } } ) A$ the plate mass can be at static equilibrium $( { \mathrm { i . e . , } } { \ddot { x } } = { \dot { x } } = x = 0 )$ .

The complete mathematical model of the accumulator system is composed of Eqs. (4.46), (4.47), and (4.52), which are repeated below with the proper substitutions for the volumes and their time-rates:

$$\text { Hose CV: } \quad \dot {P} _ {h} = \frac {\beta}{V _ {h}} (Q _ {\text { in }} - Q _ {c} - Q _ {h}) \tag {4.53}\text { Accumulator CV: } \quad \dot {P} _ {c} = \frac {\beta}{V _ {c 0} + A x} (Q _ {c} - A \dot {x}) \tag {4.54}\text { Accumulator plate: } \quad m \ddot {x} + b \dot {x} + k x = (P _ {c} - P _ {\mathrm{atm}}) A - F _ {\mathrm{PL}} \tag {4.55}$$

![](image/1aafcd3960442b2f425d2a59cbeb944b9fd83966317c2f18d71f2801786cf114.jpg)

<details>
<summary>text_image</summary>

kx F_PL P_atm A bẋ
↑+x
Plate mass, m
P_cA
</details>

Figure 4.13 Free-body diagram of the hydraulic accumulator plate (Example 4.3).

Equations (4.53), (4.54), and (4.55) represent the mathematical model of the hydromechanical system. Equation (4.49) is also required to define the orifice flow rate $Q _ { c }$ . The complete model consists of two first-order ODEs and one second-order ODE and hence the model is fourth order. The ODEs are coupled because knowledge of the mechanical motion is required in the accumulator CV equation (4.54) and pressure information is required in the orifice flow equation (4.49) and the mechanical equation (4.55). The system is clearly nonlinear because of the orifice flow equation (4.49). In summary, the dynamic variables of the system are hose pressure $P _ { h } ,$ , accumulator pressure $P _ { c } ,$ , and plate position x, while the system input variables are input flow rate $Q _ { \mathrm { i n } } ^ { } .$ , hose flow rate $Q _ { h }$ , atmospheric pressure $P _ { \mathrm { a t m } }$ , and spring preload force $F _ { \mathrm { P L } }$ .
