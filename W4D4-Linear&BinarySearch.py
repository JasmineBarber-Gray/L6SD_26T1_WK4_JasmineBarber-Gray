#what is Linear Search?
#A linear search (or sequential search) is one of the simplest searching techniques. 
#It works by checking each element in a list sequentially until the target value is found or the list ends. 
#It does not require the data to be sorted and works on any data type.

#How it works:
#Start from the first element of the array.
#Compare the current element with the target value.
#If a match is found, return the index.
#If no match is found after checking all elements, return -1.

import random
import time
import pandas as pd

#Linear Search Function
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Element found
    return -1  # Element not found

#Example 1: Searching in a sorted list of numbers
sorted_values = [12, 24, 30, 42, 55, 63, 75, 82, 91, 99]
target_num = 42
start = time.perf_counter()
index = linear_search(sorted_values, target_num)
end = time.perf_counter()
print(f"Linear Search: {target_num} found at index {index}")
print(f"Time taken: {end-start:.6f} seconds")

#Example 2: Searching in a list of strings
string_list = [ "apple", "banana", "orange", "grape", "kiwi", "melon", "peach",
                "strawberry", "blueberry", "raspberry", "cherry", "pineapple",
                "mango", "watermelon", "pomegranate", "pear", "plum", "apricot",
                "fig", "lemon", "lime", "coconut", "avocado", "blackberry",
                "cranberry", "guava", "passionfruit", "dragonfruit", "kiwifruit",
                "papaya" ]

for fruit in ["pomegranate", "blueberry", "lime", "boat"]:
    index = linear_search(string_list, fruit)
    if index != -1:
        print(f"{fruit} found at index {index}")
    else:
        print(f"{fruit} not found in list")

#Example 3: Random list
random_list = [random.randint(1, 100) for _ in range(30)]
target_num = random.choice(random_list)  # Pick a number that exists
print(f"Random List: {random_list}")
index = linear_search(random_list, target_num)
print(f"Found {target_num} at index {index} after linear search")

#What is Binary Search?
#Binary Search is an efficient algorithm for finding the position of a target element in a sorted array. 
#It works by repeatedly dividing the search interval in half, achieving a time complexity of O(log n).

#how does it work?
#for it to function correctly, certain preconditions must be met:

#1:Sorted Data: The dataset must be sorted in ascending or descending order. 
#Binary Search relies on the ability to compare the target with the middle element and decide whether to search in the left or right half. 
#Without sorting, this logic fails.

#2:Random Access: The data structure should allow constant-time access to its elements. 
#This is typically true for arrays or lists, where elements can be accessed directly using an index.

#3:Monotonic Search Space: The search space must exhibit a monotonic property, meaning the values should consistently increase or decrease. 
#This ensures that comparisons with the middle element can correctly guide the search.

# Binary Search Function
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = 0  # Count iterations
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, steps  # Found element
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, steps  # Element not found

# Binary search on sorted numbers
sorted_values = [12, 24, 30, 42, 55, 63, 75, 82, 91, 99]
target_num = 42
index, steps = binary_search(sorted_values, target_num)
print(f"Binary Search: {target_num} found at index {index} in {steps} steps")

# Binary search on sorted strings
sorted_strings = sorted(string_list)
for fruit in ["pomegranate", "blueberry", "lime", "boat"]:
    index, steps = binary_search(sorted_strings, fruit)
    if index != -1:
        print(f"{fruit} found at index {index} in {steps} steps")
    else:
        print(f"{fruit} not found after {steps} steps")
        
#What is Breadth-First Search?
#BFS  is a graph traversal algorithm that explores all nodes at the current depth level before moving to the next level.

#how does it work?
#Start from a given source node.
#Use a queue to keep track of nodes to visit next.
#Mark visited nodes to avoid processing them again.
#Process nodes level by level until the queue is empty.

from collections import deque

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return result

print("BFS traversal starting from A:", bfs(graph, 'A'))

#What is Depth-First Search?
#DFS is a graph/tree traversal algorithm that explores as far as possible along each branch before backtracking.
#Its useful for tasks like maze solving, cycle detection, and exploring decision trees.

#how does it work?
#Start at the source node.
#Mark the node as visited.
#Explore one of its unvisited neighbors.
#Repeat the process recursively (or using a stack) until you reach a node with no unvisited neighbors.
#Backtrack to explore other branches

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

print("DFS traversal starting from A:", dfs(graph, 'A'))