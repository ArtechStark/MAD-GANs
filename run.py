import os

print("Train the model", flush=True)
os.system("python RGAN.py --settings_file kdd99")
print("do anomaly detection",flush=True)
os.system("python AD.py --settings_file kdd99_test")
print()
os.system("python AD_Invert.py --settings_file kdd99_test")
