Note that even though a matrix may be zero (such as the direct-link matrix D in this case) Simulink requires that all matrices be defined. The reader should carefully enter the matrices as Simulink will fail to run if all four matrices do not have the proper dimensions: A must be $n \times n .$ , B must be $n \times r , \mathbf { C }$ must be $m \times n ,$ , and D must be $m \times r$ (in this example, $n = 2 , r = 1$ , and $m = 1 )$ .

Simulink’s State-Space block has a dialog box for the initial state vector, $\mathbf { x } ( 0 )$ . In this example, the initial states are $x _ { 1 } ( 0 ) = y _ { 0 } = 0$ and $x _ { 2 } ( 0 ) = \dot { y } _ { 0 } = 0$ . Therefore, the initial state is entered as the $2 \times 1$ column vector $[ \begin{array} { l l l l } { } & { 0 } & { ; } & { 0 } \end{array} ]$ ]in the $\mathtt { I n i t i a l }$ conditions dialog box. The ability to include initial conditions for all states is a distinct advantage of using the state-space approach in Simulink.

The remaining steps for building the Simulink diagram (Step, Clock, and To Workspace blocks) are identical to the previous example, and Fig. 6.10 presents the Simulink diagram of the spool valve using the statespace approach. Note that Simulink does not display the numerical values of the SSR matrices; the user must open the dialog box to see the respective values. Executing the simulation and plotting the output y(t) (valve position) yields a plot identical to Fig. 6.9.

![](image/a2522cb2460b9966496d0c8e5c3741fb95322ac9175603e8d9c1bcb8f1fb97fc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Step force f(t)"] -->|f(t)| B["State-Space representation of spool-valve dynamics"]
    B -->|y| C["To Workspace"]
    D["Clock"] --> E["t"]
    E --> F["To Workspace1"]
```
</details>

Figure 6.10 Simulink diagram for Example 6.5: state-space approach.

A final note is in order: if we wanted to observe the position and velocity of the valve, we could do so with the state-space method by redefining the output vector as both state variables, that is, $\mathbf { y } = \mathbf { x } .$ . Therefore, the C matrix is the $2 \times 2$ identity matrix and the D matrix is a $2 \times 1$ null vector:

$$
\begin{array}{l} C = \left[ \begin{array}{l l l l} 1 & 0 & ; & 0 & 1 \end{array} \right] \\ D = \text { zeros } (2, 1) \\ \end{array}
$$

When we run the simulation, the output y sent to the MATLAB workspace will contain two columns. The first column is the valve’s position, and the second column is the valve’s velocity data for the simulation time. This example demonstrates another advantage of using the state-space method: we can obtain the dynamic responses of all states. The transfer-function method only provides the dynamic response of a single output variable, which is valve displacement in this example.
