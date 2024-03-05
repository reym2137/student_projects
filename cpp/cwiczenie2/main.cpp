#include <iostream>

using namespace std;

int calculate_drift_lenght(float speed, float lenght){
	float result=speed*lenght/60;
	cout<<"Długość driftu:"<<result<<endl;
	return 0;
}

int main(){
	float speed=0;
	float lenght=0;
	cout<<"podaj prędkość samochodu(mph): ";
	cin>>speed;
	cout<<"podaj czas driftu(min):";
	cin>>lenght;
	calculate_drift_lenght(speed, lenght);
	return 0;
}
