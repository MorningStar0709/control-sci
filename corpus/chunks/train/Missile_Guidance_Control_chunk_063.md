It should be noted here that stability and control for fixed-wing aircraft are assessed through six rigid-body degrees of freedom models. Rotorcraft models provide three more degrees of freedom for the main flapping plus a rotational degree of freedom. Additional degrees of freedom for structural modes and other dynamic components (e.g., transmissions) can be added as necessary. The aircraft models are based on aerodynamic coefficient representations of the major aircraft components, including the wing, fuselage, vertical tail, and horizontal tail. Mass distribution is represented by the center-of-gravity location and mass moments of inertia for the aircraft. A stability analysis is performed by trimming the forces and moments on the aircraft model for each flight condition. Force and moment derivatives are obtained through perturbations from trim in the state and control variables. These derivatives are used to represent the rigid-body motion of the aircraft as a set of linear first-order differential equations. The matrix representation of the aircraft motion is then used in the linear analysis package MATLAB∗ to assess stability and to investigate feedback control design. Aircraft dynamics and control system conceptual designs are typically analyzed with respect to dynamic performance, stability, and pilot/vehicle interface.

![](image/bd7c91ecddc882bc5045cf71e8eff618df31e9721a1583b1becf656fc55ab484.jpg)

<details>
<summary>text_image</summary>

z
y
V
γ
(x, y, z)
β
x
Vertical plane
Pitch plane
Right wing
μ
Horizon
</details>

Fig. 2.6. Coordinate system

Example 1. In this example, we will consider an aircraft whose equations of motion can be represented as a point mass, based on five variables (i.e., 5-DOF). The coordinate system for this example is illustrated in Figure 2.6.

Furthermore, the variables are defined as follows:

Let x, y, z = position variables,

V = velocity vector,

α = angle-of-attack (AOA),

β = velocity heading angle,

γ = velocity elevation angle,

µ = orientation angle of the aircraft body axes relative to the velocity vector.
