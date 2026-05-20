Let's see how well we're doing by plotting the step response:

Prompt 5 Could you add to your previous code to produce a step response for Gain = 0.512? Also, can you add lines indicating the percent overshoot (horizontal line) and the settling time spec (e.g. 2

Claude.ai generates additional code which produces:

![](image/4b9674ecda98fbbcaf6054731b4072ae36c3a7e934e1ec4d48855dbe89bf086a.jpg)

<details>
<summary>line</summary>

| Time (seconds) | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 1 | 15.0 |
| 8 | 15.0 |
| 14 | 15.0 |
</details>

Hmm.. not so great. But we could maybe take it from here ourselves!

```python
import numpy as np
import control as ctl
import matplotlib.pyplot as plt
s=ctl.TransferFunction.s
def cc(x):  # cleaner code
    return np.conj(x)
