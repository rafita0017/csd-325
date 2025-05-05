import json

# load the json file
with open('student.json', 'r') as f:
    data = json.load(f)

print("Here's the original student list:\n")
for s in data:
    print(f"{s['lastName']}, {s['firstName']} : ID = {s['id']} , Email = {s['email']}")

print("\n(original list printed)\n")

# let's add myself
me = {
    "firstName": "Rafael",
    "lastName": "Garcia",
    "id": "99999",
    "email": "rafael.garcia@example.com"
}
data.append(me)

print("Added myself to the list.\n")
print("Here's the updated list:\n")
for s in data:
    print(f"{s['lastName']}, {s['firstName']} : ID = {s['id']} , Email = {s['email']}")

print("\n(updated list printed)\n")

# write back to the file
with open('student.json', 'w') as f:
    json.dump(data, f, indent=4)

print("student.json has been updated!")
