# Control loop
for i in range(500):
    u = -K.dot(x)  # the control input is u* = -Kx
    x = model.step(u)  # propagate
    trajectory.append(x)
    controls.append(u) 
```

Position and velocity plots We use the following code for plotting:

```python
