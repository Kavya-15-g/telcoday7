import json

data = []
with open(r"C:\Users\kg001\OneDrive\Desktop\test5\my_python_env\Lib\site-packages\pip\_vendor\rich\json.py") as f:
    for line in f:
        line = line.strip()
        if line:
            data.append(json.loads(line))
print("First record =", data[0])
print("Keys =", data[0].keys())
print("skip_keys")
