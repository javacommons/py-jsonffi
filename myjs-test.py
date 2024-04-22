from jsonffi import MyJS

myjs = MyJS("nuget-tools.myjs.main.dll",
            ["{{ownername}}.{{appname}}.main.dll",
             "nuget-tools.dummy.main.dll"])
#myjs = MyJS("nuget-tools.myjs.main.dll")
myjs.Execute(
  """
  var Util = $ns("JsonDLL").Util;
  function add2(a, b) { return a + b; }
  Util.Print(add2(11, 22));
  """)
myjs.SetValue("x", 456)
myjs.Execute(
  """
  Util.Print(add2(33, 44));
  print(x);
  x += 1;
  """)
print(myjs.GetValue("x"))
v = myjs.Evaluate(
  """
  x * $1
  """, 100)
print(v)
myjs.Execute(
  """
  var svc1 = $ns("NAMESPACE").Service;
  Util.Print(svc1.Add2($1, $2));
  """, 110, 220)
myjs.Execute(
  """
  var svc2 = $ns("nuget_tools.dummy").Service;
  Util.Print(svc2.Add2($1, $2));
  """, 330, 440)
myjs.Execute(
  """
  Util.Print($1);
  """, {'a': 11, 'b': 22})
u = myjs.Evaluate(
  """
  undefined
  """)
print(u)
myjs.Call("Util.Print", 777);
myjs.Call('$ns("JsonDLL").Util.Print', 888);
myjs.Call('$ns("JsonDLL").MSys2.RunBashScript', False, """
    echo ハロー©
    """);
