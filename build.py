import cx_Freeze
from cx_Freeze import setup , Executable

setup(name = "bill",
      version = "0.1",
      description = "We can generate bill",
      executables = [Executable(r"C:\Users\prashant\PycharmProjects\aws3\d3.py")])