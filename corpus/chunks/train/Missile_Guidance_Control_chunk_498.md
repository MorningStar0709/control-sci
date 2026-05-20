# Missile Flight After Motor Burnout

Once the motor has burned out, the missile will enter a “coast” phase in which the change in the missile’s velocity along the flight-path will be due entirely to the aerodynamic drag. For this period of the missile flight, the missile mass (M) will be constant, and it will also be assumed that the air density is also constant. It will be assumed that the product of the drag coefficient and the velocity raised to a power $( \beta )$ is also constant. Note that the case $\beta = 0$ corresponds to constant drag coefficient (as was assumed during motor burn).

The missile drag (D) is given by the expression

$$D = 0. 5 \rho V ^ {2} S C _ {D}, \tag {5.74}$$

while the acceleration due to drag $\left( A _ { D } \right)$ is given by $- ( D / M )$ ; that is,

$$A _ {D} = - V ^ {2} \left[ \left(0. 5 \rho S C _ {D}\right) / M \right]. \tag {5.75a}$$

Since we have assumed that the air density and missile mass are constant, and that $C _ { D } V ^ { \beta }$ is also a constant, then the parameter $( 0 . 5 C _ { D } V ^ { \beta } \rho S ) / M$ is also constant. If this is denoted by $D _ { C }$ , then the acceleration due to drag is given by

$$A _ {D} = - D _ {C} V ^ {2 - \beta}. \tag {5.85}$$

Therefore, we can write

$$\frac {d s}{d t} = V, \tag {5.86a}\frac {d V}{d t} = - D _ {p} V ^ {2 - \beta}. \tag {5.86b}$$

For the missile distance traveled we need to solve

$$d s = V d t - (V ^ {\beta - 1} d V / D _ {C}), \tag {5.87a}\int_ {s _ {0}} ^ {s} d s = - \int_ {V _ {0}} ^ {V} (V ^ {\beta - 1} / D _ {C}) d V. \tag {5.87b}$$

Here we will assume two solutions as follows:

If $0 < \beta < 1$ ,

$$s = s _ {o} + [ (V _ {o} ^ {\beta} - V ^ {\beta}) / \beta D _ {C} ]. \tag {5.88a}$$

$\mathrm { I f } \ \beta = 0 ,$

$$s = s _ {o} + [ \ln (V _ {o} / V) / D _ {C} ]. \tag {5.88b}$$

For the missile speed we need to solve

$$- (V ^ {\beta - 2} d V / D _ {C}) = d t, \tag {5.89a}- \int_ {V _ {0}} ^ {V} (V ^ {\beta - 2} / D _ {C}) d V = \int_ {t _ {0}} ^ {t} d t. \tag {5.89b}$$

![](image/253506f981ad88dddf3cd6b6e09120d95ff6d506f46e59b5ae0901202f8380d2.jpg)

<details>
<summary>text_image</summary>

AI
R_LOS
V_M
Target
θ
V_T
X
</details>

Fig. 5.36. Geometry for impact point calculations.

From the above, we obtain two solutions as follows:

${ \mathrm { I f ~ } } 1 < \beta < 1 ,$

$$t = t _ {o} + [ (V _ {o} ^ {\beta - 1} - V ^ {\beta - 1}) / (D _ {C} (\beta - 1)) ]. \tag {5.90a}$$

$\mathrm { I f } \ \beta = 0 ,$

$$t = t _ {o} + \left[ \ln \left(V _ {o} / V\right) / D _ {C} \right]. \tag {5.90b}$$
