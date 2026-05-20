We choose to write our system model in terms of turbine rotation angle $\theta _ { 1 } ;$ ; therefore, substitute $\dot { \theta } _ { 2 } = ( r _ { 1 } / r _ { 2 } ) \dot { \theta } _ { 1 }$ for the generator shaft angular velocity and $\ddot { \theta } _ { 2 } = ( r _ { 1 } / r _ { 2 } ) \ddot { \theta } _ { 1 }$ for the generator shaft angular acceleration in Eq. (2.42). Moving all dynamic variables to the left-hand side yields

$$J _ {1} \ddot {\theta} _ {1} + \frac {r _ {1} ^ {2}}{r _ {2} ^ {2}} J _ {2} \ddot {\theta} _ {1} + b _ {1} \dot {\theta} _ {1} + \frac {r _ {1} ^ {2}}{r _ {2} ^ {2}} b _ {2} \dot {\theta} _ {1} = T _ {\text { aero }} - \frac {r _ {1}}{r _ {2}} T _ {\text { gen }} \tag {2.43}$$

Finally, we can substitute the gear ratio $N = r _ { 2 } / r _ { 1 }$ into Eq. (2.43)

$$\left(J _ {1} + \frac {1}{N ^ {2}} J _ {2}\right) \ddot {\theta} _ {1} + \left(b _ {1} + \frac {1}{N ^ {2}} b _ {2}\right) \dot {\theta} _ {1} = T _ {\text { aero }} - \frac {1}{N} T _ {\text { gen }} \tag {2.44}$$

Equation (2.44) is the mathematical model of the wind turbine generator system. We can write the system model in a more compact form by defining the equivalent or “composite” inertia and friction coefficient as

$$J _ {c 1} = J _ {1} + \frac {1}{N ^ {2}} J _ {2}b _ {c 1} = b _ {1} + \frac {1}{N ^ {2}} b _ {2}$$

Therefore, the complete system model using the composite coefficients is

$$J _ {c 1} \ddot {\theta} _ {1} + b _ {c 1} \dot {\theta} _ {1} = T _ {\text { aero }} - \frac {1}{N} T _ {\text { gen }} \tag {2.45}$$

Composite terms $J _ { c 1 }$ and $b _ { c 1 }$ represent the equivalent inertia and friction coefficients experienced by the turbine shaft. The generator inertia “reflected” back to the turbine shaft through the gear train is $J _ { 2 } / N ^ { 2 }$ , and the generator friction coefficient “reflected” to the turbine shaft is $b _ { 2 } / N ^ { 2 }$ . The equivalent external torque applied to the turbine shaft is the sum of $T _ { \mathrm { a e r o } }$ and $- T _ { \mathrm { g e n } } / N$ .

Finally, note that we can rewrite the complete mathematical model (2.45) in terms of angular velocity of the turbine shaft using $\omega _ { 1 } = \dot { \theta } _ { 1 }$ and $\dot { \omega } _ { 1 } = \ddot { \theta } _ { 1 }$

$$J _ {c 1} \dot {\omega} _ {1} + b _ {c 1} \omega_ {1} = T _ {\text { aero }} - \frac {1}{N} T _ {\text { gen }} \tag {2.46}$$

Equation (2.46) is a first-order model of the wind turbine generator, and its solution will only yield angular velocity information. The reader should note the similarity between the wind turbine generator model (2.46) and the single-disk mechanical model (2.39) from Example 2.7.
