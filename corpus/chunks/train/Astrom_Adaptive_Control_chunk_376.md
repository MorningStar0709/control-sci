# 6.1 INTRODUCTION

Some theoretical problems were discussed in earlier chapters in connection with description or derivation of specific algorithms. In particular we used equilibrium analysis to analyze the self-tuners and stability theory to derive some model-reference algorithms. In this chapter we attempt to bring together theory of a more general character. The theory has several different goals:

- To present some mathematical tools that are useful in analysis of adaptive systems.   
• To analyze the behavior of adaptive systems in nonideal cases.   
- To give ideas for new algorithms and for improvement of old algorithms.

In this chapter we focus on the first two issues. The behavior of specific algorithms can be understood through analysis of stability, convergence, and performance. Stability proofs require certain assumptions. It is also of considerable interest to understand what happens when the assumptions are violated. Analysis of performance may give useful insight into performance limits; it is helpful to know whether the performance of a particular algorithm is close to the theoretical limits. A good theory should also give clues to the construction of new algorithms.

Unfortunately, there is no collection of results that can be called a theory of adaptive control in the sense specified. There is instead a scattered body of results, which gives only partial results. One reason for this is that the behavior of adaptive systems is quite complex because of their time-varying and nonlinear character. Readers who are familiar only with linear systems theory, in which most problems can be answered in great detail, should thus be warned.

The closed-loop systems obtained with adaptive control are nonlinear and sometimes also stochastic. Such systems are also very difficult to analyze. To obtain some insight with a reasonable effort, it is therefore necessary to make some simplifications. It is often possible to analyze the equilibrium conditions. The local behavior in the neighborhood of the equilibria can also be explored by using linearization. The global behavior of the systems can, however, be very complex, particularly if the design parameters are chosen badly.
