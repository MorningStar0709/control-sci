# 8–4 DESIGN OF PID CONTROLLERS WITH COMPUTATIONAL OPTIMIZATION APPROACH

In this section we shall explore how to obtain an optimal set (or optimal sets) of parameter values of PID controllers to satisfy the transient response specifications by use of MATLAB.We shall present two examples to illustrate the approach in this section.

EXAMPLE 8–2 Consider the PID-controlled system shown in Figure 8–19. The PID controller is given by

$$G _ {c} (s) = K \frac {(s + a) ^ {2}}{s}$$

It is desired to find a combination of K and a such that the closed-loop system will have 10% (or less) maximum overshoot in the unit-step response. (We will not include any other condition in this problem. But other conditions can easily be included, such as that the settling time be less than a specified value. See, for example, Example 8–3.)

There may be more than one set of parameters that satisfy the specifications. In this example, we shall obtain all sets of parameters that satisfy the given specifications.

To solve this problem with MATLAB, we first specify the region to search for appropriate K and a.We then write a MATLAB program that, in the unit-step response, will find a combination of K and a which will satisfy the criterion that the maximum overshoot is 10% or less.

Note that the gain K should not be too large, so as to avoid the possibility that the system require an unnecessarily large power unit.

Assume that the region to search for K and a is

$$2 \leq K \leq 3 \quad \text { and } \quad 0. 5 \leq a \leq 1. 5$$

If a solution does not exist in this region, then we need to expand it. In some problems, however, there is no solution, no matter what the search region might be.

In the computational approach, we need to determine the step size for each of K and a. In the actual design process, we need to choose step sizes small enough. However, in this example, to avoid an overly large number of computations, we choose the step sizes to be reasonable—say, 0.2 for both K and a.
