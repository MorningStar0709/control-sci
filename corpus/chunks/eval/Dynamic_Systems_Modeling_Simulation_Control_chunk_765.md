# Discontinuities Library

Coulomb and Viscous Friction: computes the Coulomb (dry) friction based on the sign of the input and the viscous friction coefficient. The user defines the offset (dry friction) value and the viscous friction coefficient.

Relay: determines an “on” or “off” output signal that depends on the input. The user defines the desired output values corresponding to “on” and “off” and the input thresholds for the switch-on and switch-off points.

Saturation: limits the output to be between upper and lower values set by the user. If the input signal is between the upper/lower limits, the output is equal to the input. If the input is greater than the upper limit, the output is set to the upper value; if the input is less than the lower limit, the output is set to the lower value.
