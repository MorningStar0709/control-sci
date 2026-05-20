# Example 8.10 (Active Suspension)

We return to the active-suspension problem of Example 2.2. Ride quality is to be measured according to the tracked air-cushion vehicle (TACV) specification [6, 7]—an upper bound on the power density spectrum of the vertical acceleration of the passenger compartment (mass M). The design objective, then, is to limit the vertical acceleration in a frequency-selective manner. At the same time, the extension of the suspension spring must also be limited; ideally, the mass M is motionless while the suspension stretches and contracts to follow the road. This is clearly impractical, as the vehicle moves over hills and valleys.

Road roughness is specified as a power density spectrum of the form $A/\omega^{2}$ . Thus, the power density spectrum of any output variable z in response to the input $y_{R}$ is $(A/\omega^{2})|T_{y_{Rz}}(j\omega)|^{2}$ . We may therefore consider specifications on $(\sqrt{A}/s)T_{y_{Rz}}(s)$ . We use A = 0.25; this corresponds to a standard deviation of the change in road level of 0.5 m over the 27 m traversed in one second by a vehicle moving at 100 km/h.

The specifications are as follows:

- The weighted vertical acceleration transmission $(.5 / s)T_{y_Ra}(s)$ shall be bounded in magnitude by the TACV specifications curve,   
- The weighted transmission of the spring extension $\ell = x_{1} - x_{2}$ shall be bounded in magnitude by 0.15 at all frequencies.

Design the active suspension control, using $H_{\infty}$ methods.
