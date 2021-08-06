import wikipedia as wp

try:
    a = wp.page("Wikipedia")
    print(a.images[0])
except:
    print("oops")
# print(a.images[0])

