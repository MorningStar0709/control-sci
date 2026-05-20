where $\rho$ is the nominal fluid density and $C _ { d }$ is the discharge coefficient. The reader should note that Eq. (4.48) indicates flow from the hose to the accumulator that occurs when $P _ { h } > P _ { c }$ as depicted in Fig. 4.12. However, it is possible for the accumulator pressure to exceed the hose pressure, which would reverse the direction (and sign) of flow $Q _ { c }$ . For this case, $P _ { c } > P _ { h }$ and we cannot use Eq. (4.48) because the radicand would be negative. Therefore, we can modify Eq. (4.48) to produce a general equation that accommodates positive or negative orifice flow

$$Q _ {c} = C _ {d} A _ {0} \operatorname{sgn} (P _ {h} - P _ {c}) \sqrt {\frac {2}{\rho} | P _ {h} - P _ {c} |} \tag {4.49}$$

Note that the radicand is always positive (due to the absolute value of the pressure difference) and that the signum function operation sgn $( P _ { h } - P _ { c } )$ results in either +1, −1, or zero, and, therefore, determines whether orifice flow is positive (hose to accumulator), negative (accumulator to hose), or zero.

The accumulator volume is

$$V _ {c} = V _ {c 0} + A x \tag {4.50}$$

where $V _ { c 0 }$ is the accumulator volume when $x = 0$ . Plate position x is measured from the static equilibrium position where the spring force balances the nominal pressure force. It is clear that the time-rate of the accumulator CV is ${ \dot { V } } _ { c } = A { \dot { x } }$ .

Next, we derive the mechanical model for the accumulator plate mass by utilizing the free-body diagram shown in Fig. 4.13. Note that we have assumed that linear viscous friction acts on the plate (bẋ ) and that atmospheric pressure $P _ { \mathrm { a t m } }$ acts on the top part of the plate. Furthermore, the accumulator spring is initially compressed in order to balance the nominal pressure force and hence the spring preload force $F _ { \mathrm { P I } }$ is included in the freebody diagram. The reader should note that when the plate is at rest at position $x = 0 .$ , the accumulator is in static equilibrium and the preload $F _ { \mathrm { P L } }$ balances the pressure forces. Summing all external forces on plate mass m yields

$$+ \uparrow \sum F = P _ {c} A - k x - F _ {\mathrm{PL}} - P _ {\mathrm{atm}} A - b \dot {x} = m \ddot {x} \tag {4.51}$$

or, after rearranging Eq. (4.51)

$$m \ddot {x} + b \dot {x} + k x = (P _ {c} - P _ {\mathrm{atm}}) A - F _ {\mathrm{PL}} \tag {4.52}$$
