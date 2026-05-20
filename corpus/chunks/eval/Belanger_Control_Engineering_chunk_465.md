b. With $\theta_{2}$ , i, and $\omega_{2}$ as outputs, design a reduced-order observer of order 2. The observer gain matrix should be chosen so that the error system has eigenvalues at $-10 \pm j10$ . (Note: Infinitely many gain matrices can do this.)   
c. Simulate the system and the two observers, with $v = 2 \mathrm{~V}$ (a constant), $\omega_{2}(0) = 5 \mathrm{rad/s}$ , and all other initial state and observer variables equal to zero.

![](image/a356d4f6cde632e9867153e051ae8867aaaf6fea1639ff2ec870103e213974fc.jpg)

7.52 Crane The crane model of Problem 2.11 (Chapter 2) was linearized in Problem 2.17. Using the linearized model:

a. Design a reduced-order observer (of order 3) with x as the measured output. The eigenvalues of the error system should be -10 and $-10 \pm j10$ .   
b. Design a reduced-order observer (of order 2) with x and $\theta$ as measured outputs. The eigenvalues of the error system should be $-10 \pm j10$ . (This is achievable with infinitely many observer gains.)   
c. With $F = 0$ , $\theta(0) = 0.5$ rad, and all other system and observer state variables equal to zero, simulate the linearized system with both observers.

![](image/4f2d41cdc62d3e955a0b8d13234ecec86f81bf27ce3efe926407d7469c38c9ee.jpg)

7.53 High-wire artist For the linearized system of Problem 2.18, with $\theta$ and $\phi$ as outputs, design a reduced-order observer (of order 2) to estimate the two angular velocities. The error system eigenvalues should be at $-20 \pm j20$ .

![](image/7dbd839eb4f21f6bc1f01ff9974b91d509f2eb674a9ffeb463b1b928f267c6ca.jpg)

7.54 Two-pendula problem In Problem 2.19 (Chapter 2), a linearized model was derived for a system with two pendula. (Assume $\ell_1 = 1\mathrm{m}$ and $\ell_2 = 0.5\mathrm{m}$ .) We wish to use optimal observer theory to design a reduced-order observer with $\theta_{1}, \theta_{2}$ , and $x$ as measurements.

Assume W = I and $V = v_{0}^{2}I$ . Design a few third-order observers for $\omega_{1}$ , $\omega_{2}$ , and v, and adjust $v_{0}$ so that each of the three eigenvalues has a real part less than -2. Calculate (approximately) the value of $v_{0}$ that just achieves this.

![](image/883799b3f809bbbb486a14fc0651d7e79b7ecf0aae5bd1f76fa3f76ff0d92a19.jpg)

7.55 Maglev
