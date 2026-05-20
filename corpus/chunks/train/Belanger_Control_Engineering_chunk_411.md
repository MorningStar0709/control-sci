# Example 7.10 (Train)

The train described in Example 2.3 (Chapter 2) is to be accelerated from rest to 25 m/s over level terrain. The head locomotive is to track the desired velocity $v_{d}(t) = 25(1 - e^{-t/40})$ , within $\pm 2$ m/s if possible; the traction force is not to exceed 120 kN, and the spring and damper couple forces are limited to 75,000 N and 50,000 N, respectively. Set up and solve an appropriate LQ problem for a locomotive and four cars.

Solution First the system is linearized about the steady state. In the absence of friction and on horizontal terrain, Newton's second law implies a steady state where all velocities are 25 m/s and no forces act on the cars or the locomotive. The steady-state values $x_{2}, x_{3}, \ldots, x_{N}$ of the coupler lengths are all equal to the unstressed length, $x_{0}$ . The state variable $x_{1}$ is not used in this problem; it is the distance traveled by the locomotive, and it does not enter into the determination of forces and velocities.

Using the desired steady state as a reference, we define

$$\Delta x _ {i} = x _ {i} - x _ {0}, \quad i = 2, 3, 4, 5\Delta v _ {i} = v _ {i} - 2 5, \quad i = 1, 2, 3, 4, 5.$$

From Equations 2.26 and 2.27,

$$\Delta \dot {x} _ {i} = \Delta v _ {i - 1} - \Delta v _ {i}, \quad i = 2, 3, 4, 5\Delta \dot {v} _ {1} = - 1 2. 5 \Delta x _ {2} -. 7 5 \Delta v _ {1} +. 7 5 \Delta v _ {2} +. 0 0 5 F _ {1}\Delta \dot {v} _ {i} = 6 2. 5 \Delta x _ {i} - 6 2. 5 \Delta x _ {i + 1} + 3. 7 5 \Delta v _ {i - 1}, 7. 5 \Delta v _ {i} + 3. 7 5 \Delta v _ {i + 1}, \quad i = 2, 3, 4\Delta \dot {v} _ {5} = 6 2. 5 \Delta x _ {5} + 3. 7 5 \Delta v _ {4} - 3. 7 5 \Delta v _ {5}.$$

Here, $F_{1}$ is the locomotive traction force.

The velocity error of the locomotive is described by

$$v _ {1} - v _ {d} = 2 5 + \Delta v _ {1} - (2 5 - 2 5 e ^ {- t / 4 0})= \Delta v _ {1} + z$$

where $z = 25e^{-t / 40}$ satisfies

$$\dot {z} = - \frac {1}{4 0} z, \quad z (0) = 2 5.$$

To choose a performance index, we recall that

$$\text { coupler spring force } = K (x _ {i} - x _ {0}) = K \Delta x _ {i}\text { damper spring force } = D (v _ {i - 1} - v _ {i}) = D (\Delta v _ {i - 1} - \Delta v _ {i})$$

with $K = 2.5 \times 10^{6}$ N/m and $D = 1.5 \times 10^{5}$ N/m/s. We try an index where the forces and velocities are normalized to their desired maxima:
