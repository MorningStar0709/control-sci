# Pneumatic Capacitance

Because pneumatic systems often involve gas flowing into a constant-volume vessel, the fluid capacitance C is usually defined as the ratio of the change in mass m to the change in pressure $P$

$$C = \frac {d m}{d P} \tag {4.60}$$

that has units of kg/Pa or $\mathrm { k g - m } ^ { 2 } / \mathrm { N }$ . The mass of a gas in a vessel is $m = \rho V$ , and, therefore, the differential of mass for a constant-volume vessel is $d m = V d \rho$ . Consequently, the pneumatic capacitance (4.60) for a constant-volume container becomes

$$C = V \frac {d \rho}{d P} \tag {4.61}$$

Therefore, pneumatic capacitance depends on the compressibility of the gas with respect to change in pressure. Recall that from basic thermodynamics the expansion process of a gas may be at a constant temperature (isothermal), constant pressure (isobaric), or constant entropy (isentropic). We consider here isothermal and isentropic (adiabatic and reversible) processes, which we can model with the polytropic process

$$\frac {P}{\rho^ {n}} = a \text { or } P = a \rho^ {n} \tag {4.62}$$

where a is a constant and n is the polytropic exponent. For an isothermal process n = 1; for an isentropic process $n = \gamma$ . Taking differentials of both sides of Eq. (4.62) yields

$$d P = a n \rho^ {n - 1} d \rho \tag {4.63}$$

Solving Eq. (4.63) for $d \rho / d P$ we obtain

$$\frac {d \rho}{d P} = \frac {\rho^ {1 - n}}{a n} = \frac {\rho \rho^ {- n}}{a n} \tag {4.64}$$

Next, solve Eq. (4.62) for the constant $a = P \rho ^ { - n }$ and substitute into Eq. (4.64) to yield

$$\frac {d \rho}{d P} = \frac {\rho}{n P} \tag {4.65}$$

Using the ideal gas law (4.56) to substitute for pressure P in Eq. (4.65) the derivative $d \rho / d P$ becomes

$$\frac {d \rho}{d P} = \frac {1}{n R T} \tag {4.66}$$

Finally, substituting Eq. (4.66) into Eq. (4.61) yields the pneumatic capacitance for a constant-volume vessel:

$$C = \frac {V}{n R T} \tag {4.67}$$

Note that the pneumatic capacitance of a fixed vessel can vary depending on the gas temperature, type of gas, and thermodynamic process.

We can separate variables in the pneumatic capacitance equation (4.60) to obtain CdP = dm and divide this result by dt to yield the differential equation

$$C \dot {P} = \dot {m} = w \tag {4.68}$$

Equation (4.68) is analogous to the fundamental equation of an electrical capacitor and the hydraulic reservoir derived in Section 4.2.
