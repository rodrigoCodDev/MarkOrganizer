# MarkOrganizer

MarkOrganizer is a project to organize markdown files in an folder, like a project, splitting the file into parts. The initial perspective was to solve a problem with images, but, I want to make new ways to organize markdown files.



## The problem :building_construction:



[Typora](https://typora.io/) is one of the best markdown editors I've used recently. One of its functions is to be able to do ctrl + v on screenshots when you want to use them in markdowns. This is very practical. The problem is that this function saves the screenshot in the editor folders, not the markdown folder.

To solve this problem, I has create this program that captures all the images from the markdown file and puts them in a new markdown folder in an organized way.

It was made to organize the images, but the idea is to create new organizational features.



## How to execute? :computer:



This project was made in python, you need Python installed in your computer to execute this project. Another specification is that execute in Linux, there haven't test or version for windows, I going to arrange later.

When you download, open a terminal in the folder **src** and execute this command:

```bash
python main.py
```



## How to use? :file_folder:



In this version I have included one some function, it can work for Typora's problem or one markdown simple file that you want use. The program will only create this markdown folder and organize the images, how I explained. 

The program will be have two inputs:



| Input                                   | Explanation                                                  |
| --------------------------------------- | ------------------------------------------------------------ |
| **Enter the markdown file path:**       | You have to put the path of you markdown file. Like: /home/myuser/Documents/myMark.md |
| **Enter the new markdown folder path:** | You have to put the path of the folder you want to organize the Markdown. Like: /home/myuser/Documents/myUncreatedFolder |





