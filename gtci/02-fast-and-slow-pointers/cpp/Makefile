CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -pedantic
SRC = $(wildcard *.cpp)
EXEC_DIR = exec
TARGETS = $(patsubst %.cpp,$(EXEC_DIR)/%, $(SRC))

all: $(EXEC_DIR) $(TARGETS)

$(EXEC_DIR):
	mkdir -p $(EXEC_DIR)

$(EXEC_DIR)/%: %.cpp | $(EXEC_DIR)
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -rf $(EXEC_DIR)
