def reset(self, x_initial = [1, 0, 0, 0], random=False):
    # We can also simulate a disturbance from a random distribution
    if random == True: 
```

```python
self.state = np.random.uniform(-0.1, 0.1, size=4)
else:
    self.state = x_initial
return np.array(self.state, dtype='float64').reshape(4,1) 
```

We can now start the simulation. We set up the model and set as initial state:

$$
x _ {0} = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \\ 0 \end{array} \right] \tag {391}
$$

The optimal control input is calculated at each time instant as

$$u ^ {*} (t) = - K x (t) \tag {392}$$

We simulate 10 seconds with the following Python code:

```python
