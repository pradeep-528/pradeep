#!/usr/bin/python
# entering employee details and their count

class employee:
      count=0
      def __init__(self,name,salary):
          print name
          print salary
          employee.count+=1
          print employee.count
em=employee('pradeep',20000)
em=employee('kumar',18000)
