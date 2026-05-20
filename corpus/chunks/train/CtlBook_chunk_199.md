# 7.2.2 Summary

Some key points about the Root Locus computation are

1. Closed loop poles are not the same as the poles of the individual $\operatorname { s y }$ stem blocks.   
2. Closed loop poles predict the time response of closed loop system.   
3. Closed loop poles predict the stability of the closed loop system.   
4. The controller introduces parameter K.   
5. The Root Locus diagram is a plot of how closed loop poles change with K.   
6. We usually consider $0 \le K \le \infty$   
7. python.control method: root\_locus\_plot(sys) .

```python
import control as ctl
import Matplotlib.Pyplot as plt
s=ctl.TransferFunction.s
K = 1
denom = ((s+1)*(s+2)*(s+3))
sys = ctl.TransferFunction(K/denom)
figRL = plt.Figure()
ax = plt.gca()
plt.title('Root Locus Diagram: Example 7.1')
ctl.root_locus_plot(sys, ax=ax)
plt.grid()
plt.show() 
```

Listing 7.1. Basic Python code for Root Locus (See Chapter 8).
