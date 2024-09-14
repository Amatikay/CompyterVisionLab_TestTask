#ifndef GRAPH_H
#define GRAPH_H

#include <list>
#include <vector>

class Graph {
public:	
	/*
	Конструктор с парамтером генерирует случайный,
	ненаправленный, невзвешенный граф по модели 
	Эрдёша Реньи
	*/
	Graph(const int size, const float p);

	void print();
	std::list<int> bfs_search(const int a,const int b);
	~Graph(){};
private:
	std::vector<std::vector<int>> adj_list;
};

#endif
