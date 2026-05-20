# B.4 CONSTRUCTING BASIC M-FILES

We have seen through the previous simple examples that MATLAB is a command-driven computing tool. In many cases, we can assemble the desired single-line commands to create an algorithm or program called an M-file. When we run an M-file, these commands are executed sequentially as if we separately typed each command in the MATLAB environment.

We can create a new M-file (a blank template) by clicking on the “blank page” icon beneath the File menu in the upper left corner of the MATLAB window. When the new template is opened, the user can begin typing MATLAB commands on each line (as well as comment lines preceded by the % character). MATLAB M-file B.1 is a program that computes the function $y ( x ) = 2 . 5 x ^ { 2 } - \tan { 1 . 2 x }$ for the independent variable −1 ≤ $x \leq 1$ and plots y(x). This M-file (called Ex1.m) illustrates the use of a for loop to iterate through multiple calculations. Note that we could have condensed the algorithm into a few simple command lines but instead we choose to show how to program an algorithm as an M-file. The algorithm (or script) Ex1.m begins with comment lines that document the M-file name and purpose. Next, the starting and final values of independent variable x are defined as well as the incremental step dx for 500 data points (= Npts). The for loop repeats all of the command lines between the for and end statements 500 times (the index integer begins at i=1 and ends at i=500). After the loop is repeated the results are plotted using the plot command.

In this textbook, a user might construct a specialized M-file to perform the following tasks: (1) set the numerical values for the system parameters (such as mass, stiffness, friction, capacitance, etc.), (2) define the system objects (such as transfer functions or state-space representations), (3) obtain the system response by executing a numerical simulation tool, or (4) plot the system response(s). Simulink models could be executed to obtain the system response by using the sim command in an M-file:

sim model\_name

where the Simulink model is model\_name.mdl. Constructing Simulink models is explained in Appendix C. If the mathematical model is a linear, time-invariant (LTI) system, then the user might use built-in MATLAB commands such as step, impulse, or lsim to obtain the system response. These built-in commands for linear system analysis are described in the next section.

MATLAB M-file B.1   
```matlab
%
% Example M-file Ex1.m
%
% This M-file computes the function y(x) = 2.5*x^2 - tan(1.2x)
% for the range -1 <= x <= 1. The function y(x) is plotted vs. x

% Define start x, final x, and step size dx
x_start = -1;
x_end = 1;
Npts = 500;
dx = (x_end - x_start)/(Npts - 1); % compute increment for x
x_now = x_start; % starting value for x
% FOR loop for x
for i=1:Npts
    y(i) = 2.5*x_now^2 - tan(1.2*x_now);
    x(i) = x_now; % store current x
    x_now = x_now + dx; % increment x_now by dx
end
% Plot y(x)
plot(x,y)
title('y vs. x')
xlabel('x')
ylabel('y(x)')
grid 
```
