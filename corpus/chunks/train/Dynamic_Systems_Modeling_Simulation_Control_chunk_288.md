The reader should note that the first three commands define the time vector t and the pulse input vector u. Of course, the object sys must be defined and the user may choose either a transfer function or SSR.

The built-in MATLAB commands step and impulse assume that the LTI system has zero initial conditions (of course, by definition systems represented by transfer functions have zero initial conditions). In many cases we want to simulate systems that have nonzero initial conditions (hence the system must be created as a state-space model). We may include initial conditions using the MATLAB commands lsim and initial. The lsim command is modified by adding the initial state vector x0 to the right-hand-side argument list:

$$> > [ y, t ] = \text { lsim(sys,u,t,x0) };$$

As before, the user must define the input vector u and simulation time vector t. Of course, the initial conditions x0 can be used only when the object sys is defined by an SSR.

The command initial simulates the response of an LTI system to its initial conditions (with zero input). If initial conditions exist, the user must define the system using a state-space model. The usage of initial is similar to the step, impulse, and lsim commands:

$$> > [ y, t ] = \text { initial(sys,x0,t) };$$

Again, it should be emphasized that the initial command cannot be used with transfer-function models as (by definition) transfer functions are derived by assuming zero initial conditions.

In summary, the built-in MATLAB commands allow a user to quickly obtain the system response to standard inputs (step for a unit-step and impulse for a unit-impulse input, respectively), arbitrary input functions (lsim), and arbitrary initial conditions (initial, for SSR models only). These commands can be used only for linear systems that can be represented by a transfer function or state-space model. The following examples illustrate the use of these built-in MATLAB commands.
