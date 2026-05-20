# Practical Aspects

The design procedure given by Algorithm 5.3 is a solution to a general pole-placement design problem. The solution is specified in terms of the closed-loop characteristic equation with auxiliary constraints on the controller polynomials. Although the characteristic polynomial in principle can be chosen arbitrarily, it is necessary to choose it properly in order to obtain a controller that is not too sensitive to modeling errors. For a practical problem a variety of requirements must be expressed in terms of conditions on the characteristic equation. This is straightforward for systems of low order but it may be difficult for a system of high order. Real control-system design is typically an iterative procedure consisting of the steps:

1. Choose a characteristic polynomial and controller constraints $R_{d}$ and $S_{d}$ .   
2. Determine a controller using Algorithm 5.3.   
3. Evaluate the design.

The steps are repeated until a satisfactory result is obtained. Steps 2 and 3 are straightforward. The difficult step is to modify the characteristic polynomial and the controller constraints if the design is not satisfactory. Some detail of the procedure will be discussed in the following.
