#modules is a portion of a program(an extension file) that can be invoked through otherprograms withou having to write them inevery program
#modules can define classes and variables
#the use of modules is based on using a code(program body, functions,variable) already stored on it called import
#we can define our most used functions in a module and import it, instead of copying their definitions into different programs
import CIS_Module as s_m
#from CIS_Module import div as dv

print(s_m.add(2,3))
print(s_m.subt(4,5))
print(s_m.mult(3,3))
print(s_m.div(4,2))

##for efficiency reasons, each module is only imported once per interpreter session. Therfore, if you change your module,you must restart the interpreter -or, if it's just one module you want to test interactively,
##use importlib.reload(), e.g import importlib; importlib.reload(modulename)

#Serach Path
#while importing a module, python looks at several places. Interpreter first looks for a built in module. Then(if built in module not found). python looks into a list of directories defined in sys.path.The search is in this order
# 1. current directory
# 2. pythonpath
# 3. the installation dependent default directory

#in shell
#import CIS_Module
#dir(CIS_Module)
