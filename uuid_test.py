import uuid

# Generate different types of UUIDs
uuid1 = uuid.uuid1()
uuid3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'example.com')
uuid4 = uuid.uuid4()
uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, 'example.com')

# Print the generated UUIDs
print(f"UUID1: {uuid1}")
print(f"UUID3: {uuid3}")
print(f"UUID4: {uuid4}")
print(f"UUID5: {uuid5}")

# Parse a UUID from a string
uuid_str = '12345678-1234-5678-1234-567812345678'
parsed_uuid = uuid.UUID(uuid_str)
print(f"Parsed UUID: {parsed_uuid}")

# Access properties of a UUID
u = uuid.uuid4()
print(f"UUID: {u}")
print(f"Hex: {u.hex}")
print(f"Int: {u.int}")
print(f"URN: {u.urn}")
print(f"Variant: {u.variant}")
print(f"Version: {u.version}")

