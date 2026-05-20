# Kinematics constraint assuming constant acceleration between timesteps
for k in range(N):
    p_k1 = X[0, k + 1]
    v_k1 = X[1, k + 1]
    p_k = X[0, k]
    v_k = X[1, k]
    a_k = U[0, k]

problem.subject_to(p_k1 == p_k + v_k * dt + 0.5 * a_k * dt**2)
problem.subject_to(v_k1 == v_k + a_k * dt) 
```

Next, we’ll apply the state and input constraints.

```python
