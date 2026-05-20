where the single input heat flow rate is clearly $q _ { \mathrm { B H } }$ and the output heat flow rates from the room to its surroundings are $q _ { i } , i = 1 , 2 , \ldots , 6$ . Each of the six output heat flow rates can be expressed using Eq. (4.81) and the temperature difference across the corresponding thermal resistance surface and its thermal resistance $R _ { i }$

$$q _ {i} = \frac {T - T _ {a}}{R _ {i}} \quad i = 1, 2, \dots , 6 \tag {4.87}$$

where $T _ { a }$ is the ambient (exterior) temperature. Substituting Eq. (4.87) for the six output heat flow rates into the energy balance equation (4.86) we obtain

$$C \dot {T} = q _ {\mathrm{BH}} - \frac {T - T _ {a}}{R _ {1}} - \frac {T - T _ {a}}{R _ {2}} - \frac {T - T _ {a}}{R _ {3}} - \frac {T - T _ {a}}{R _ {4}} - \frac {T - T _ {a}}{R _ {5}} - \frac {T - T _ {a}}{R _ {6}} \tag {4.88}$$

Equation (4.88) is an acceptable form for the thermal system model. However, we can simplify Eq. (4.88) using the following compact notation

$$C \dot {T} = q _ {\mathrm{BH}} - \sum_ {i = 1} ^ {6} \frac {T - T _ {a}}{R _ {i}} \tag {4.89}$$

Equation (4.89) can be further simplified as

$$C \dot {T} = q _ {\mathrm{BH}} - \frac {T - T _ {a}}{R _ {\mathrm{EQ}}} \tag {4.90}$$

where $R _ { \mathrm { E Q } }$ is the equivalent (or combined) thermal resistance defined by

$$\frac {1}{R _ {\mathrm{EQ}}} = \frac {1}{R _ {1}} + \frac {1}{R _ {2}} + \dots + \frac {1}{R _ {6}} = \sum_ {i = 1} ^ {6} \frac {1}{R _ {i}} \tag {4.91}$$

The reader should note that the equivalent thermal resistance is defined in the same manner as the equivalent electrical resistance for parallel resistors. Finally, we can move all terms involving the dynamic variable T in

Eq. (4.90) to the left-hand side to yield

$$R _ {\mathrm{EQ}} C \dot {T} + T = R _ {\mathrm{EQ}} q _ {\mathrm{BH}} + T _ {a} \tag {4.92}$$

Equation (4.92) is the mathematical model of the thermal system and is equivalent to Eq. (4.88). Room temperature T is the dynamic variable and baseboard heater input $q _ { \mathrm { B H } }$ and ambient temperature $T _ { a }$ are the two system inputs.
