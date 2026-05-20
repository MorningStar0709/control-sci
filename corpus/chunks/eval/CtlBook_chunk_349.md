# 10.1 Problem Statement and Learning Objectives

The problem of this chapter is to nd a good set of PID control parameters $( K _ { P } , K _ { I } , K _ { D } )$ by searching the 3D space created by those values. A key aspect of this search is careful denition of good. We will focus on the following aspects of performance when the system has a step input. with

 $T _ { S }$ (settling time)   
 %OS (percent overshoot)   
 SSE (Steady State Error)   
 $C u _ { m a x } ,$ the amount of eort applied by the controller to the plant (related to energy consumption).

In each case we will nd the controller which achieves response closest to the desired value. We will introduce and use a set of python routines which simply search a 3D space by nested iteration.

Upon completing this chapter, the successful student will be able to:

 Take an initial rough design of PID parameters, and, using a specic computational tool, rene it to achieve one or more performance specications without simplifying assumptions.   
 Manage the trade-o between accuracy and computation time to get results in an ecient manner.
