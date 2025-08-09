import subprocess
import sys

# Run the function image directly
result = subprocess.run(
    ["docker", "run", "--rm", "my-function-image"],
    capture_output=True,
    text=True
)

print("Container output:", result.stdout.strip())
