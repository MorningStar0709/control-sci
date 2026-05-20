# 4.3 Missile Equations of Motion

A point-mass model will be assumed for the missile’s flight dynamics, which include aerodynamic, gravitational, rocket thrust forces, a time-varying mass, and up to four stages (for more details on the missile dynamics the reader is referred to Chapters 2 and 3). In simplified form, this particular model will require the following input parameters to describe the missile:

Table 4.4. Guidance Methods for Air-to-Air Missiles∗

<table><tr><td>Semiactive Homing</td><td>Active Homing</td><td>Passive Homing</td></tr><tr><td>Falcon</td><td>Meteor</td><td>Sidewinder</td></tr><tr><td>Sparrow</td><td>Sidewinder II AIM-9X</td><td>Mica</td></tr><tr><td>Skyflash</td><td>AMRAAM AIM-120A</td><td>Magic 2</td></tr><tr><td>Aspide</td><td>Patriot MIM-104</td><td>Shafrir</td></tr><tr><td>Phoenix (+ Active)</td><td>Harpoon AGM-84G</td><td>SAAB 327</td></tr><tr><td>AA-1 Through AA-7</td><td></td><td>ASRAAM (British Aerospace)Super R530R-73 (NATO Code: AA-11 ARCHER)ShrikeStandard ArmHarmAerospatiale (AS-30L)-Laser Guided</td></tr></table>

∗Originally published in The Fundamentals of Aircraft Combat Survivability Analysis and Design, R.E. Ball, AIAA Education Series, copyright © 1985. Reprinted with permission.

1. Initial vacuum thrust $T _ { o }$   
2. Initial weight $W _ { o }$   
3. Final weight $W _ { f }$   
4. Burn time $t _ { b }$   
5. Nozzle exit area $A _ { e }$   
6. Aerodynamic reference area A   
7. Either:

(a) Cone angle $\theta _ { c }$ and induced axial force coefficient $C _ { x 2 }$ to compute the axial force coefficient $C _ { x }$ by a functional expression, or   
(b) A table for powered flight and, if applicable, for coasting flight, or $C _ { x }$ as a function of Mach number M and angle of attack α.

8. Either:

(a) Normal force coefficients $C _ { N 1 }$ and $C _ { N 2 }$ to compute the normal force $C _ { N }$ as a quadratic expression in α, or   
(b) A table of $C _ { N }$ as a function of M and α.

9. Coast time before ignition and after burnout.

10. Maximum permissible normal acceleration loading $a _ { N m a x }$

11. Maximum angle of attack $\alpha _ { m a x }$

Figure 4.5 shows the aerodynamic and thrust acceleration vectors that will be used for this model.

The missile’s equations of motion are

$$\frac {d \mathbf {r}}{d t} = \mathbf {v}, \tag {4.1a}\frac {d \mathbf {v}}{d t} = \mathbf {a} = a _ {v} \mathbf {1} _ {v} + a _ {L} \mathbf {1} _ {L} + \mathbf {g}. \tag {4.1b}$$
