# Modeling Thermal Systems

Thermal system models are based on the energy balance equation (4.80) where the rate of energy stored by the thermal capacitance is $\dot { \xi } _ { h } = C \dot { T }$ as capacitance has units of J/K and the time-rate of temperature has units of K/s. Substituting the time-rate of enthalpy ${ \dot { h } } = { \dot { m } } c _ { p } T$ into Eq. (4.80) we obtain

$$C \dot {T} = \sum \dot {m} _ {\text { in }} c _ {p} T _ {\text { in }} - \sum \dot {m} _ {\text { out }} c _ {p} T _ {\text { out }} + \sum q _ {\text { in }} - \sum q _ {\text { out }} \tag {4.85}$$

where $T _ { \mathrm { i n } }$ and $T _ { \mathrm { o u t } }$ are the fluid temperatures of the streams flowing into and out of the thermal capacitance, respectively, and T is the uniform temperature of the lumped thermal capacitance.

Models of thermal systems can be derived using the following steps:

1. Draw a thermal system boundary around each thermal capacitance, identifying whether the system is a closed or an open system.   
2. Label the input and output heat transfer rates $q _ { i }$ between thermal capacitances or their surroundings. For open systems, label the enthalpy rates $\dot { h } _ { i }$ due to mass flowing into or out of the thermal capacitance.   
3. Apply the energy balance equation (4.85) to each thermal capacitance.

It is important to note that the resulting mathematical model will consist of one first-order differential equation for each thermal capacitance where the dynamic variable is the temperature of each capacitance. We illustrate this modeling process with the following examples.
