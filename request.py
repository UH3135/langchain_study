from langserve import RemoteRunnable

chain = RemoteRunnable("https://flat-jasmine-uh3135-28992e63.koyeb.app/chat/playground/")
print(chain.invoke({"user_input":"안녕하세요"}))