Parameter ``N``:
    numpy.array(states x inputs), cross weight matrix.

Returns:
    numpy.array(inputs x states), controller gain matrix.
    """
    P = sp.linalg.solve_discrete_are(a=A, b=B, q=Q, r=R, s=N)
    return np.linalg.solve(B.T @ P @ B + R, B.T @ P @ A + N.T) 
```  
Snippet B.2. Infinite horizon, discrete time LQR solver in Python

Other formulations of LQR for finite horizon and discrete time can be seen on Wikipedia.[1]

The course notes for MIT 6.832 Underactuated Robotics: Algorithms for Walking, Running, Swimming, Flying, and Manipulation by Russ Tedrake have a rigorous proof of the results shown above.[2]
