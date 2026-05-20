# Eurotherm Temperature Controller

Temperature control is traditionally done with simple PID controllers, which are cheaper than conventional industrial controllers. Auto-tuning is now also used in such simple systems. One example is controllers produced by Eurotherm in the United Kingdom. A modified relay tuning is used in those controllers. Full control power is used until an artificial setpoint is reached. Two half-periods of a relay tuning are then used, and the controller parameters are calculated from the transient. The controller also has facilities for automatic on-line tuning based on transient response analysis.

In temperature control loops, there are usually different dynamics depending on whether the temperature is increasing or decreasing. This nonlinearity can be handled by using gain scheduling.
