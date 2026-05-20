# 7.2.2 Sample rate

Running a feedback controller at a faster update rate doesn’t always mean better control. In fact, you may be using more computational resources than you need. However, here are some reasons for running at a faster update rate.

Firstly, if you have a discrete model of the system, that model can more accurately approximate the underlying continuous system. Not all controllers use a model though.

Secondly, the controller can better handle fast system dynamics. If the system can move from its initial state to the desired one in under 250 ms, you obviously want to run the controller with a period less than 250 ms. When you reduce the sample period, you’re making the discrete controller more accurately reflect what the equivalent continuous controller would do (controllers built from analog circuit components like op-amps are continuous).

Running at a lower sample rate only causes problems if you don’t take into account the response time of your system. Some systems like heaters have outputs that change on the order of minutes. Running a control loop at 1 kHz doesn’t make sense for this because the plant input the controller computes won’t change much, if at all, in 1 ms.
