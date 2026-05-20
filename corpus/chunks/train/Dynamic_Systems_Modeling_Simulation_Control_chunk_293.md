# 6.3 BUILDING SIMULATIONS USING SIMULINK

MATLAB’s Simulink is an extremely useful and powerful software tool for simulating dynamic systems and obtaining the dynamic response. Universally accepted, it is used in both academic settings and the engineering industry. Simulink is a graphical tool based on block diagrams composed of individual I/O blocks. A working outline of Simulink and the basic steps for building a simulation are presented in this section; Appendix C presents a more complete Simulink tutorial.

A good numerical simulation tool successfully incorporates the following desirable traits:

1. Ease of entering the mathematical models that represent the system dynamics   
2. Ability to include standard and arbitrary inputs to the system   
3. Ease of storing and plotting the desired output variables   
4. Ability to include arbitrary initial conditions for the dynamic variables   
5. Ease of adjusting the run-time and numerical integration parameters

Simulink uses a graphical user interface (GUI) that allows the user to browse and select I/O blocks from several libraries, such as the Continuous and Math Operations libraries. The Continuous library includes block icons for standard models such as the transfer function, SSR, and the integrator block for
