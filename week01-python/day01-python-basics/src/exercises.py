"""Day 1 exercises covering types, conversions, and operators."""

record_count_text = "125"
record_count = int(record_count_text)

temperature_celsius = 21.8
rounded_temperature = int(temperature_celsius)

employee_count = 50
employee_count_decimal = float(employee_count)

print(record_count)
print(rounded_temperature)
print(employee_count_decimal)


first_value = 10
second_value = 3

print(first_value + second_value)
print(first_value - second_value)
print(first_value * second_value)
print(first_value / second_value)
print(first_value // second_value)
print(first_value % second_value)
print(first_value**second_value)


source_record_count = 1_000
target_record_count = 995

print(source_record_count == target_record_count)
print(source_record_count != target_record_count)
print(source_record_count > target_record_count)
print(source_record_count >= target_record_count)

file_exists = True
schema_is_valid = True
row_count_is_valid = False

can_process_file = file_exists and schema_is_valid
has_validation_problem = not row_count_is_valid
can_continue = can_process_file and row_count_is_valid

print(f"Can process file: {can_process_file}")
print(f"Has validation problem: {has_validation_problem}")
print(f"Can continue: {can_continue}")

dataset_name = "customer_data"
number_of_rows = 1_000
file_size_mb = 25.5
dataset_is_valid = True
description = None

print(dataset_name)
print(number_of_rows)
print(file_size_mb)
print(dataset_is_valid)
print(description)

print(type(dataset_name))
print(type(number_of_rows))
print(type(file_size_mb))
print(type(dataset_is_valid))
print(type(description))


row_count_text = "2500"
row_count = int(row_count_text)
print(row_count + 500)

successful_records = 950
failed_records = 50
total_records = successful_records + failed_records
print(f"Total records: {total_records}")
success_rate = successful_records / total_records * 100
print(f"Success rate: {success_rate}%")
print(f"Success rate is at least 95%: {success_rate >= 95}")

file_exists = True
file_is_empty = False
schema_is_valid = True

ready_for_processing = file_exists and not file_is_empty and schema_is_valid
print(f"Ready for processing: {ready_for_processing}")

total_rows = 10_000
invalid_rows = 125

print(f"Valid row count: {total_rows - invalid_rows}")
print(f"Invalid row percentage: {invalid_rows / total_rows * 100}")
print(f"Dataset is valid: {invalid_rows < 0.02 * total_rows}")
