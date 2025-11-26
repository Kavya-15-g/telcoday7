import yaml
with open(r"C:\Users\kg001\Downloads\TS24550_SS_SmDataSourceRegistration.yaml") as f:
     data = yaml.safe_load(f)

print(data)
def print_yaml(d, indent=0):
    space = " " * indent
    if isinstance(d, dict):
        for k, v in d.items():
            print(f"{space}{k}:")
            print_yaml(v, indent + 2)
    elif isinstance(d, list):
        for item in d:
            print_yaml(item, indent)
    else:
        print(f"{space}{d}")

print_yaml(data)

