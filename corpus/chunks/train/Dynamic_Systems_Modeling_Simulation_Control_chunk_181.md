# Example 4.6

Consider again the pneumatic system from Example 4.5. Compute the pneumatic capacitance C and initial massflow rate $w _ { \mathrm { i n } }$ through the valve if the system has the following characteristics at the instant the valve is opened: chamber volume $\bar { V = 3 } ( 1 0 ^ { - 4 } ) \mathrm { m } ^ { 3 }$ , upstream air temperature $T = 2 9 8 \mathrm { K }$ , upstream supply pressure $P _ { S } = 6 ( 1 0 ^ { 5 } )$ Pa, downstream chamber pressure $P = 1 . 2 ( 1 0 ^ { 5 } )$ Pa, discharge coefficient $C _ { d } = 0 . 8$ , and valve area $A _ { 0 } = 2 ( 1 0 ^ { - 6 } ) ~ \mathrm { m } ^ { 2 }$ . Assume an isothermal expansion process with air as the working gas.

Equation (4.67) defines the pneumatic capacitance for a fixed-volume vessel:

$$C = \frac {V}{n R T}$$

where $n = 1$ (isothermal process) and $R { = } 2 8 7 \mathrm { N } { \mathrm { - } } \mathrm { m } / \mathrm { k g } { \mathrm { - } } \mathrm { K }$ is the gas constant for air. Using the pneumatic characteristics given for this problem, the pneumatic capacitance is $C { = } 3 . 5 0 7 7 ( 1 0 ^ { - 9 } ) \mathrm { k g { - } m ^ { 2 } / N }$ .

The initial input mass-flow rate $w _ { \mathrm { i n } }$ is determined by either Eq. (4.57) for unchoked flow or Eq. (4.58) for choked flow. Hence, we must compute the initial downstream-to-upstream pressure ratio $P / P _ { S }$ and compare this ratio with the critical pressure ratio, where $C _ { r } { = } 0 . 5 2 8$ for air (see Eq. (4.59)). The initial pressure ratio is $P / P _ { S } = 1 . 2 ( 1 0 ^ { 5 } ) / 6 ( 1 0 ^ { 5 } ) = 0 . 2$ , which is less than the critical pressure ratio $C _ { r }$ . Therefore, the initial mass-flow rate is choked, and we compute its numerical value using Eq. (4.58)

$$w _ {\mathrm{in}} = C _ {d} A _ {0} P _ {S} \sqrt {\frac {\gamma}{R T} C _ {r} ^ {\frac {\gamma + 1}{\gamma}}}$$

where $\gamma = 1 . 4$ for air. Using the numerical values for the gas and valve characteristics in the above equation yields $w _ { \mathrm { i n } } { = } 0 . 0 0 2 2 4 8 \mathrm { k g / s }$ .
