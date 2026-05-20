# 11.5.2 Conversion by Computer

In python.control there is a built in function to convert transfer functions from continuous time to discrete time, control.sample\_system().

```python
import numpy as np
import control as ctl
s = ctl.TransferFunction.s
