# 5.7 Design of a Controller for the Double Integrator

In pole-placement design we are primarily choosing the polynomials $A_{c}$ and $A_{c}$ , whose zeros are the closed-loop poles, and the sampling period. To make proper choices it is important to understand how they influence response to command signals, load disturbances, measurement noise, and sensitivity to modeling errors. This is illustrated in this section where we consider control of a double-integrator plant. The design will be based on Algorithm 5.1.
