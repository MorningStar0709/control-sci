MATLAB Program 2–3   
```matlab
A = [0 1 0; 0 0 1; -5 -25 -5];
B = [0; 25; -120];
C = [1 0 0];
D = [0];
[num,den] = ss2tf(A,B,C,D)
num =
    0 0.0000 25.0000 5.0000
den
    1.0000 5.0000 25.0000 5.0000
% **** The same result can be obtained by entering the following command: *****
[num,den] = ss2tf(A,B,C,D,1)
num =
    0 0.0000 25.0000 5.0000
den =
    1.0000 5.0000 25.0000 5.0000 
```

Nonlinear Systems. A system is nonlinear if the principle of superposition does not apply. Thus, for a nonlinear system the response to two inputs cannot be calculated by treating one input at a time and adding the results.

Although many physical relationships are often represented by linear equations, in most cases actual relationships are not quite linear. In fact, a careful study of physical systems reveals that even so-called “linear systems” are really linear only in limited operating ranges. In practice, many electromechanical systems, hydraulic systems, pneumatic systems, and so on, involve nonlinear relationships among the variables. For example, the output of a component may saturate for large input signals.There may be a dead space that affects small signals. (The dead space of a component is a small range of input variations to which the component is insensitive.) Square-law nonlinearity may occur in some components. For instance, dampers used in physical systems may be linear for low-velocity operations but may become nonlinear at high velocities, and the damping force may become proportional to the square of the operating velocity.

Linearization of Nonlinear Systems. In control engineering a normal operation of the system may be around an equilibrium point, and the signals may be considered small signals around the equilibrium. (It should be pointed out that there are many exceptions to such a case.) However, if the system operates around an equilibrium point and if the signals involved are small signals, then it is possible to approximate the nonlinear system by a linear system. Such a linear system is equivalent to the nonlinear system considered within a limited operating range. Such a linearized model (linear, time-invariant model) is very important in control engineering.
