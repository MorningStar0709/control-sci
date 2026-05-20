# 4.8 Combined MHE/Particle Filtering

We next propose a new state estimation method that combines some of the best elements of MHE and PF. This type of combination has several design parameters and can take different forms, and we use the general term combined MHE/PF to designate this entire class of state estimators. To motivate the design of MHE/PF, consider the strengths and weaknesses of pure MHE and pure PF. The main strengths of MHE are

1. MHE propagates the state using the full nonlinear model.   
2. MHE uses optimization to find the most likely estimate. Physical constraints can be included in the optimization.   
3. MHE employs a horizon of measurements.

Using the full nonlinear model prevents inaccurate model linearizations from interfering with the fitting of the model to the data. The use of optimization produces the best state or state trajectory to describe the current snapshot of data. Optimization methods generally evaluate a small set of points in the state space to find the best estimate compared to exhaustive enumeration, gridding, and sampling strategies. That becomes a significant strength as the dimension of the state space model increases past $n \approx 2 { - } 3$ . The use of a moving window of data provides some robustness to unmodeled disturbances entering the system. The goal in most recursive estimation is to consider measurements one at a time. That is often a valid goal, mainly because it allows faster computation of the current estimate given the current measurement. But unmodeled disturbances are often problematic when measurements are considered one at a time. No single measurement is sufficient to conclude that an unmodeled disturbance has shifted the state significantly from its current estimated value. Only when several sequential measurements are considered at once is the evidence sufficient to overturn the current state estimate and move the state a significant distance to better match all of the measurements. MHE has this capability built in.

The main weaknesses of MHE are

1. MHE may take significant computation time.   
2. MHE uses local instead of global optimization.
