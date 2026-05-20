# 7.6 Optimal Control Systems with State Constraints

In the previous sections, we discussed the optimal control systems with control constraints. In this section, we address the optimal control systems with state constraints [79, 120].

Optimal control systems with state constraints (Constrained Optimal Control) has been of great interest to engineers. Some examples of state-constrained problems are the solution of the minimum time-to-climb problem for an aircraft that is required to start within a specified flight envelope, the determination of the best control policy for an industrial mechanical robot subject to path constraints, and the speed of an electric motor which cannot exceed a certain value without damaging some of the mechanical components such as bearings and shaft. There have been several methods proposed to handle state variable inequality constraints. In general, there are three methods for handling these systems $[49]$ :

1. slack variables,

2. penalty functions, and

3. interior-point constraints.

Let us first consider the penalty function method.
