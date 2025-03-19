# A-try-on-Law-LLM


Deploying a fine-tuned language generation model for the French legal field.


The model comes from https://huggingface.co/MaziyarPanahi/calme-3.1-llamaloi-3b


The video demonstration is also included in this repository: video.mp4.
(image.png)

I made some small adjustments based on the example code provided by the author:

I used a while loop for interactive dialogue instead of a single-turn conversation.

A parameter conversation_history is used to track the dialogue history, and each new input includes the previous conversation, ensuring the model doesn't produce inconsistent responses.

The format of the returned result was always a list containing nested dictionaries, which was hard to read. I made a slight modification so that it only returns text.
