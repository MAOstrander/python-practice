big_list = list(range(1,50))
print big_list

everything_even = big_list[1::2]
print everything_even

words = "Thisisanexamplestringfulloflettersnospaces"
print words[::-1]

middle_chunk_backwards = big_list[30:10:-1]
print middle_chunk_backwards

def sillycase(thing):
    thing = thing.lower()
    middle = len(thing)/2
    middle = int(round(middle))
    last_half = thing[middle:].upper()
    return thing[:middle] + last_half

sillycase("testString")
