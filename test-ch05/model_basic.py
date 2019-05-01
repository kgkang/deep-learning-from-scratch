
import netelements as net

g = net.Graph()
g.set_as_default()

A = net.Variable(10)
b = net.Variable(1)

x = net.Placeholder()

y = net.multiply(A,x)
z = net.add(y,b)

sess = net.Session()
result = sess.run(operation=z, feed_dict={x:10})

print(result)


