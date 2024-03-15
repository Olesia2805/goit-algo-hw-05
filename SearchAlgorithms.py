import timeit

def read_file(file_path):
    with open(file_path, 'r', encoding = 'cp1251') as file:
        return file.read()

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


def build_shift_table(pattern):
    
    table = {}
    length = len(pattern)
    
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
   
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):

    shift_table = build_shift_table(pattern)
    i = 0 

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


def polynomial_hash(s, base=256, modulus=101):

    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):

    substring_length = len(substring)
    main_string_length = len(main_string)
    
    base = 256 
    modulus = 101  

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def search_times(text, pattern):
    result_kmp = []
    result_bm = []
    result_rk = []

    position_kmp = timeit.timeit(lambda: kmp_search(text, pattern), number = 1)
    position_bm = timeit.timeit(lambda: boyer_moore_search(text, pattern), number = 1)
    position_rk = timeit.timeit(lambda: rabin_karp_search(text, pattern), number = 1)

    result_kmp.append(position_kmp)
    result_bm.append(position_bm)
    result_rk.append(position_rk)

    return result_bm, result_kmp, result_rk

text1 = read_file("article1.txt")
text2 = read_file("article2.txt")

exists1 = "public static int binarySearch"
noexists1 = "Strawberry is my favorite fruit"

exists2 = "A comparison of current graph"
noexists2 = "Also, I love black tea"

sorting_exists1 = search_times(text1, exists1)
sorting_noexists1 = search_times(text1, noexists1)
sorting_exists2 = search_times(text2, exists2)
sorting_noexists2 = search_times(text2, noexists2)

print (f"|{'Substring':<40} | {'Boyer–Moore':<20} | {'Knuth–Morris–Pratt':<20} | {'Rabin-Karp':<20} |")
print (f"|{'-'*40} | {'-'*20} | {'-'*20} | {'-'*20} |")
print(f"|{f'{exists1}':<40} | {sorting_exists1[0][0]:20.5f} | {sorting_exists1[1][0]:20.5f} | {sorting_exists1[2][0]:20.5f} |")
print(f"|{f'{noexists1}':<40} | {sorting_noexists1[0][0]:20.5f} | {sorting_noexists1[1][0]:20.5f} | {sorting_noexists1[2][0]:20.5f} |")
print(f"|{f'{exists2}':<40} | {sorting_exists2[0][0]:20.5f} | {sorting_exists2[1][0]:20.5f} | {sorting_exists2[2][0]:20.5f} |")
print(f"|{f'{noexists2}':<40} | {sorting_noexists2[0][0]:20.5f} | {sorting_noexists2[1][0]:20.5f} | {sorting_noexists2[2][0]:20.5f} |")