import os
import sys

# -----------------------------------------------static data section------------------------------------------------
# ---- Start Settings -----

# action_status value 1 will generate the index.html file
# action_status value 0 will view the index.html file in terminal
action_status=1 

# ---- END Settings ----- 
# list of files to be ignore during the execution 
ignore_list=["learning", ".git", "automation.py", "README.md" ,"assets" ,"index.html",".github"]

# index Html Static Part1
part1_text_file = open('./assets/part1.txt','r') 
part1_content=part1_text_file.read()

# index Html Static Part2
part2_text_file = open('./assets/part2.txt','r') 
part2_content=part2_text_file.read()
# -----------------------------------------------static data section------------------------------------------------


# -----------------------------------------------Function section------------------------------------------------
#function for Specific files removal from the list 
def optimize_list_function(input_list):
  if len(input_list)>1 :
    for i in ignore_list :
        input_list.remove(i)

def create_index_page_function(dynamic_part):
    final_data = part1_content+dynamic_part +part2_content
    if action_status==1:
      index_file = open("index.html", "w")
      index_file.write(final_data)
      index_file.close()
    if action_status==0:
      print(final_data)
    

def create_li_name_function(input):
    x = input.replace("_", " ")
    x = x.replace(".html", " Page")
    return x
# -----------------------------------------------Function section------------------------------------------------

# -----------------------------------------------Main section------------------------------------------------
# Get the list of all files and directories
path = "./"
dir_list = os.listdir(path)
optimize_list_function(dir_list)
dir_list.sort()
dynamic_part=''
if len(dir_list) > 0:
    for i in dir_list:
        # dynamic_part+= '''<li><a href="/'''+i+'">'+i+'''</a></li>'''
        dynamic_part+= '''<li><a href="/'''+i+'"target="_blank">'+create_li_name_function(i)+'''</a></li>'''

# Get the list of all files and directories

create_index_page_function(dynamic_part)
# -----------------------------------------------Main section------------------------------------------------


