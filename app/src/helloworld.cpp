#include <iostream>
#include "helloworld.h"


namespace hello{
void say_hello(){
    helloworld::Request msg;
    msg.set_name("Sejun");
    std::cout<<"Hello, "<<msg.name()<<std::endl;
}
}

Status GreeterServiceImpl::SayHello(ServerContext* context,
                                const Request* request,
                                Reply* reply) {
    std::string prefix("Hello");
    std::cout<<"SayHello:Received from "<<request->name()<<std::endl;
    reply->set_message(prefix+request->name());
    return Status::OK;
}

Status GreeterServiceImpl::SayBye(ServerContext* context,
                                const Request* request,
                                Reply* reply) {
    std::string prefix("Bye");
    std::cout<<"SayBye:Received from "<<request->name()<<std::endl;
    reply->set_message(prefix+request->name());
    return Status::OK;
}


Service::Service(std::string addr, int port)
{
    server_address= addr+":"+std::to_string(port);
    std::cout<<server_address<<std::endl;
}

Service::~Service()
{
    server_address = "\0";
}
void Service::RunService(){
    grpc::EnableDefaultHealthCheckService(true);
    grpc::reflection::InitProtoReflectionServerBuilderPlugin();

    // Listen on the given address without any authentication mechanism.
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    // Register "service" as the instance through which we'll communicate with
    // clients. In this case it corresponds to an *synchronous* service.
    builder.RegisterService(&service);
    // Finally assemble the server.
    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;

    // Wait for the server to shutdown. Note that some other thread must be
    // responsible for shutting down the server for this call to ever return.
    server->Wait();    
}