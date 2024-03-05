import json

with open(r'C:\Users\sanch\Downloads\sample-data.json') as f:
    json_data = json.load(f)

output = "Interface State\n"
output += "=" * 80 + "\n"
output += "{:<55} {:<10} {:<6}\n".format("Description", "Speed", "MTU")
output += "-" * 80 + "\n"

for item in json_data["imdata"]:
    interface = item["l1PhysIf"]["attributes"]
    description = interface["dn"]
    speed = interface.get("speed", "inherit")
    mtu = interface.get("mtu", "default")
    output += "{:<55} {:<10} {:<6}\n".format(description, speed, mtu)

print(output)
