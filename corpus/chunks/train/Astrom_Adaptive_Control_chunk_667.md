# Parallel Estimators and Other Schemes

There are many other ways to deal with parameter tracking. One possibility is to have several parallel estimators with different forgetting factors and to choose the one in which the estimates have the smallest residuals. It is also possible to have several parallel estimators that are reset periodically in a staggered way. There are also other schemes in which the forgetting factor is made signal dependent.

![](image/2f8a328e9b75afc5981f19e51f31c80793aa171a0ec69779c641e94412801148.jpg)  
Figure 11.11 Tracking piecewise constant parameters using covariance re-setting.
