# Example 4.3

Figure 4.12 shows an accumulator in a hydraulic circuit where $Q _ { \mathrm { i n } }$ is the input volumetric-flow rate. Derive the mathematical model of the complete system.

Accumulators are placed downstream from hydraulic sources (e.g., pumps) in order to attenuate (reduce) ripples or spikes in flow rate or pressure. The system shown in Fig. 4.12 consists of a hose (with constant volume $V _ { h } )$ connecting a pump to a hydraulic load. The load might be a hydraulic motor that is part of a hydrostatic transmission, which may require a prescribed flow rate $Q _ { h }$ for proper operation. The accumulator consists of a chamber with pressure $P _ { c }$ and volume $V _ { c }$ and a movable plate (mass m) restrained by spring k. High-pressure fluid is allowed to flow from the hose to the accumulator through a sharp-edged orifice with constant area $A _ { 0 }$ . The accumulator can store fluid during rapid increases in hose pressure $P _ { h }$ and release fluid to the hose during rapid decreases in hose pressure. Consequently, accumulators are used to dampen out fluctuations in hose pressure or flow-rate.

We begin by applying the pressure-rate equation (4.40) to each fluid CV: the hose CV and the accumulator CV

$$\text { Hose: } \quad \dot {P} _ {h} = \frac {\beta}{V _ {h}} (Q _ {\text { in }} - Q _ {c} - Q _ {h} - \dot {V} _ {h}) \tag {4.46}\text { Accumulator: } \quad \dot {P} _ {c} = \frac {\beta}{V _ {c}} (Q _ {c} - \dot {V} _ {c}) \tag {4.47}$$

Note that in Eq. (4.46) the net volumetric-flow rate into the hose CV is $Q _ { \mathrm { i n } } - Q _ { c } - Q _ { h }$ . Furthermore, the hose volume $V _ { h }$ is constant, and, therefore, $\dot { V } _ { h } = 0$ in Eq. (4.46). We can use Eq. (4.9) to represent the turbulent flow through the sharp-edged orifice

$$Q _ {c} = C _ {d} A _ {0} \sqrt {\frac {2}{\rho} (P _ {h} - P _ {c})} \tag {4.48}$$

![](image/1b1c8c70a036cff22b237eeb36700a766c1fd9168ec4495907353edb63952e81.jpg)

<details>
<summary>text_image</summary>

Atmospheric pressure, P_atm
k
Accumulator
P_c, V_c
Plate mass, m
Area, A
Orifice
Q_c
(from pump)
Q_in →
P_h Hose volume, V_h (to load)
Q_h
</details>

Figure 4.12 Hydraulic accumulator for Example 4.3.
