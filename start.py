from transformers import pipeline
import torch
from pprint import pprint


pipe = pipeline("text-generation",
                model="MaziyarPanahi/calme-3.1-llamaloi-3b",
                device=0,  
                torch_dtype=torch.float16,
                max_length= 1000) 

# 用于存储对话历史
conversation_history = []
n=1
# 循环以进行交互式对话
while True:


    user_input = input("You: ")

    if user_input.lower() == "exit":  
        break

    # 将对话历史添加到输入
    conversation_history.append({"role": "user", "content": user_input})


    input_for_model = conversation_history

  
    result = pipe(input_for_model)


    # 直接提取文本
    assistant_reply = result[0]['generated_text'][n]['content']

    # 打印纯文本回复
    print(f"Assistant: {assistant_reply}")


    conversation_history.append({"role": "assistant", "content": assistant_reply})
    n+=2
