from concurrent import futures
import grpc

from protos import users_pb2_grpc, users_pb2


class UserService(users_pb2_grpc.UsersServicer):
    def GetUser(self, request, context):
        return users_pb2.UserResponse(name="John Doe", email="john@example.com")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
