# 5.11 Guided Weapons

In this section we will briefly discuss guided weapons, with particular emphasis on guidance techniques (see also Section 4.8, and Appendices E and F).
Specifically, we will address the problem of optimal control theory that supports highly sophisticated weapon delivery system requirements.
These guided weapons (or missiles) are capable of covering a large target accessibility footprint when launched with a wide range of initial conditions.
In guided missiles, a guidance algorithm is commonly programmed into the missile’s onboard digital computer, which computes steering angles and motor ignition times during the powered phase of the flight.
Specifically, the function of the guidance algorithm is to guarantee that in the presence of perturbations and model approximations, the missile still satisfies all mission requirements, especially terminal accuracy.
The main advantage of using modern control theory is the flexibility in designing an optimal guidance law that minimizes a performance or cost index.
Among the guidance laws the missile analyst has at his disposal are proportional navigation (PN), the method of singular perturbation technique (SPT), and Kalman filter trackers.
In proportional navigation, the missile launched from an aircraft is made to hit a target by pointing the relative velocity vector at the target at every point in the flight path.
Also, the line-of-sight (LOS) rate is driven to zero by lateral acceleration commands proportional to the LOS.
In standoff weapon delivery cases for ranges, perhaps up to 277.8 km (150 nm) a missile will require precise guidance and in-flight missile updates to reduce the system errors and terminal miss distance in minimum time.
That is, the objective of minimum time is to transfer a system from an arbitrary initial state $\mathbf { x } _ { 0 }$ at time $t = 0$ to a final state x(T ) in minimum time.
For a more detailed discussion of minimum time, see [10].
The performance index can be selected to reflect the requirements of a given or desired mission.
For example, the guidance algorithm used in the SRAM II (short-range attack missile) is a linear quadratic regulator (LQR) with a terminal controller derived from modern control theory.
A regulator is designed to keep a stationary system within an acceptable deviation from a reference condition using acceptable amounts of control.
