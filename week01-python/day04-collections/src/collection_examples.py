"""Examples of Python collections used in data processing."""

dataset_names = [
    "customers",
    "orders",
    "products",
]

print(dataset_names)

print(dataset_names[0])
print(dataset_names[1])
print(dataset_names[-1])

dataset_names.append("payments")
dataset_names.insert(1, "employees")
dataset_names.remove("products")
removed_dataset = dataset_names.pop()

print(f"Removed: {removed_dataset}")

dataset_names[0] = "active_customers"

print(dataset_names)

# List length and membership
print(f"Dataset count: {len(dataset_names)}")

has_orders = "orders" in dataset_names
has_inventory = "inventory" in dataset_names

print(f"Contains orders: {has_orders}")
print(f"Contains inventory: {has_inventory}")

# The in operator is useful when checking required columns:
required_column = "customer_id"
columns = ["customer_id", "name", "email"]

if required_column in columns:
    print("Required column found")

# List slicing
row_counts = [100, 200, 300, 400, 500]

print(row_counts[0:3])
print(row_counts[:3])
print(row_counts[2:])
print(row_counts[::2])


# Sorting lists
file_sizes_mb = [25.5, 10.0, 42.7, 8.3]

file_sizes_mb.sort()
print(file_sizes_mb)

file_sizes_mb.sort(reverse=True)
print(file_sizes_mb)

# In production code, sorted() is often safer when the original order still matters.
original_counts = [500, 100, 300]
sorted_counts = sorted(original_counts)

print(original_counts)
print(sorted_counts)

# Tuples are immutable lists
database_connection = (
    "localhost",
    5432,
    "analytics",
)

host = database_connection[0]
port = database_connection[1]
database_name = database_connection[2]

print(host)
print(port)
print(database_name)


host, port, database_name = database_connection

print(f"Connecting to {database_name} on {host}:{port}")

# List versus tuple
# Use a list when values may change:
pipeline_steps = ["extract", "transform", "load"]

# Use a tuple when the structure should remain fixed:
database_location = ("localhost", 5432)

# Sets store unique values.
country_codes = [
    "SE",
    "NO",
    "SE",
    "DK",
    "NO",
    "FI",
]

unique_country_codes = set(country_codes)

print(unique_country_codes)
print(f"Unique countries: {len(unique_country_codes)}")

# Set operations
source_customer_ids = {101, 102, 103, 104}
target_customer_ids = {102, 103, 104, 105}

# Values in either set:
all_customer_ids = source_customer_ids | target_customer_ids
print(all_customer_ids)

# Values present in both:
matching_customer_ids = source_customer_ids & target_customer_ids
print(matching_customer_ids)

# Values present only in the source:
missing_from_target = source_customer_ids - target_customer_ids
print(missing_from_target)

# Values present in only one set:
different_customer_ids = source_customer_ids ^ target_customer_ids
print(different_customer_ids)


# Dictionaries store key-value pairs.
customer = {
    "customer_id": 101,
    "name": "Amina Hassan",
    "country": "Sweden",
    "is_active": True,
}

print(customer)

print(customer["name"])
print(customer["country"])

customer["is_active"] = False

customer["email"] = "amina@example.com"

removed_country = customer.pop("country")
print(f"Removed country: {removed_country}")

# Safe dictionary access
# print(customer["phone_number"]) -> KeyError
phone_number = customer.get("phone_number")
print(phone_number)

# Provide a default:
phone_number = customer.get(
    "phone_number", "Not provided"
)  # This is important when processing inconsistent JSON or API records.
print(phone_number)

# Dictionary methods
employee = {
    "employee_id": 501,
    "name": "Omar",
    "department": "Data",
}

print(employee.keys())
print(employee.values())
print(employee.items())

for key, value in employee.items():
    print(f"{key}: {value}")


# Nested collections
# Real data usually combines lists and dictionaries.
customers = [
    {
        "customer_id": 101,
        "name": "Amina",
        "country": "Sweden",
    },
    {
        "customer_id": 102,
        "name": "Yusuf",
        "country": "Norway",
    },
    {
        "customer_id": 103,
        "name": "Sara",
        "country": "Sweden",
    },
]

# Process every customer:
for customer_record in customers:
    print(f"{customer_record['customer_id']}: {customer_record['name']}")

# Filter Swedish customers:
for customer_record in customers:
    if customer_record["country"] == "Sweden":
        print(customer_record["name"])


# List comprehensions
# A list comprehension creates a list from another iterable.
# Traditional loop:
customer_names = []

for customer_record in customers:
    customer_names.append(customer_record["name"])

# List comprehension:
customer_names = [customer_record["name"] for customer_record in customers]

print(customer_names)

# With filtering:
swedish_customer_names = [
    customer_record["name"]
    for customer_record in customers
    if customer_record["country"] == "Sweden"
]

print(swedish_customer_names)


# Use comprehensions for simple transformations.
# valid_ids = [record["id"] for record in records if record["is_valid"]]
# Avoid placing complex business logic inside a comprehension. Use a normal loop or function when readability suffers.


# Dictionary comprehensions
customer_lookup = {
    customer_record["customer_id"]: customer_record["name"]
    for customer_record in customers
}

# Lookup tables provide fast access:
print(customer_lookup)
# This is often more efficient than repeatedly looping through all customers.
print(customer_lookup[102])
