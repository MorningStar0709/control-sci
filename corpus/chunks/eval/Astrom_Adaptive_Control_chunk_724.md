# PLC Implementations

Adaptive controllers can also be implemented in ordinary programmable logic controller (PLC) systems. Such solutions are used by manufacturing companies with competent in-house expertise. For example, 3M has implemented adaptive controllers in this way. The first installation was made in 1987. Currently, there are about 200 adaptive loops in operation. A wide range of processes are controlled. The systems are implemented on a variety of platforms such as General Electric, Modicon, Measurex, Square-D, and Reliance. Programming is done in Basic or C. The applications include standard loops for temperature, pressure, position, and humidity and more specialized loops associated with 3M proprietary processes. The adaptive algorithms that are used are based on estimation of parameters in models having the structure

$$A ^ {*} (q ^ {- 1}) y (t) = B _ {1} ^ {*} (q ^ {- 1}) u (t - d) + B _ {2} ^ {*} (q ^ {- 1}) v (t - d)$$

where v is a measurable disturbance. Polynomial $A^{*}$ has degree one or two, but polynomials $B_{1}^{*}$ and $B_{2}^{*}$ may have higher degree to cope with variable time delay. The parameters are estimated by a special gradient technique. The control design is a modified minimum-variance strategy.
