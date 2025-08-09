import subprocess
import sys

# Run the function image directly
result = subprocess.run(
    ["docker", "run", "--rm", "my-function-image"],
    capture_output=True,
    text=True
)

print("Container output:", result.stdout.strip())

if "Hello from container function!" not in result.stdout:
    print("❌ Test failed")
    sys.exit(1)

print("✅ Test passed")