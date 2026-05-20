# Example 1.1 Time dependence in digital filtering

A digital filter is a simple example of a computer-controlled system. Suppose that we want to implement a compensator that is simply a first-order lag. Such a compensator can be implemented using A-D conversion, a digital computer, and D-A conversion. The first-order differential equation is approximated by a first-order difference equation. The step response of such a system is shown in Fig. 1.4. The figure clearly shows that the sampled system is not time-invariant because the response depends on the time when the step occurs. If the input is delayed, then the output is delayed by the same amount only if the delay is a multiple of the sampling period.

![](image/5d3796c5656d411eb8cf4e18d09edd43d0fa7e41b6cfbc39b802bf45e7231883.jpg)  
Figure 1.4 (a) Block diagram of a digital filter. (b) Step responses (dots) of a digital computer implementation of a first-order lag for different delays in the input step (dashed) compared with the first sampling instant. For comparison the response of the corresponding continuous-time system (solid) is also shown.

The phenomenon illustrated in Fig. 1.4 depends on the fact that the system is controlled by a clock (compare with Fig. 1.1). The response of the system to an external stimulus will then depend on how the external event is synchronized with the internal clock of the computer system.

Because sampling is often periodic, computer-controlled systems will often result in closed-loop systems that are linear periodic systems. The phenomenon shown in Fig. 1.4 is typical for such systems. Later we will illustrate other consequences of periodic sampling.
