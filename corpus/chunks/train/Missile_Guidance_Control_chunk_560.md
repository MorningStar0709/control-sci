Now it is possible to write an equation for the time of flight $t _ { f f }$ explicitly in terms of the geometry defined by $\mathbf { r } _ { v }$ and $\mathbf { r } _ { t }$ and in terms of one or more of the trajectory parameters. It is not, however, possible to obtain one of the trajectories as an explicit function of $t _ { f f }$ , and the geometry defined by $\mathbf { r } _ { v }$ and $\mathbf { r } _ { t }$ , due to the transcendental nature of the explicit function for $t _ { f f }$ . Thus, although the solution is unique, it is necessary to perform a numerical iteration to determine the trajectory parameters. Once the parameters are determined, the required velocity can be computed by the methods presented in the previous section. In this section, three possible iteration methods will be outlined. The following sections will consider some of the more detailed aspects of the iteration processes.

(5.1) Iteration on the Semimajor Axis (a) The time of flight can be given by the equations

$$
t _ {f f} = \left\{ \begin{array}{l l} (\sqrt {a ^ {3} / \mu}) [ 2 \pi - (\alpha - \sin \alpha) - (\beta - \sin \beta) ] & \text {if} t _ {f f} > t _ {f f (m)}, \\ (\sqrt {a ^ {3} / \mu}) [ (\alpha - \sin \alpha) - (\beta - \sin \beta) ], & \text {if} t _ {f f} \leq t _ {f f (m)}, \end{array} \right. \tag {29}
$$

where $t _ { f f ( m ) }$ , the required time for the minimum energy trajectory, is given by

$$t _ {f f (m)} = \left(\sqrt {a ^ {3} / \mu}\right) [ \pi - (\beta - \sin \beta) ], \tag {31}$$

where

$$\alpha = \pi ,a = s / 2,$$

and s, α, and $\beta$ in these equations are determined as functions of the parameter a and the geometry by (20), (22), and (23), respectively. The iteration procedure may then be outlined as follows

(1) A value of a is chosen and $t _ { f f }$ computed by (29) or (30).   
(2) The difference between the required time of flight $t _ { f f } = T - t _ { o }$ and that computed in (1) is used to compute a corrected value of $a$ .

(3) Step (1) is repeated using this new value of $^ { a . }$

(4) This procedure is repeated until a sufficiently small difference between the required time of flight and that computed is obtained.

The value of a obtained may then be used to compute the required velocity by the equations described in Sections (4.1.1) and (4.1.2). For the method described in Section (4.1.3) it will be necessary to first compute the parameter p, which is given as (see (6.30))

$$p = a (1 - e ^ {2}), \tag {32}$$

where $( 1 - e ^ { 2 } )$ may be computed from (18) or (19).
