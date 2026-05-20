# 6.5.5 Guidance Techniques

As discussed in Section 6.5.3, the function of a ballistic missile’s guidance system is to generate a sequence of command signals that will steer the vehicle and terminate its thrust in such a way that the intended mission is accomplished and all of the guidance constraints are satisfied. Once the guidance system has selected a course and calculated the initial conditions that will place the missile on this course, it is up to the flight control and propulsion systems to obtain these initial conditions with sufficient accuracy. Control errors arise through the inability of the guidance system to determine exactly when the desired position and velocity have been obtained, and to errors and dispersions in executing guidance commands. Ordinarily, the vehicle must rely solely on inertial information during the thrusting period, so that the error at cut-off is a function of the inertial system errors, cut-off control errors, and the position and velocity errors at the beginning of the thrust period. The total burnout error then propagates as a perturbation of the true path with respect to the trajectory computed in the missile, and may be evaluated at any point along the trajectory to the first order.

There are several guidance techniques of various degrees of difficulty available to the missile designer. Three of the more common types are [9]:

(1) explicit guidance,   
(2) implicit guidance, and   
(3) delta guidance.

These techniques are based, to some extent, on the correlated (or, required) velocity concept. These methods, as mentioned above, differ in the degree of complexity of the in-flight computations and the amount of preflight targeting or precomputation required.

Explicit Guidance: Explicit guidance is a generic term for the system of guidance equations that result from a direct solution of the equations of motion for the freeflight trajectory of a vehicle subject to specified boundary conditions. This boundary value problem may be considered a generalization of Lambert’s theorem, which as we have seen, expresses the relationship for the conic path passing through the radius vector $\mathbf { r } _ { o }$ at time $t _ { o }$ , and radius vector r at time t , for Keplerian elliptic motion.
