import tensorflow as tf

sess = tf.Session()
def per(leg, a):
    print(leg +"\n", sess.run(a))



def stp0():
    w = tf.Variable(0)
    y = tf.square(w)

    sess.run(tf.initialize_all_variables())
    for i in range(1,4):
        asi = w.assign(i)
        sess.run(asi)
        per("w", w)
        per("y", y)


    return
stp0()
W=0
y=W**2
for i in range(1,4):
        W=i
        print("W",W)
        print("y=W^2",y)