# 10–3 SOLVING POLE-PLACEMENT PROBLEMS WITH MATLAB

Pole-placement problems can be solved easily with MATLAB. MATLAB has two commands—acker and place—for the computation of feedback-gain matrix K. The command acker is based on Ackermann’s formula.This command applies to single-input systems only.The desired closed-loop poles can include multiple poles (poles located at the same place).

If the system involves multiple inputs, for a specified set of closed-loop poles the state-feedback gain matrix K is not unique and we have an additional freedom (or freedoms) to choose K. There are many approaches to constructively utilize this additional freedom (or freedoms) to determine K. One common use is to maximize the stability margin.The pole placement based on this approach is called the robust pole placement. The MATLAB command for the robust pole placement is place.

Although the command place can be used for both single-input and multiple-input systems, this command requires that the multiplicity of poles in the desired closed-loop poles be no greater than the rank of B. That is, if matrix B is an n\*1 matrix, the command place requires that there be no multiple poles in the set of desired closedloop poles.

For single-input systems, the commands acker and place yield the same K. (But for multiple-input systems, one must use the command place instead of acker.)

It is noted that when the single-input system is barely controllable, some computational problem may occur if the command acker is used. In such a case the use of the place command is preferred, provided that no multiple poles are involved in the desired set of closed-loop poles.

To use the command acker or place, we first enter the following matrices in the program:

where J matrix is the matrix consisting of the desired closed-loop poles such that

$$
\mathbf {J} = \left[ \begin{array}{c c c c} \mu_ {1} & \mu_ {2} & \ldots & \mu_ {n} \end{array} \right]
$$

Then we enter

$$K = \operatorname{acker} (A, B, J)$$

or

$$K = \text { place } (A, B, J)$$

It is noted that the command eig $( \mathsf { A } { - } \mathsf { B } ^ { { \ast } } \mathsf { K } )$ may be used to verify that K thus obtained gives the desired eigenvalues.

EXAMPLE 10–2 Consider the same system as treated in Example 10–1. The system equation is

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

where
