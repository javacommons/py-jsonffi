from jsonffi import JsonFFI

#api = JsonFFI("{{ownername}}.{{appname}}.main.dll")
api = JsonFFI("cpp_api_02.dll")
answer = api.call("add2", [11, 22])
print("answer={}".format(answer))

answer = api.call("div", [11, 22])
print("answer={}".format(answer))

answer = api.call("add2", [11, 22, 33])
print("answer={}".format(answer))
