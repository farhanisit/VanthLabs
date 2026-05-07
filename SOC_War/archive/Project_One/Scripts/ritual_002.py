# ~/VanthLabs/Project_One/Scripts/Python/ritual_002.py

name = input("Seeker, what is your name? ")
age = input("How old are you? ")

# Convert age to int
try:
    age = int(age)
    days_lived = age * 365
    print(f"\n🧮 {name}, you have lived approximately {days_lived} days on this Earth.")
except ValueError:
    print("\n⚠️ Invalid age input. Age must be a number.")
    exit()

# Ask about boolean purpose
willing = input("Are you willing to walk the Python path? (yes/no): ").lower()
is_ready = willing == "yes"

print(f"🔥 Ready to grind? {is_ready}")
print(f"📜 Data types of your inputs:")
print(f"- Name: {type(name)}")
print(f"- Age: {type(age)}")
print(f"- is_ready: {type(is_ready)}")

