The linear approximation is based on the fact that the actual curve does not differ much from its tangent line if the operating condition does not vary too much.

The capacitance C of a tank is defined to be the change in quantity of stored liquid necessary to cause a unit change in the potential (head). (The potential is the quantity that indicates the energy level of the system.)

$$C = \frac {\text { change in liquid stored, } \mathrm{m} ^ {3}}{\text { change in head, } \mathrm{m}}$$

It should be noted that the capacity $( \mathbf { m } ^ { 3 } )$ and the capacitance $( \mathbf { m } ^ { 2 } )$ are different. The capacitance of the tank is equal to its cross-sectional area. If this is constant, the capacitance is constant for any head.

Liquid-Level Systems. Consider the system shown in Figure 4–1(a). The variables are defined as follows:

$$\bar {Q} = \text { steady - state flow rate (before any change has occurred) }, \mathrm{m} ^ {3} / \secq _ {i} = \text { small deviation of inflow rate from its steady - state value, } \mathrm{m} ^ {3} / \mathrm{sec}q _ {o} = \text { small deviation of outflow rate from its steady - state value, } \mathrm{m} ^ {3} / \sec\bar {H} = \text { steady - state head (before any change has occurred) }, mh = \text { small deviation of head from its steady - state value, m }$$

As stated previously, a system can be considered linear if the flow is laminar. Even if the flow is turbulent, the system can be linearized if changes in the variables are kept small. Based on the assumption that the system is either linear or linearized, the differential equation of this system can be obtained as follows: Since the inflow minus outflow during the small time interval dt is equal to the additional amount stored in the tank, we see that

$$C d h = \left(q _ {i} - q _ {o}\right) d t$$

From the definition of resistance, the relationship between $q _ { o }$ and h is given by

$$q _ {o} = \frac {h}{R}$$

The differential equation for this system for a constant value of R becomes

$$R C \frac {d h}{d t} + h = R q _ {i} \tag {4-2}$$

Note that RC is the time constant of the system. Taking the Laplace transforms of both sides of Equation (4–2), assuming the zero initial condition, we obtain

$$(R C s + 1) H (s) = R Q _ {i} (s)$$

where

$$H (s) = \mathscr {L} [ h ] \quad \text { and } \quad Q _ {i} (s) = \mathscr {L} [ q _ {i} ]$$

If $q _ { i }$ is considered the input and h the output, the transfer function of the system is

$$\frac {H (s)}{Q _ {i} (s)} = \frac {R}{R C s + 1}$$
