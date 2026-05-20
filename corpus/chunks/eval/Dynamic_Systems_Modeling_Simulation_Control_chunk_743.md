# C.1 INTRODUCTION

Simulink is a numerical simulation tool that is part of the MATLAB software package developed by Math-Works. It uses a graphical user interface (GUI) to develop a block diagram representation of dynamic systems. The reader should keep in mind that Simulink is used to obtain the solution to dynamic systems comprised of linear and/or nonlinear ordinary differential equations (ODEs). Simulink performs this task by numerically integrating the ODEs that the user has defined by constructing a graphical block diagram representation of the system dynamics. The user develops the desired block diagram by selecting and connecting various inputoutput (I/O) blocks such as transfer functions, integrators, and gains. Simulink provides the user with a GUI that contains a wide array of I/O blocks.

We can summarize the basic steps for using Simulink to obtain the system response:

1. Select the appropriate I/O blocks needed to represent the system dynamics (e.g., I/O blocks for transfer functions, state-space representations (SSRs), and integrators)   
2. Select the appropriate blocks to represent the input function(s) (e.g., step, pulse, sinusoid).   
3. Store the desired system output variables for plots or later analysis.   
4. Select the numerical simulation parameters (e.g., run time, numerical integration method, integration step size).   
5. Execute the Simulink model to obtain the system response.
