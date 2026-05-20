# Example 6.7

Give two examples of disturbances in control systems. Identify the inputs and outputs and explain what is the disturbance signal.

1) Consider an automatic pilot on a commercial aircraft. The input to the automatic pilot is the desired heading in degrees relative to North. The output of the system is the plane's actual heading, for example as sensed by a compass. Gusts of wind which blow the plane o its heading constitute an external disturbance.   
2) Consider the temperature control system for a refrigerator. The input is the desired temperature (such as a constant value of 38 deg F.). The system output is the actual temperature inside the refrigerator.   
When the door is opened there is an input of warm air which increases the air temperature. This increase in temperature is a disturbance.

The block diagram of Figure 6.6 is a representation of a closed loop negative feedback system with a disturbance, d(t). Let's calculate the output, Y .

$$Y = D + E GY = D + G (X - Y H)Y (1 + G H) = D + G XY = \frac {D}{(1 + G H)} + \frac {G}{(1 + G H)} X \tag {6.4}$$

The output thus consists of two components, one due to the disturbance, D, and one due to the input, X. Note what happens however when GH >> 1. In that case

$$Y \approx D / G H + X \frac {1}{H}$$

The disturbance input is reduced by the loop gain, GH.

Disturbance Examples There are many phenomena which can be treated as disturbances in analysis of a control system and thus reduced by Equation 6.4. Some frequently encountered disturbances include:

 Electrical Noise (additive)   
 Vibrations   
 Unmodeled exibility or mechanical resonance.

 Unmodeled mechanical eects such as non-linear friction, or eects of temperature on mechanical parameters.
