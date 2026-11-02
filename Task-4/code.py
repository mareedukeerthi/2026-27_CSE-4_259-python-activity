


def compress_text(text):

    if not text:
        return ""

    encoded = ""
    count = 1

    
    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            count += 1

        else:
            encoded += text[i - 1]

            if count > 1:
                encoded += str(count)

            count = 1

    
    encoded += text[-1]

    if count > 1:
        encoded += str(count)

    return encoded



print("===== TEXT COMPRESSION USING CHARACTER RUNS =====")

original = input("Enter a string: ")

if not original:
    print("Error: Empty string is not allowed.")

else:

    
    compressed = compress_text(original)

    
    original_length = len(original)
    compressed_length = len(compressed)

    
    space_saved = original_length - compressed_length

    print("\n========== COMPRESSION RESULT ==========")

    print("Original String   :", original)
    print("Encoded String    :", compressed)

    print("Original Length   :", original_length)
    print("Encoded Length    :", compressed_length)

    print("Characters Saved  :", space_saved)

    
    if compressed_length < original_length:

        percentage = (
            space_saved / original_length
        ) * 100

        print("Compression Status: Beneficial")
        print("Space Saved       :", round(percentage, 2), "%")

    else:

        print("Compression Status: Not Beneficial")
        print("Space Saved       : 0%")

    print("========================================")

