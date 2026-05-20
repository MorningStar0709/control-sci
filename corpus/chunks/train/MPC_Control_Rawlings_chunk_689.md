# 6.2.5 Tracking Nonzero Setpoints

For tracking nonzero setpoints, we compute steady-state targets as discussed in Section 1.5. The steady-state input-output model is given by

$$y _ {s} = G u _ {s} \quad G = C (I - A) ^ {- 1} B$$

in which G is the steady-state gain of the system. The two subsystems are denoted

$$
\left[ \begin{array}{c} y _ {1 s} \\ y _ {2 s} \end{array} \right] = \left[ \begin{array}{c c} G _ {1 1} & G _ {1 2} \\ G _ {2 1} & G _ {2 2} \end{array} \right] \left[ \begin{array}{c} u _ {1 s} \\ u _ {2 s} \end{array} \right]
$$

For simplicity, we assume that the targets are chosen to be the measurements $\left( H = I \right)$ . Further, we assume that both local systems are square, and that the local targets can be reached exactly with the local inputs. This assumption means that $G _ { 1 1 }$ and $G _ { 2 2 }$ are square matrices of full rank. We remove all of these assumptions when we treat the constrained two-player game in the next section. If there is model error, integrating disturbance models are required as discussed in Chapter 1. We discuss these later.

The target problem also can be solved with any of the four approaches discussed so far. We consider each.

Centralized case. The centralized problem gives in one shot both inputs required to meet both output setpoints

$$u _ {s} = G ^ {- 1} y _ {\mathrm{sp}}\mathcal {Y} _ {s} = \mathcal {Y} _ {\mathrm{sp}}$$

Decentralized case. The decentralized problem considers only the diagonal terms and computes the following steady inputs

$$
u _ {s} = \left[ \begin{array}{c c} G _ {1 1} ^ {- 1} & \\ & G _ {2 2} ^ {- 1} \end{array} \right] y _ {\mathrm{sp}}
$$

Notice these inputs produce offset in both output setpoints

$$
\mathcal {Y} _ {s} = \left[ \begin{array}{c c} I & G _ {1 2} G _ {2 2} ^ {- 1} \\ G _ {2 1} G _ {1 1} ^ {- 1} & I \end{array} \right] \mathcal {Y} _ {\mathrm{sp}}
$$

Noncooperative case. In the noncooperative game, each player attempts to remove offset in only its outputs. Player one solves the following problem

$$\min _ {u _ {1}} (y _ {1} - y _ {1 s p}) ^ {\prime} \overline {{Q}} _ {1} (y _ {1} - y _ {1 s p})\mathrm{s.t.} y _ {1} = G _ {1 1} u _ {1} + G _ {1 2} u _ {2}$$

Because the target can be reached exactly, the optimal solution is to find $u _ { 1 }$ such that $y _ { 1 } = y _ { 1 s p }$ , which gives

$$u _ {1 s} ^ {0} = G _ {1 1} ^ {- 1} \left(y _ {1 s p} - G _ {1 2} u _ {2} ^ {p}\right)$$

Player two solves the analogous problem. If we iterate on the two players’ solutions, we obtain
