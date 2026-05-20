# Example 1.14 Particle accelerators

Particle accelerators are the key experimental tool in particle physics. The Dutch engineer Simnon van der Meer made a major improvement in accelerators by introducing feedback to control particle paths, which made it possible to increase the beam intensity and to improve the beam quality substantially. The method, which is called stochastic cooling, was a key factor in the successful experiments at CERN. As a result van der Meer shared the 1984 Nobel Prize in Physics with Carlo Rubbia.

A schematic diagram of the system is shown in Fig. 1.14. The particles enter into a circular orbit via the injector. The particles are picked up by a detector at a fixed position and the energy of the particles is increased by the kicker, which is located at a fixed position. The system is inherently sampled because the particles are only observed when they pass the detector and control only acts when they pass the kicker.

From the point of view of sampled systems, it is interesting to observe that there is inherent sampling both in sensing and actuation.

The systems in these examples are periodic because of their pulsed operation. Periodic systems are quite difficult to handle, but they can be considerably simplified by studying the systems at instants synchronized with the pulses—that is, by using sampled-data models. The processes then can be described as time-invariant discrete-time systems at the sampling instants. Examples 1.11 and 1.13 are of this type.
