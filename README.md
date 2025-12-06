# CISC121-Project---Binary-Search-Visulization

https://huggingface.co/spaces/blizzardlizzer/binarysearch

A visualization of Binary search

The reason why I chose this algorithm is because of its applicability in the real world when analyzing data


**Computational Thinking**

Decomposition
- think about how to set up your pointers
- think about how to move your pointers based on the target
- think about when to know the target is found

Pattern Recognition
  - Binary search is an algorithm, so it works the same for any list size
  - The method for finding mid, left and right pointers works the same for every list
  - and then as the algorithm goes on, the new pointers are also found the same way for each list
 
 Abstraction
 - The parts that will be shown to the user are the left, right and mid pointers, as well as how they move.
    - This will be done using different highlights
 - The calculations for mid can also be shown to help with understanding how the pointers are chosen
 - The halves of the list will also be shown to help with seeing how the algorithm finds the target
 - The parts that will not be shown are how the input or generated list is generated, as that is not important.
 -  The only thing that matters is the user seeing how binary search searches through their list

Algorithmic Design
- The user will first be asked to input a list of numbers with the option to generate a random list of size 50 to test the algorithm
- The program will then generate the list and perform the pointer calculations, and the algorithm will run until the target is found or not found
- The user can choose between an animated version of a version that displays each step 1 by 1
- This will be done using Gradio to provide a visualization of the search


**Flowchart**
<img width="664" height="738" alt="image" src="https://github.com/user-attachments/assets/9bf55c2f-653c-4c0c-8ba0-57b906237a7b" />




**Screenshots/ gif**

**static**

<img width="592" height="329" alt="image" src="https://github.com/user-attachments/assets/beb9e76a-4907-43a1-bf17-536f6dae959b" />

Since the target is in the list, target is found



<img width="624" height="477" alt="image" src="https://github.com/user-attachments/assets/69d2da33-4fd7-4965-801a-ef3e3853e02a" />

since the target is not in the list, target is not found



<img width="353" height="312" alt="image" src="https://github.com/user-attachments/assets/cfc8afd0-08d8-416f-8197-575dce1aaa3d" />

Error handling: the input list is not sorted




**Animated**



![ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/9170dbcc-c319-46d3-89c8-7bac215e4d09)

Random array



![ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/253d2810-758d-427c-9891-703f977e62d0)

user given array

**Steps to Run**
- choose which visulization you want(step by step or animated)
- then enter your list or choose a random array for the animated version
- then watch the algorithm solve the problem

**AI Disclaimer**
- the binary search algorithm was make by me
- the visuals with gradio as well as the visuals within the algorithm steps, were created with the help of ai
  
