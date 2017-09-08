import tensorflow as tf

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
# print(node1)
# print(node2)
# || Tensor("Const:0", shape=(), dtype=float32)
# || Tensor("Const_1:0", shape=(), dtype=float32)
sess = tf.Session()
# print(sess.run([node1, node2]))
# || [3.0, 4.0]

node3 = tf.add(node1, node2)
# print('node3', node3)
# print('sess.run([node3])', sess.run([node3]))
# || [3.0, 4.0]
# || node3 Tensor("Add:0", shape=(), dtype=float32)
# || sess.run([node3]) [7.0]

a = tf.placeholder(tf.float32)
# print('a', a)
b = tf.placeholder(tf.float32)
# print('b', b)
adder_node = a + b # + provide a shortcut for tf.add(a, b)
# print('adder_node', adder_node)
# print(sess.run(adder_node, {a: 3, b: 4.5}))
# print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))
# || a Tensor("Placeholder:0", dtype=float32)
# || b Tensor("Placeholder_1:0", dtype=float32)
# || adder_node Tensor("add:0", dtype=float32)
# || 7.5
# || [ 3.  7.]
#
add_and_tripe = adder_node * 3
# print(sess.run(add_and_tripe, {a: 3, b: 4.5}))

W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
init = tf.global_variables_initializer()
sess.run(init)
# print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
# || [ 0.          0.30000001  0.60000002  0.90000004]
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
# print(sess.run(squared_deltas, {x: [1, 2], y: [2, 3]}))
# || [ 4.          7.29000044]
# print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
# fixW = tf.assign(W, [-1.])
# fixb = tf.assign(b, [1.])
# sess.run([fixW, fixb])
# print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
# || 0.0

# optimizer = tf.train.GradientDescentOptimizer(0.01)
# train = optimizer.minimize(loss)
# for i in range(1000):
#     sess.run(train,  {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})
# print(sess.run([W, b]))
# || [array([-0.9999969], dtype=float32), array([ 0.99999082], dtype=float32)]

#Implement linear model.
# train_X = [1, 2, 3, 4]
# train_Y = [0, -1, -2, -3]
#
# W = tf.Variable([3.0])
# b = tf.Variable([1.0])
# x = tf.placeholder(tf.float32)
# y = tf.placeholder(tf.float32)
#
# linear_model = W * x + b
# squared_deltas = tf.square(linear_model - y)
# loss = tf.reduce_sum(squared_deltas)
#
# optimier = tf.train.GradientDescentOptimizer(0.01)
# train = optimier.minimize(loss)
#
# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     for i in range(1000):
#         sess.run(train, {x: train_X, y: train_Y})
#     print(sess.run([W, b]))
