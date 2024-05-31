from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("./ZhipuAI/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("./ZhipuAI/chatglm3-6b", trust_remote_code=True).half().cuda()
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
response, history = model.chat(tokenizer, "如何提高学习效率？", history=history)
print(response)