# 4.1 Introduction

We now turn to the general problem of estimating the state of a noisy dynamic system given noisy measurements. We assume that the system generating the measurements is given by

$$x ^ {+} = f (x, w)y = h (x) + v \tag {4.1}$$

in which the process disturbance, w, measurement disturbance, v, and system initial state, $x ( 0 )$ , are independent random variables with stationary probability densities. One of our main purposes is to provide a state estimate to the MPC regulator as part of a feedback control system, in which case the model changes to $x ^ { + } = f ( x , u , w )$ with both process disturbance w and control input u. But state estimation is a general technique that is often used in monitoring applications without any feedback control. In Chapter 5, we discuss the combined use of state estimation with MPC regulation. In this chapter we consider state estimation as an independent subject. For notational convenience, we often neglect the control input u as part of the system model in this chapter.
