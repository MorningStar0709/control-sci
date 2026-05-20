# 4–5 THERMAL SYSTEMS

Thermal systems are those that involve the transfer of heat from one substance to another. Thermal systems may be analyzed in terms of resistance and capacitance, although the thermal capacitance and thermal resistance may not be represented accurately as lumped parameters, since they are usually distributed throughout the substance. For precise analysis, distributed-parameter models must be used. Here, however, to simplify the analysis we shall assume that a thermal system can be represented by a lumped-parameter model, that substances that are characterized by resistance to heat flow have negligible heat capacitance, and that substances that are characterized by heat capacitance have negligible resistance to heat flow.

There are three different ways heat can flow from one substance to another: conduction, convection, and radiation. Here we consider only conduction and convection. (Radiation heat transfer is appreciable only if the temperature of the emitter is very high compared to that of the receiver. Most thermal processes in process control systems do not involve radiation heat transfer.)

For conduction or convection heat transfer,

$$q = K \Delta \theta$$

where q=heat flow rate, kcalsec

$$\Delta \theta = \text { temperature difference }, ^ {\circ} \mathrm{C}K = \text { coefficient }, \mathrm{kcal} / \sec^ {\circ} \mathrm{C}$$

The coefficient K is given by

$$
\begin{array}{l} K = \frac {k A}{\Delta X}, \quad \text {   for   conduction   } \\ = H A, \quad \text {   for   convection   } \\ \end{array}
$$

where k=thermal conductivity, kcalm sec °C

$$A = \text { area normal to heat flow, } m ^ {2}\Delta X = \text { thickness of conductor, m }H = \text { convection coefficient }, \mathrm{kcal} / \mathrm{m} ^ {2} \sec {} ^ {\circ} \mathrm{C}$$

Thermal Resistance and Thermal Capacitance. The thermal resistance R for heat transfer between two substances may be defined as follows:

$$R = \frac {\text { change in temperature difference, } ^ {\circ} \mathrm{C}}{\text { change in heat flow rate, kcal / sec }}$$

The thermal resistance for conduction or convection heat transfer is given by

$$R = \frac {d (\Delta \theta)}{d q} = \frac {1}{K}$$

Since the thermal conductivity and convection coefficients are almost constant, the thermal resistance for either conduction or convection is constant.

The thermal capacitance C is defined by
