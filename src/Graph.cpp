#include "../include/Graph.h"
#include <random>
#include <iostream>
Graph::Graph(const int size, const float p){
	adj_list.resize(size);
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_real_distribution<> dis(0.0, 1.0);

	for (int i = 0; i < size; i++){
		for (int j = i+1; j < size; j++){
			if (dis(gen) < p ) {
				adj_list[i].push_back(j);
				adj_list[j].push_back(i);
			}
		}
	} 
}

void Graph::print(){
	for(auto &i: adj_list){
		for(auto &j: i){
			std::cout<< j << " ";
		}
		std::cout << std::endl;
	}
}

