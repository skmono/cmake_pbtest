#include <iostream>
#include <string>

#include <grpcpp/grpcpp.h>
#include <grpcpp/health_check_service_interface.h>
#include <grpcpp/ext/proto_server_reflection_plugin.h>

#include "helloworld.grpc.pb.h"
#include "helloworld.pb.h"

using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using grpc::Server;

using helloworld::Request;
using helloworld::Reply;
using helloworld::Greeter;

namespace hello{
    void say_hello();
}

class GreeterServiceImpl final : public Greeter::Service {
    Status SayHello(ServerContext*, const Request*, Reply*);
    Status SayBye(ServerContext*, const Request*, Reply*);
};


class Service{
public:
    Service(){server_address="0.0.0.0:50051";}
    Service(std::string, int);
    ~Service();
    void RunService(void);

private:
    GreeterServiceImpl service;
    std::string server_address;
    ServerBuilder builder;
};