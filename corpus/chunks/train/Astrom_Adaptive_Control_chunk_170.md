# Summary

The indirect self-tuning regulator based on model-following given by Algorithm 3.1 is a straightforward application of the idea of self-tuning. The adaptive controller has states that correspond to the parameter estimate $\varphi$ , the covariance matrix $P$ , the regression vector $\varphi$ , and the states required for the implementation of the control law. The controller in Example 3.4 has 20 state variables; updating of the covariance matrix $P$ alone requires ten states. The complete codes for the controllers in the examples are listed in the problems at the end of this chapter.

The algorithm can be generalized in many different ways by choosing other recursive estimation methods and other control design techniques. The idea is easy to apply. A detailed discussion of practical implementation is given in Chapter 11.
