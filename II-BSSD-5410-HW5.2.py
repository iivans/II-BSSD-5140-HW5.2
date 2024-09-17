def calculate_percentage_of_original_in_class_code(original_file, modified_file):
    with open(original_file, 'r') as orig, open(modified_file, 'r') as mod:
        original_text = orig.read().strip()  # Read and strip whitespace
        modified_text = mod.read().strip()

    original_length = len(original_text)
    
    if original_length == 0:
        return 0.0  # If original file is empty, return 0%

    # Calculate how much of the original text is present in the modified text
    copied_length = len([char for char in original_text if char in modified_text])

    # Calculate the percentage of the original content that is found in the modified content
    percentage_copied = (copied_length / original_length) * 100

    return percentage_copied

# Compare LCSOriginal.txt to ClassCode.txt
lcs_copied_percentage = calculate_percentage_of_original_in_class_code('LCSOriginal.txt', 'ClassCode.txt')

# Compare EditDistanceOriginal.txt to ClassCode.txt
edit_distance_copied_percentage = calculate_percentage_of_original_in_class_code('EditDistanceOriginal.txt', 'ClassCode.txt')

# Print the percentage of original content found in the modified content
print(f"LCS code - Original Content Found: {lcs_copied_percentage:.2f}%")
print(f"Edit Distance code - Original Content Found: {edit_distance_copied_percentage:.2f}%")
