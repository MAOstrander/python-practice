print "assign with parenthesis"
a = (1,2,3,4)
print a

print "assign without parenthesis"
b = 5,6,7,8
print b

print "tuples to tuples"
(c,d) = a,b
print c
print d

print "tuples containing multiple tuples"
e = c,d
print e

print "Swapping assignments"
f, g = b, a
print f
print g
f,g = g,f
print f
print g

print "Returning 'multiple things' using the powers of tuples"
def stringer(test_string):
  up = test_string.upper()
  down = test_string.lower()
  titled = test_string.title()
  rever = test_string[::-1]
  return up,down,titled,rever

answer = stringer("MATHew OstrAnder")


print "Smooshing two iterables together"
def combo(iter1, iter2):
  smooshed = [];
  for (index, value) in enumerate(iter1):
    print iter2[index]
    print value
    smooshed.append((value,iter2[index]))
  return smooshed


answer = combo('abc','gef')
print answer
