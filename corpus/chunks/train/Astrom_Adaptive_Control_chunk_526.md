# Summary

There are many ways to make suboptimal dual controllers. Most of the approximations that are discussed start with the cautious controller and try to introduce some active learning. This can be done by including a term in the loss function that reflects the quality of the estimates. This term should also be a function of the control signal that is going to be determined. The suboptimal controllers should also be such that they can be used for higher-order systems without too much computation.
