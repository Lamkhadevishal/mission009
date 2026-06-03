# Resolved multiplication example

# Show both branch results and a final chosen value
num1_a = 8
num1_b = 9
num2 = 7
print(f"branch-A: {num1_a} * {num2} = {num1_a * num2}")
print(f"branch-B: {num1_b} * {num2} = {num1_b * num2}")

# Final chosen result (chose branch-A)
num1 = num1_a
result = num1 * num2
print(f"Resolved result: {num1} * {num2} = {result}  # resolved (chose branch-A)")
