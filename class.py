class employee:
   name=""
   def getname(self,str):
        self.name=str

obj=employee()
obj.getname("Sourabh")

print(obj.name)