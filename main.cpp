#include <random>
#include <iostream>
#include <deque>
#include "include/Graph.h"

int main(){
	int graph_size = 10;
	
	Graph G(graph_size, .3);
	G.print(std::cout);
	
	std::cout << std::endl;
	std::cout << std::endl;

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_real_distribution<> dis(0, graph_size);
	int a = {};
	int b = {};
	do {
		a = dis(gen);
		b = dis(gen);
	} while (a == b);


	std::cout << a << "\t" << b << std::endl;
	std::cout << std::endl;
	
	for(auto &i: G.bfs_search(a, b)){
		std::cout << i << " ";
	}
	std::cout << std::endl;

}

