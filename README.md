# Build-Programming
This repo will house the analysis scripts for the article: Logistics, Affordances, and Evaluation of Build Programming: A Code Reading Instructional Strategy.

**Suggested Citation**  
Amanpreet Kapoor, Tianwei Xie, Leon Kwan, and Christina Gardner-McCune. 2023. Logistics, Affordances, and Evaluation of Build Programming: A Code Reading Instructional Strategy. In Proceedings of 54th ACM Technical Symposium on Computer Science Education (SIGCSE ‘23), March 2023, Toronto, Canada. ACM, NY, USA, 7 pages.
https://doi.org/10.1145/3545945.3569756 

## How to Run

### Setup

Download Clang
- Windows: download [llvm 13.0.0](https://github.com/llvm/llvm-project/releases/tag/llvmorg-13.0.0)
- MacOS: `brew install llvm`

Install python dependencies
`pip install -r requirements.txt`

### Run
`python3 codeAnalyzer.py`

# Program Layout

`codeAnalyzer.py` provides metrics for all `.cpp` files of a directory with the Canvas naming convention `[student name]_[number]_[number]_[filename].cpp`. The results are outputed to the file `output.json`.

![readimage](https://user-images.githubusercontent.com/29406643/217935196-d6ba87d0-4a09-4eb4-9a7e-f1e15e4d8855.svg)
