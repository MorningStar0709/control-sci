# Start and end at rest
problem.subject_to(X[:, 0] == np.array([[0.0], [0.0]])
problem.subject_to(X[:, N] == np.array([[r], [0.0]])
