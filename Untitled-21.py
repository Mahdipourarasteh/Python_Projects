xs = [3,1,2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)

xs.insert(1,25)
print(xs)
x = xs.pop()
print(x, xs)