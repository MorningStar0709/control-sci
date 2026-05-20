# Postsampling Filters

The signal from the D-A converter is piecewise constant. This may cause difficulties for systems with weakly damped oscillatory modes because they may be excited by the small steps in the signal. In such a case it is useful to introduce a special postsampling filter that smoothes the signal before applying it to the actuator. In some cases this can be achieved by suitable modification of the actuator dynamics. In extreme cases it may be advisable to design special D-A converters that will give piecewise linear control signals.
