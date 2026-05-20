# 10–2 POLE PLACEMENT

In this section we shall present a design method commonly called the pole-placement or pole-assignment technique. We assume that all state variables are measurable and are available for feedback. It will be shown that if the system considered is completely state controllable, then poles of the closed-loop system may be placed at any desired locations by means of state feedback through an appropriate state feedback gain matrix.

The present design technique begins with a determination of the desired closed-loop poles based on the transient-response and/or frequency-response requirements, such as speed, damping ratio, or bandwidth, as well as steady-state requirements.

Let us assume that we decide that the desired closed-loop poles are to be at $s = \mu _ { 1 }$ , $s = \mu _ { 2 } , \ldots , s = \mu _ { n }$ . By choosing an appropriate gain matrix for state feedback, it is possible to force the system to have closed-loop poles at the desired locations, provided that the original system is completely state controllable.

In this chapter we limit our discussions to single-input, single-output systems. That is, we assume the control signal $u ( t )$ and output signal $y ( t )$ to be scalars. In the derivation in this section we assume that the reference input $r ( t )$ is zero. [In Section 10–7 we discuss the case where the reference input $r ( t )$ is nonzero.]

In what follows we shall prove that a necessary and sufficient condition that the closed-loop poles can be placed at any arbitrary locations in the s plane is that the system be completely state controllable. Then we shall discuss methods for determining the required state feedback gain matrix.

It is noted that when the control signal is a vector quantity, the mathematical aspects of the pole-placement scheme become complicated. We shall not discuss such a case in this book. (When the control signal is a vector quantity, the state feedback gain matrix is not unique. It is possible to choose freely more than n parameters; that is, in addition to being able to place n closed-loop poles properly, we have the freedom to satisfy some or all of the other requirements, if any, of the closed-loop system.)
