CXX = g++
DEBUG_FLAGS = -g
STD_FLAGS = -std=c++20
CXXFLAGS = $(DEBUG_FLAGS) $(STD_FLAGS)
BUILD_DIR = build

all: $(BUILD_DIR)/main

$(BUILD_DIR)/main: main.o bfs_search.o Graph.o
	@mkdir -p $(BUILD_DIR)
	$(CXX) main.o bfs_search.o Graph.o -o $(BUILD_DIR)/main $(CXXFLAGS)

main.o : main.cpp
	$(CXX) main.cpp $(CXXFLAGS) -c

bfs_search.o: src/bfs_search.cpp
	$(CXX) src/bfs_search.cpp  $(CXXFLAGS) -c
	
Graph.o: src/Graph.cpp
	$(CXX) src/Graph.cpp  $(CXXFLAGS) -c
	
clean:
	rm -rf ./build *.o

run: all
	$(BUILD_DIR)/main
