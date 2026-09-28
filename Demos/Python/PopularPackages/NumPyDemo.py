try:
    import numpy as np
except ModuleNotFoundError:
    raise SystemExit("NumPy is not installed. Install it with: python -m pip install numpy")

marks = np.array([75, 80, 90, 65, 85])

print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))