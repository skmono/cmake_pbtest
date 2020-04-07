#include <hdr/helloworld.h>

int main(){
    Service service("0.0.0.0", 50051);
    service.RunService();
    return 0;
}