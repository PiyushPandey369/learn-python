import numpy as np

# --- Array creation ---
a1 = np.arange(10)                       # 1D array
a2 = np.arange(12).reshape(3, 4)         # 2D array (3x4)
a3 = np.arange(27).reshape(3, 3, 3)      # 3D array (3x3x3)
a4 = np.arange(8).reshape(2, 2, 2)       # 3D array (2x2x2)


# --- 1D slicing & indexing ---
print("=== 1D Slicing ===")
print("Elements:", a1)

print("a1[2:5] →", a1[2:5])  # [2, 3, 4]


# --- 2D slicing & indexing ---
print("\n=== 2D Slicing ===")
print("Elements:\n", a2)

print("a2[1,2] →", a2[1, 2])        # 6
print("a2[2,3] →", a2[2, 3])        # 11
print("a2[1,1] →", a2[1, 1])        # 5
print("a2[1:,1:3] →\n", a2[1:, 1:3])  # [[5,6],[9,10]]
print("a2[::2,::3] →\n", a2[::2, ::3])  # [[0,3],[8,11]]
print("a2[::2,1::2] →\n", a2[::2, 1::2])  # [[1,3],[9,11]]
print("a2[1,::3] →", a2[1, ::3])    # [4,7]
print("a2[:2,1] →", a2[:2, 1])      # [1,5]


# --- 3D slicing with a4 ---
print("\n=== 3D Slicing (a4) ===")
print("Elements:\n", a4)

print("a4[1,0,1] →", a4[1, 0, 1])   # 5


# --- 3D slicing with a3 ---
print("\n=== 3D Slicing (a3) ===")
print("Elements:\n", a3)

print("a3[1,:,:] →\n", a3[1, :, :])          # 2nd matrix
print("a3[::2] →\n", a3[::2])                # 1st and last matrix
print("a3[0,1,:] →", a3[0, 1, :])            # [3,4,5]
print("a3[1,:,1] →", a3[1, :, 1])            # [10,13,16]
print("a3[2,1:,1:] →\n", a3[2, 1:, 1:])      # [[22,23],[25,26]]
print("a3[::2,0,::2] →\n", a3[::2, 0, ::2])  # [[0,2],[18,20]]
