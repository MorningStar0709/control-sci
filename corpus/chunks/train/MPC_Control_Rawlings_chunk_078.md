This controller corresponds to an infinite horizon control law. Notice that it is stabilizing and has a reasonable stability margin. Nominal stability is a guaranteed property of infinite horizon controllers as we prove in the next section.

With this motivation, we are led to consider directly the infinite horizon case

$$V (x (0), \mathbf {u}) = \frac {1}{2} \sum_ {k = 0} ^ {\infty} x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) \tag {1.16}$$

in which $x ( k )$ is the solution at time k of $x ^ { + } = A x + B u$ if the initial state is $x ( 0 )$ and the input sequence is u. If we are interested in a continuous process (i.e., no final time), then the natural cost function is an infinite horizon cost. If we were truly interested in a batch process (i.e., the process does stop at $k = N )$ , then stability is not a relevant property, and we naturally would use the finite horizon LQ controller and the time-varying controller, $u ( k ) = K ( k ) x ( k ) , k = 0 , 1 , \ldots , N .$ .

In considering the infinite horizon problem, we first restrict attention to systems for which there exist input sequences that give bounded cost. Consider the case A = I and B = 0, for example. Regardless of the choice of input sequence, (1.16) is unbounded for $x ( 0 ) \neq 0$ . It seems clear that we are not going to stabilize an unstable system $\left( A = I \right)$ without any input $\left( B = 0 \right)$ . This is an example of an uncontrollable system. In order to state the sharpest results on stabilization, we require the concepts of controllability, stabilizability, observability, and detectability. We shall define these concepts subsequently.
