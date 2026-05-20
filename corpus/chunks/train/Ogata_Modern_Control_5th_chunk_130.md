Pressure Systems. Consider the system shown in Figure 4–4(a). If we assume only small deviations in the variables from their respective steady-state values, then this system may be considered linear.

Let us define

$\bar { P }$ gas pressure in the vessel at steady state (before changes in pressure have= occurred), $\mathrm { l b } _ { \mathrm { f } } / \mathrm { f t } ^ { 2 }$

pi= small change in inflow gas pressure, $\mathrm { l b } _ { \mathrm { f } } / \mathrm { f t } ^ { 2 }$

po= small change in gas pressure in the vessel, $\mathrm { l b } _ { \mathrm { f } } / \mathrm { f t } ^ { 2 }$

V= volume of the vessel, ft3

m= mass of gas in the vessel, lb

q= gas flow rate, lbsec

$\rho = \mathrm { \ d e n s i t y { \mathrm { ~ o f ~ } } g a s , l b / f t ^ { 3 } }$

For small values of $p _ { i }$ and $p _ { o }$ , the resistance R given by Equation (4–8) becomes constant and may be written as

$$R = \frac {p _ {i} - p _ {o}}{q}$$

The capacitance C is given by Equation (4–9), or

$$C = \frac {d m}{d p}$$

Since the pressure change $d p _ { o }$ times the capacitance C is equal to the gas added to the vessel during dt seconds, we obtain

$$C d p _ {o} = q d t$$

or

$$C \frac {d p _ {o}}{d t} = \frac {p _ {i} - p _ {o}}{R}$$

which can be written as

$$R C \frac {d p _ {o}}{d t} + p _ {o} = p _ {i}$$

If $p _ { i }$ and $p _ { o }$ are considered the input and output, respectively, then the transfer function of the system is

$$\frac {P _ {o} (s)}{P _ {i} (s)} = \frac {1}{R C s + 1}$$

where RC has the dimension of time and is the time constant of the system.

Pneumatic Nozzle–Flapper Amplifiers. A schematic diagram of a pneumatic nozzle–flapper amplifier is shown in Figure 4–5(a). The power source for this amplifier is a supply of air at constant pressure. The nozzle–flapper amplifier converts small changes in the position of the flapper into large changes in the back pressure in the nozzle. Thus a large power output can be controlled by the very little power that is needed to position the flapper.

In Figure $4 \mathrm { - } 5 ( \mathrm { a } )$ , pressurized air is fed through the orifice, and the air is ejected from the nozzle toward the flapper. Generally, the supply pressure $P _ { s }$ for such a controller is 20 psig $( 1 . 4 ~ \mathrm { k g _ { f } } / \mathrm { c m } ^ { 2 }$ gage). The diameter of the orifice is on the order of 0.01 in. (0.25 mm) and that of the nozzle is on the order of 0.016 in. (0.4 mm). To ensure proper functioning of the amplifier, the nozzle diameter must be larger than the orifice diameter.
