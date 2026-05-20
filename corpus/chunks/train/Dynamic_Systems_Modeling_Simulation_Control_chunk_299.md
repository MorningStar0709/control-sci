# 6.4 SIMULATING LINEAR SYSTEMS USING SIMULINK

In this section, we present three different methods for simulating a linear system with Simulink. These three methods are

1. Transfer functions   
2. State-space representation   
3. Integrator blocks for each state-variable equation

Clearly, we may use transfer functions or an SSR only if the mathematical model consists of linear ODEs. Example 6.3 demonstrated the transfer-function approach to simulating a simple first-order electrical system. The third method, integrating each state-variable equation using an integrator block, can be applied to both linear and nonlinear mathematical models. All three methods have their advantages and drawbacks, as we demonstrate and discuss in this section by presenting the multiple simulation approaches applied to a common linear dynamic system.
