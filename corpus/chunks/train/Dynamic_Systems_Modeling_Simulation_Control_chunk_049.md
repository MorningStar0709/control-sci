# Friction Elements

When a mechanical element dissipates energy due to its motion, it can be modeled as a friction element. In such cases, a fundamental relationship between relative velocity and the resistive force is required to model friction. Just as we used a “spring element” to model stiffness in a mechanical system, we can use a “damper” (or “dashpot”) element to model friction. Figure 2.4 shows a translational damper, which is a fluid-filled cylinder that encases a piston and a rod. The absolute velocity of the piston/rod is ${ \dot { x } } _ { 2 }$ (positive is to the right), and the absolute velocity of the cylinder is ${ \dot { x } } _ { 1 }$ (also positive to the right). If the damper exhibits a linear relationship between the resistive force and relative motion, then the damper force is

$$F = b (\dot {x} _ {2} - \dot {x} _ {1}) \tag {2.14}$$

where b is the viscous friction coefficient, with dimensions of force/velocity, or units of N-s/m. Clearly, the damper force depends on the relative velocity between the piston/rod and cylinder.

![](image/86e309e94d1b2ccf5e898d99107df27faeb9ca3b2145f1be896717bd201d7601.jpg)

<details>
<summary>text_image</summary>

Viscous
fluid
F
ẋ₁
ẋ₂
F
</details>

Figure 2.4 Translational damper.

Friction elements can only dissipate energy. From basic mechanics we know that power is the time rate of change of energy, or force × velocity. Consider a translational damper where ẋ is the velocity magnitude of the piston relative to the stationary cylinder. The rate of energy dissipation from the damper is

$$\dot {\xi} _ {f} = - (b \dot {x}) \dot {x} = - b \dot {x} ^ {2} \tag {2.15}$$

Recall that energy is the scalar (or “dot”) product of the force vector and displacement vector, and, therefore, a minus sign is inserted to indicate that the friction force bẋ is in the opposite direction of the velocity. Equation (2.15) shows that the rate of energy loss is always negative regardless of the direction of the velocity. Power or energy time rate of change has units of N-m/s or J/s or watts (W).

Next, consider a rotational or torsional damper, where the damping torque is proportional to the relative angular velocity

$$T = b \left(\dot {\theta} _ {2} - \dot {\theta} _ {1}\right) \tag {2.16}$$
