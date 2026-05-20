# 3.5 Autopilots

This section considers the design of autopilots utilizing the discussion of Section 3.2.1 on airframe transfer functions.
As can be seen from Figures 3.22 and 3.23, an autopilot is a closed-loop system inside the main guidance subsystem that ensures that the missile achieves accelerations as commanded and maintains stability;
the control system consists of a roll autopilot and, as will be discussed below, two essentially identical pitch and yaw autopilots.
The function of the autopilot is to stabilize and guide the missile by requesting fin deflections, which cause the missile body to rotate and hence translate.
Its basic job changes at the target acquisition phase from nulling the seeker gimbal angles (if used) to satisfying acceleration commands.
The fin servos respond to the commands ordered by the autopilot, and the actual fin deflection is computed by the balance between servo torque and aerodynamic hinge moment.
These fin deflections then act to force the airframe dynamic model.
Historically, autopilots were developed for aircraft flight control systems.
As a result, and because the transient response of an aircraft varies considerably with changes in airspeed and altitude, the gains of all autopilots were scheduled as a function of Mach number or dynamic pressure.
The autopilot requirements and limitations are closely related to the overall design of the guidance subsystem.
The aerodynamic characteristics of the missile airframe are an integral part of the autopilot design and operation.
Therefore, the autopilot refers to the missile airframe dynamics and associated stability augmentation system, which is designed so that the missile lateral acceleration follows the autopilot acceleration commands as closely as possible.
The design of an autopilot must be tailored to each individual missile airframe configuration and its associated aerodynamic characteristics, which are nonlinear functions of missile velocity, angle of attack, control surface deflection, and altitude.
Therefore, a properly designed autopilot provides a nearly linear response characteristic if changes in these parameters about their nominal design values are small.
It should be pointed out, however, that there are some missile designs that do not require an autopilot.
