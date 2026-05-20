Configuration Parameters: Example_1/Configuration (Active)
Select:
Solver
Data Import/Export
Optimization
Diagnostics
Hardware Implementation
Model Referencing
Simulation Target
Simulation time
Start time: 0.0 Stop time: 4
Solver options
Type: Fixed-step Solver: ode4 (Runge-Kutta)
Fixed-step size (fundamental sample time): 0.01
Tasking and sample time options
Periodic sample time constraint: Unconstrained
Tasking mode for periodic sample times: Auto
Automatically handle rate transition for data transfer
Higher priority value indicates higher task priority
OK Cancel Help Apply
</details>

Figure C.4 Setting the numerical integration parameters (Example C.1).

The final step is to execute the simulation by clicking the Run simulation (or “play”) button. A plot of output y(t) can be created using MATLAB’s plot command:

>> plot(t,y)    % plot output vs. time
>> grid    % add grid lines to plot
>> xlabel('Time, s')    % add x-axis label
>> ylabel('Output, y')    % add y-axis label
