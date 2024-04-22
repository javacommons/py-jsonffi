from jsonffi import MyJS

myjs = MyJS("nuget-tools.myjs.main.dll", ["{{ownername}}.{{appname}}.main.dll"])
myjs.Execute(
  """
  var TestClass = $ns("NAMESPACE").TestClass;
  """)
myjs.Execute(
  """
  var o = new TestClass($1, $2);
  """, 11, 20)
v = myjs.Call(
  """
  o.Area
  """)
print(v)
