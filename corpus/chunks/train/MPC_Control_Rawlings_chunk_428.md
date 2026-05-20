The limitations of nominal MPC when uncertainty is present motivated the introduction of feedback, or closed-loop, MPC in which the decision variable is a policy, i.e., a sequence of control laws, rather than a sequence of control actions (Mayne, 1995;
Kothare, Balakrishnan, and Morari, 1996;
Mayne, 1997;
Lee and Yu, 1997;
Scokaert and Mayne, 1998).
With this formulation, the implicit MPC control law can be the same as the receding horizon control law obtained by DP.
See Section 3.3.4 and papers such as Magni, De Nicolao, Scattolini, and Allg¨ower (2003), where a $H _ { \infty }$ MPC control law is obtained.
But such results are conceptual because the decision variable is infinite dimensional.
Hence practical controllers employ suboptimal policies that are finitely parameterized, an extreme example being nominal MPC.
To avoid constraint violation, suboptimal MPC often requires tightening of the constraints in the optimal control problem solved online (Michalska and Mayne, 1993;
Chisci, Rossiter, and Zappa, 2001;
Mayne and Langson, 2001).
Of particular interest is the demonstration in Lim´on Marruedo, Alamo, and Camacho (2002) that using a sequence ´ of nested constraint sets yields input-to-state stability of nominal MPC if the disturbance is sufficiently small.
This procedure was extended in Grimm, Messina, Tuna, and Teel (2007), who do not require the value function to be continuous and do not require the terminal cost to be a control-Lyapunov function.
The robust suboptimal controllers discussed in this chapter employ the concept of tubes introduced in the pioneering papers by Bertsekas and Rhodes (1971a,b), and developed for continuous time systems by Aubin (1991) and Khurzhanski and Valyi (1997) and, for linear systems, use a control parameterization proposed by Rossiter, Kouvaritakis, and Rice (1998).
Robust positive invariant sets are employed to construct tubes as shown in (Chisci et al., 2001) and (Mayne and Langson, 2001).
Useful references are the surveys by Blanchini (1999) and Kolmanovsky and Gilbert (1995), as well as the recent book by Blanchini and Miani (2008).
Kolmanovsky and Gilbert (1995) provide an extensive coverage of the theory and computation of minimal and maximal robust (disturbance) invariant sets.
