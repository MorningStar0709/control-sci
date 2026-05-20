# 10.5 CLOSED-LOOP STABILITY

Stability is an essential attribute of a closed-loop control system. We expect that a stable closed-loop system remains “under control” during all normal modes of operation. For example, operating a stable closed-loop cruise-control system will never result in an automobile speed that diverges from the desired reference speed and ultimately becomes unbounded in time. A stable cruise-control system will produce an automobile speed that remains bounded over time. The closed-loop speed response may or may not exhibit good damping characteristics or ultimately match the desired reference speed, but as long as the speed response does not become unbounded or “blow up” the system is said to be stable.

We use the bounded-input, bounded-output (BIBO) definition of stability: a system is BIBO stable if for every bounded input the output remains bounded for all time. The reader should note that BIBO stability does not impose any specific performance criteria on the system response and hence a stable system can have very poor transient and/or steady-state responses. All that is required for BIBO stability is that the system response does not diverge to infinity when the reference input is a bounded function. For linear, time-invariant (LTI) systems, BIBO stability requires that all characteristic roots (or poles or eigenvalues) lie in the left-half of the complex plane. The reader may want to review Sections 7.3 and 7.4 (first- and second-order system response) to solidify his or her understanding of how root locations in the complex plane correspond to the system response (in particular, see Figs. 7.13–7.16). As a quick example, consider the transfer function of an LTI system

$$G _ {P} (s) = \frac {1}{0 . 5 s ^ {3} + 4 s ^ {2} + 2 3 s + 3 4} = \frac {Y (s)}{U (s)} \tag {10.35}$$

This transfer function could represent the input-output relationship of an open-loop system (plant). The characteristic roots (or poles) are determined by setting the denominator of $G _ { P } ( s )$ to zero:

$$\text { Characteristic roots: } \quad 0. 5 s ^ {3} + 4 s ^ {2} + 2 3 s + 3 4 = 0$$

The three roots are $s _ { 1 } = - 2$ and $s _ { 2 , 3 } = - 3 \pm j 5$ . Because all three roots have negative real parts, they lie in the left-half of the complex plane. For this example the homogeneous or free response has the general form

$$y _ {H} (t) = c _ {1} e ^ {- 2 t} + e ^ {- 3 t} [ c _ {2} \cos 5 t + c _ {3} \sin 5 t ]$$
