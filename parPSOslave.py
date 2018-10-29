from mpi4py import MPI

comm = MPI.COMM_WORLD
status = MPI.Status()

def costFunction(x):
    sum=0
    for i in range(len(x)):
        sum+= x[i]*x[i]
    return sum

while(1):
    obj_recv = comm.recv(source=0, tag=MPI.ANY_TAG, status=status)
    tag = status.Get_tag()
    if tag == 200:
        break

    f = costFunction(obj_recv[1])
    obj_sent = (obj_recv[0], f)
    comm.send(obj_sent, dest=0)