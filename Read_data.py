import wfdb
import numpy as np
import matplotlib.pyplot as plt

data_path = r"D:\School\Research\Heart\bidmc-congestive-heart-failure-database-1.0.0"

profile_name = "chf01"
rec = wfdb.rdann(f"{data_path}/{profile_name}", "ecg")

rr = np.diff(rec.sample) / rec.fs


plt.figure(figsize=(12,5))
plt.plot(rr[:1000])

plt.title(f"{profile_name}")
plt.xlabel("Beat Number")
plt.ylabel("Time Interval (Seconds)")

plt.show()
