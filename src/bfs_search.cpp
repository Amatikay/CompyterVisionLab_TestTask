#include "../include/Graph.h"
#include <deque>
#include <unordered_map>
#include <set>

std::list<int> Graph::bfs_search(const int a, const int b){
	if (a == b){
		return {a};
	}
	 std::deque<int> queue = {a};
	 std::set<int> visited = {a};
	 std::unordered_map<int, int> prev;
	 prev[a] = -1;
	 
	 while ( !queue.empty() ){
	 
	 	int node = queue.front();
	 	queue.pop_front();
	 	
	 	if (node == b){
	 		std::list<int> path;
	 		
	 		while (node != -1){
	 			path.push_back(node);
	 			node = prev[node];
	 		}
	 		path.reverse();
	 		return path;
	 	}

	 	for (int &neighbor: adj_list[node]){
	 		if (!visited.contains(neighbor)){
	 			visited.insert(neighbor);
	 			queue.push_back(neighbor);
	 			prev[neighbor] = node;
	 		} 
	 	}
	 }
	return {-2}; 
	}
