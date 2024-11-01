from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/chat/")
print(chain.invoke({"user_input":"안녕하세요"}))