import math

def wind_chill(t, v):
    return 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)

#input
t = float(input("Enter temperature (°F): "))
v = float(input("Enter wind speed (mph): "))

# Validating input
if abs(t) > 50 or v > 120 or v < 3:
    print("Invalid input: Temperature must be in [-50, 50] and wind speed in [3, 120].")
else:
    print(f"Wind Chill: {wind_chill(t, v):.2f}")
