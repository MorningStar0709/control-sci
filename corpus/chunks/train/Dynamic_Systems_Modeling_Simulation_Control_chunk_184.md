# Thermal Resistance

Heat can be transferred in three ways: conduction, convection, and radiation. Conduction involves the diffusion of heat energy between two bodies that are in physical contact, such as heat transfer through a solid material. Convection involves the transfer of heat energy through the motion of a fluid. Radiation involves the transfer of heat through the absorption of electromagnetic radiation such as infrared waves and solar energy. Conductive or convective heat transfer can be approximated by a linear function of temperature difference, while heat transfer via radiation is a highly nonlinear function of the temperature difference. Therefore, we consider only conduction and convection in this section.

Thermal resistance elements hinder (resist) the flow of heat energy despite a temperature difference. Thermal insulating materials can be modeled as thermal resistance elements. For conduction or convection, the rate of heat transfer q can be approximated by a linear function of the temperature difference $\Delta T$

$$q = \frac {1}{R} \Delta T \tag {4.81}$$

where R is the thermal resistance (in K-s/J or K/W). Another way to express Eq. (4.81) is $\Delta T = R q$ , which is analogous to Ohm’s law for an electrical resistor $( e _ { R } = R I )$ ), where heat-flow rate $q$ is analogous to electrical current I and temperature difference $\Delta T$ is analogous to voltage drop $e _ { R }$ . Equation (4.81) makes sense intuitively if we consider two extreme cases. When thermal resistance is infinite, R → ∞ (i.e., perfect insulation), the heat transfer rate $q \to 0$ despite the magnitude of the temperature difference ΔT between the two bodies. At the other extreme, when $R \to 0 ( { \mathrm { i . e } }$ ., zero insulation) the heat transfer rate $q \to \infty$ , which implies that the heat is transferred instantaneously between two bodies.

Thermal resistance R for conduction is proportional to the thickness of the material (x) and inversely proportional to area normal to the heat flow (A) and the material’s thermal conductivity coefficient (k):

$$\text { Conduction: } \quad R = \frac {x}{k A} \tag {4.82}$$

For example, copper has a thermal conductivity coefficient k that is on the order of 18 times greater than the conductivity coefficient for stainless steel. Consequently, copper is an excellent conductor of heat and a poor insulating material.

Thermal resistance R for convection is inversely proportional to the area A and the convection coefficient H:

$$\text { Convection: } \quad R = \frac {1}{H A} \tag {4.83}$$

The convection coefficient for water is 50–100 times greater than the convection coefficient for air, and hence air is a better insulator compared to water.
