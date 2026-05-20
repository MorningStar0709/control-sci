# 7.3 FIRST-ORDER SYSTEM RESPONSE

Recall that many of the mathematical models we derived in Chapters 2–4 for physical engineering systems were first-order differential equations. Table 7.1 summarizes several examples of systems represented by first-order I/O equations. In the case of the electrical, pneumatic, and thermal systems in Table 7.1, we obtain a first-order model because each system has only one energy-storage element, namely, a single electrical capacitance, fluid capacitance, or thermal capacitance element, all denoted by the symbol C. Furthermore, the electrical, pneumatic, and thermal systems in Table 7.1 all contain a single resistance element (electrical resistor, fluid resistance, or thermal resistance), all denoted by symbol R. The mechanical rotor example in Table 7.1 can be written as a first-order system only if angular position ?? does not appear in the modeling equation.

Note that all first-order models of the physical systems in Table 7.1 have the same standard form

$$\tau \dot {y} + y = b u \tag {7.25}$$

where y is the dynamic or output variable of interest, u is the input variable, and b is the right-hand side coefficient. The constant ?? in Eq. (7.25) must have units of time so that the dimensions of the first term on the left-hand side (?? ̇y) match the dimensions of the second term (y). Table 7.2 defines the output variable and constant ?? for every first-order model presented in Table 7.1. The constant ?? is the product of the resistance and capacitance elements for the electrical, pneumatic, and thermal systems. We characterize the first-order system response in terms of the constant ??, so it is important for the reader to note that we can write any linear, first-order model in the “standard form” of Eq. (7.25).

Table 7.1 Examples of Engineering Systems Modeled by a First-Order Input-Output Equation
