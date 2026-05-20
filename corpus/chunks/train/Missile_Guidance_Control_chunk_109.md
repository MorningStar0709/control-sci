In Section 3.2 the various forces and moments acting on a missile were developed. In this section, we will discuss the stability conditions in terms of the airframe dynamics. Specifically, in an aerodynamically maneuvering missile, the function of the control surfaces is to exert a moment so that the missile can develop an angle of attack (AOA), and thereby achieve lift from the body and wings (if any). (Note that in some applications, a wingless airframe relying only on body-lift is preferred.) As will be discussed further in the autopilot section, the pitching of the airframe causes the seeker to develop a spurious component of the measured line-of-sight (LOS) angular rate $d \lambda / d t$ , which results in a parasitic attitude loop.∗ An important measure of the necessary pitching of the airframe is the alpha over gamma dot $( \alpha / \dot { \gamma } )$ time constant, τ , of the linearized airframe response, defined by the following relation:

$$\tau = \alpha / \dot {\gamma} = \frac {2 M}{\rho V _ {m} S} \left[ \frac {\frac {\partial C _ {m}}{\partial \delta}}{\frac {\partial C _ {L}}{\partial \alpha} \left(\frac {\partial C _ {m}}{\partial \delta}\right) - \frac {\partial C _ {L}}{\partial \delta} \left(\frac {\partial C _ {m}}{\partial \alpha}\right)} \right],$$

where

M = mass of the missile,

Vm = missile speed,

S = missile reference area,

α = angle of attack,

γ = flight path angle,

ρ = air (or atmospheric) density,

![](image/90684ad27541e2dd06d591523eaa90efe95bc0424fe5f24296ca8cc163820b23.jpg)

<details>
<summary>text_image</summary>

Fα·α
+Mα·α
Icp
Icg
Center of pressure
Center of gravity
</details>

(a) Stable condition: ${ \cal M } _ { \alpha } { < } 0$

![](image/8d3a271685450f44f622d025fbba6c61955e3171504d81959b0f63fae0e57ef8.jpg)

<details>
<summary>text_image</summary>

Fα · α
Icp
Icg
Center of gravity
Center of pressure
</details>

(b) Unstable condition: ${ \cal M } _ { \alpha } > 0$

$$M _ {\alpha} = \frac {F _ {\alpha} (\mathrm{I} _ {c g} - \mathrm{I} _ {c p})}{\mathrm{I} _ {\text { pitch }}} = \frac {\mathrm{qSdC} _ {\mathrm{m} \alpha}}{\mathrm{I} _ {\text { pitch }}}(d = \text { diameter of the missile })$$

Fig. 3.13. Aerodynamic missile stability conditions.
