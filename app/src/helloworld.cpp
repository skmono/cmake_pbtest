#include <iostream>
#include "helloworld.h"
#include "helloworld.pb.h"


namespace hello{
void say_hello(){
    helloworld::Request msg;
    msg.set_name("Sejun");
    std::cout<<"Hello, "<<msg.name()<<std::endl;
}
}
