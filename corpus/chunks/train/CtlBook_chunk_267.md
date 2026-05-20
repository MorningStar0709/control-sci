# we want to output all 4 states so
C is 4 rows x 4 cols
np.array([[1, 0, 0, 0],   # output all 4 states]
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]])

D = ColVector([0, 0, 0, 0]) 
```  
Listing 8.3. (continued on next page.)

```python
print('A: ', A.shape)
print('B: ', B.shape)
print('C: ', C.shape)
print('D: ', D.shape)
