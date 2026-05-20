# Create system with two outputs for phase plot
C2 = np.array([[1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]) # This gives both X2 and Xdot2

sys2 = ctl.ss(A, B, C2, D)

if True:
    # Plot phase trajectory
    plt.figure(2)
    plt.plot(y1[2][0], y1[3][0])
    plt.grid(True)
    plt.xlabel('Position')
    plt.ylabel('Velocity')
    plt.title("Phase" Plot (x_3 vs x_3 dot)')
    #
    # # Convert to transfer functions
    # tf = ctl.ss2tf(sys)
    # # tf = tfs4x4
    # print("\nTransfer functions to each state var:")
    # print(tf)

plt.show() 
```

Listing 8.4. python.control 4x4 State Space setup for the Auto suspension system example with all 4 states as output.
