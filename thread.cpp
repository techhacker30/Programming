#include <iostream>
#include <thread>
using namespace std;

void naming(){
	std::cout<<"Printing a name"<<endl;
	cout<<"this is thread"<<endl;
}

int main(){
	thread t(naming);
	t.join(); //the join() run and main thread wait untile the threads work was done
	//t.detach() //the detach() functon will terminated if main function was done their work. you can not join the thread again after detaching.
	std::cout<<"Run After Thread Run"<<endl;
	return 0;
}
