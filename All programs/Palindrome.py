# Palindrome Generator
# List of common palindromes
'''

palindrome_list = [
    "racecar", "madam", "level", "radar", "civic", "kayak", 
    "noon", "deed", "rotor", "refer", "stats", "tenet",
    "malayalam", "mom", "dad", "pop", "eye", "bob", "nun",
    "wow", "sos", "pep", "tot", "gag", "mum", "sis"
]

print("=" * 50)
print("PALINDROME GENERATOR")
print("=" * 50)

word = input("\nEnter a word: ").lower().strip()

print("\n" + "-" * 50)
print("SEARCHING FOR SIMILAR PALINDROMES...")
print("-" * 50)

# Find similar palindromes
similar = []
for p in palindrome_list:
    # Check if word is substring of palindrome or shares letters
    if word in p or any(char in p for char in word):
        similar.append(p)

if similar:
    print(f"\n✓ Found {len(similar)} similar palindrome(s):")
    for s in similar[:5]:  # Show top 5
        print(f"  → {s}")
else:
    print("\n✗ No similar palindromes found in list.")

# Generate new palindromes
print("\n" + "-" * 50)
print("GENERATED PALINDROMES:")
print("-" * 50)

# Method 1: word + reverse
reversed_word = word[::-1]
option1 = word + reversed_word
print(f"\nOption 1: {word} + {reversed_word}")
print(f"  Result: {option1}")

# Method 2: reverse + word
option2 = reversed_word + word
print(f"\nOption 2: {reversed_word} + {word}")
print(f"  Result: {option2}")

# Verify they're palindromes
print("\n" + "-" * 50)
print("VERIFICATION:")
print("-" * 50)
print(f"'{option1}' is palindrome: {option1 == option1[::-1]}")
print(f"'{option2}' is palindrome: {option2 == option2[::-1]}")

print("\n" + "=" * 50)
print("Done!")
print("=" * 50)


'''


print("PALINDROME GENERATOR")
print("-" * 40)

word = input("\nEnter a word: ").lower().strip()

# Check if already a palindrome
reversed_word = word[::-1]

if word == reversed_word:
    print(f"\n'{word}' is a palindrome!")
else:
    print(f"\nGenerating palindromes from '{word}'...")
    
    # Method 1: word + reverse
    option1 = word + reversed_word
    print(f"\nOption 1: {word} + {reversed_word} = {option1}")
    
    # Method 2: reverse + word
    option2 = reversed_word + word
    print(f"Option 2: {reversed_word} + {word} = {option2}")

print("\nDone!")

