# 5–5 TRANSIENT-RESPONSE ANALYSIS WITH MATLAB

Introduction. The practical procedure for plotting time response curves of systems higher than second order is through computer simulation. In this section we present the computational approach to the transient-response analysis with MATLAB. In particular, we discuss step response, impulse response, ramp response, and responses to other simple inputs.

MATLAB Representation of Linear Systems. The transfer function of a system is represented by two arrays of numbers. Consider the system

$$\frac {C (s)}{R (s)} = \frac {2 s + 2 5}{s ^ {2} + 4 s + 2 5} \tag {5-35}$$

This system can be represented as two arrays, each containing the coefficients of the polynomials in decreasing powers of s as follows:

$$
\begin{array}{l} \mathrm{num} = [ 2 \quad 2 5 ] \\ \mathrm{den} = [ 1 \quad 4 \quad 2 5 ] \\ \end{array}
$$

An alternative representation is

$$
\begin{array}{l} \mathrm{num} = [ 0 2 2 5 ] \\ \mathrm{den} = [ 1 \quad 4 \quad 2 5 ] \\ \end{array}
$$

In this expression a zero is padded. Note that if zeros are padded, the dimensions of “num” vector and “den” vector become the same.An advantage of padding zeros is that the “num” vector and “den” vector can be directly added. For example,

$$
\begin{array}{l} \mathrm{num} + \mathrm{den} = [ 0 2 2 5 ] + [ 1 4 2 5 ] \\ = [ 1 \quad 6 \quad 5 0 ] \\ \end{array}
$$

If num and den (the numerator and denominator of the closed-loop transfer function) are known, commands such as

$$\text { step(num,den), } \quad \text { step(num,den,t) }$$

will generate plots of unit-step responses (t in the step command is the user-specified time.)

For a control system defined in a state-space form, where state matrix A, control matrix B, output matrix C, and direct transmission matrix D of state-space equations are known, the command

$$\operatorname{step} (A, B, C, D), \quad \operatorname{step} (A, B, C, D, t)$$

will generate plots of unit-step responses. When t is not explicitly included in the step commands, the time vector is automatically determined.

Note that the command step(sys) may be used to obtain the unit-step response of a system. First, define the system by

$$\mathrm{sys} = \mathrm{tf} (\mathrm{num}, \mathrm{den})$$

or

$$\mathrm{sys} = \mathrm{ss} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D})$$

Then, to obtain, for example, the unit-step response, enter

$$\operatorname{step} (\text { sys })$$

into the computer.
