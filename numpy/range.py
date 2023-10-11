import numpy as np

jumlah_kucing = np.array([3, 2, 1, 1, 7, 3, 2, 1, 0, 2])
range = jumlah_kucing.max() - jumlah_kucing.min()
print(range)

# Interquartile Range

iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print(iqr)
