Each flight section consists of cut-off time (sec), vacuum thrust (Newtons), fuel burn rate (kg/sec), dry mass (kg), reference area (m2), nozzle exit area $( \mathbf { m } ^ { 2 } )$ , coefficients of lift and drag as functions of Mach number, integration step size (sec), and missile stage identifier. These important performance variables will now be defined. The cut-off time is the absolute missile flight time when the model should transition to the next flight section. The vacuum thrust is the gross amount of missile propelling force, which is produced as the motor burns the fuel. The fuel burn rate is the speed at which the fuel is burned by the motor. The dry mass is the structure mass. The fuel mass is the amount of fuel that is available for thrust production. The reference area is the missile cross-sectional area. The nozzle exit area is the total area of the thrust outlet(s) of the missile motor. The coefficients of lift and drag define the lift and drag characteristics of the missile. The integration step size is the time over which to integrate the missile position, velocity, and expended fuel. The missile stage identifier signifies to which missile stage the dry mass and fuel mass correspond. When multiple flight sections are used to model a single missile stage, then their stage identifiers are set to the same value. Only masses of the first of those sections contribute to the total mass of the missile.

At the beginning of the flyout, the dry and fuel masses of the missile are calculated as follows:

$$M _ {D t} = \Sigma M _ {D}, \tag {6.252a}M _ {F T} = \Sigma M _ {F}, \tag {6.252b}$$

where

$$M _ {D t} = \text { total missile dry mass } [ \mathrm{kg} ],M _ {D} = \text { individual stage dry mass } [ \mathrm{kg} ],M _ {F T} = \text { total missile available fuel mass [kg]},M _ {F} = \text { individual stage available fuel mass } [ \mathrm{kg} ].$$

The total missile mass at liftoff is then calculated by

$$M _ {T} = M _ {D t} + M _ {F T}, \tag {6.253a}$$

where $M _ { T }$ is the total missile mass in [kg]. Throughout the flyout, the missile performance variables, that is, thrust, fuel burn rate, reference area, nozzle exit area, the lift/drag characteristics, and the integration step size, are all set using the parameters of the current flight section. Therefore, the total mass is updated by the following expression:

$$M _ {T} = M _ {D t} + M _ {F T} - \Delta M _ {F}, \tag {6.253b}$$
