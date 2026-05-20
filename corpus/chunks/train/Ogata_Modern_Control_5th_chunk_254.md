Consider the gear-train system shown in Figure 5–51. In this system, a load is driven by a motor through the gear train. Assuming that the stiffness of the shafts of the gear train is infinite (there is neither backlash nor elastic deformation) and that the number of teeth on each gear is proportional to the radius of the gear, obtain the equivalent moment of inertia and equivalent viscous-friction coefficient referred to the motor shaft and referred to the load shaft.

In Figure 5–51 the numbers of teeth on gears 1, 2, 3, and 4 are $N _ { 1 } , N _ { 2 } , N _ { 3 }$ , and $N _ { 4 } .$ , respectively. The angular displacements of shafts, 1, 2, and 3 are $\theta _ { 1 } , \theta _ { 2 }$ , and $\theta _ { 3 } ,$ , respectively.Thus, $\theta _ { 2 } / \theta _ { 1 } = N _ { 1 } / N _ { 2 }$ and $\theta _ { 3 } / \theta _ { 2 } = N _ { 3 } / N _ { 4 }$ The moment of inertia and viscous-friction coefficient of each gear-train. component are denoted by $J _ { 1 } , b _ { 1 } ; J _ { 2 } , b _ { 2 }$ ; and $J _ { 3 } , b _ { 3 }$ ; respectively. $( J _ { 3 }$ and $b _ { 3 }$ include the moment of inertia and friction of the load.)

![](image/29758e805897c2043b1cf92a1eb09a31982105b493a4a52b11cbe2e0ed1dd55a.jpg)

<details>
<summary>text_image</summary>

Shaft 1
J₁, b₁
Input torque
from motor
Tₘ(t)
θ₁
N₁
Gear 1
Shaft 2
J₂, b₂
θ₂
Gear 2
N₂
N₃
Gear 3
Gear 4
N₄
J₃, b₃
θ₃
Load torque
Tₗ(t)
</details>

Figure 5–51 Gear-train system.

Solution. For this gear-train system, we can obtain the following equations: For shaft 1,

$$J _ {1} \ddot {\theta} _ {1} + b _ {1} \dot {\theta} _ {1} + T _ {1} = T _ {m} \tag {5-63}$$

where $T _ { m }$ is the torque developed by the motor and $T _ { 1 }$ is the load torque on gear 1 due to the rest of the gear train. For shaft 2,

$$J _ {2} \ddot {\theta} _ {2} + b _ {2} \dot {\theta} _ {2} + T _ {3} = T _ {2} \tag {5-64}$$

where $T _ { 2 }$ is the torque transmitted to gear 2 and $T _ { 3 }$ is the load torque on gear 3 due to the rest of the gear train. Since the work done by gear 1 is equal to that of gear 2,

$$T _ {1} \theta_ {1} = T _ {2} \theta_ {2} \quad \text { or } \quad T _ {2} = T _ {1} \frac {N _ {2}}{N _ {1}}$$

If $N _ { 1 } / N _ { 2 } < 1$ the gear ratio reduces the speed as well as magnifies the torque. For shaft 3,,

$$J _ {3} \ddot {\theta} _ {3} + b _ {3} \dot {\theta} _ {3} + T _ {L} = T _ {4} \tag {5-65}$$

where $T _ { L }$ is the load torque and $T _ { 4 }$ is the torque transmitted to gear 4. $T _ { 3 }$ and $T _ { 4 }$ are related by

$$T _ {4} = T _ {3} \frac {N _ {4}}{N _ {3}}$$

and $\theta _ { 3 }$ and $\theta _ { 1 }$ are related by
