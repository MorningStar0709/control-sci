<table><tr><td>System Parameter</td><td>Value</td></tr><tr><td>Coil resistance,  $R$ </td><td>3 Ω</td></tr><tr><td>Iron core/air permeability,  $\mu$ </td><td> $800\pi(10^{-7}) \text{ N/A}^{2}$ </td></tr><tr><td>Length of coil,  $l$ </td><td>0.04 m</td></tr><tr><td>Area of the air gap,  $A$ </td><td> $\pi(10^{-4}) \text{ m}^{2}$ </td></tr><tr><td>Characteristic displacement,  $d$ </td><td>0.0078 m</td></tr><tr><td>Armature–valve mass,  $m$ </td><td>0.05 kg</td></tr><tr><td>Viscous friction coefficient,  $b$ </td><td>10 N·s/m</td></tr><tr><td>Dry-friction force,  $F_{\text{dry}}$ </td><td>0 N</td></tr><tr><td>Preload spring force,  $F_{\text{PL}}$ </td><td>2 N</td></tr></table>

This back-emf voltage term appears on the right-hand side of the solenoid coil equation (11.9) with a negative sign. Consequently, positive velocity of the armature decreases the net voltage in the coil. Using Eq. (11.11), the derivative $d L / d x$ is

$$\frac {d L}{d x} = L _ {x} = \frac {L _ {0}}{d (1 - x / d) ^ {2}} \tag {11.14}$$

The electromagnetic force $F _ { \mathrm { e m } }$ of the solenoid was also derived in Chapter 3, and it is a nonlinear function of current

$$F _ {\mathrm{em}} = \frac {1}{2} \frac {d L}{d x} I ^ {2} \tag {11.15}$$

Equations (11.13) and (11.15) show that both the back emf and electromagnetic force depend on the derivative $L _ { x } .$ . In order to simplify our simulation model, we assume that the change in inductance L is constant with position x, which is a reasonable assumption for a 2-mm displacement. Hence, we define the constant $K = d L / d x$ and compute K using Eq. (11.14) with a nominal displacement $x _ { \mathrm { n o m } } = 0 . 0 0 1$ m (1 mm) and the initial inductance $L _ { 0 }$ using Eq. (11.12).
