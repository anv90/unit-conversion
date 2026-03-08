import requests
print("=" * 60)
print("Testing Unit Conversion Microservice")
print("=" * 60)

print("\nTest 1.0: Convert time (5 hrs)")
#add params
response = requests.get(f"http://localhost:6001/unit-conversion?num=5&unit=hr")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()
    print("Expected {'day': 0.20833333333333334, 'hr': 5.0, 'min': 300.0, 'sec': 18000.0}")
    print(f"Result: ${result}")
else:
    print(response.text)


print("\nTest 2.0: Convert some weight units")
#add params
response = requests.get(f"http://localhost:6001/unit-conversion?num=5&unit=lb")
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    result = response.json()

    expected = {
        "g": (5.0 * 453.592),
        "kg": ((5.0 * 453.592) * 0.001),
        "lb": (5.0),
        "mg": ((5.0 * 453.592) * 1000),
        "oz": (5 * 16),
        "tn_metric": ((5.0 * 453.592) * 0.000001),
        "tn_short": ((5.0 * 453.592) / 907185),
        }
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
else:
    print(response.text)
