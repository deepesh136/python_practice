with open("class_practice.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)
            
            
"""
way to check non ascii character error in your python file.just replace the file name in open().
"""
