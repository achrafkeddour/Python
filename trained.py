import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Step 1: Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium" or "gpt2-large" for larger models if your hardware supports it
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Step 2: Prepare your dataset from "data.txt"
def load_dataset(file_path, tokenizer, block_size=128):
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size  # Adjust this based on your text length and GPU memory
    )
    return dataset

# Path to your data file
data_file = "data.txt"
train_dataset = load_dataset(data_file, tokenizer)

# Step 3: Set up data collator for language modeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # GPT-2 is not masked language model, so set this to False
)

# Step 4: Define training arguments
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned",  # Where to save the model
    overwrite_output_dir=True,
    num_train_epochs=3,  # Number of training epochs (adjust as needed)
    per_device_train_batch_size=4,  # Adjust based on your GPU memory
    save_steps=500,
    save_total_limit=2,
    logging_dir='./logs',
    logging_steps=100,
)

# Step 5: Initialize Trainer and fine-tune the model
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()

# Step 6: Save the fine-tuned model and tokenizer
model.save_pretrained("./gpt2-finetuned")
tokenizer.save_pretrained("./gpt2-finetuned")

# Step 7: Chatbot interaction function
def generate_response(prompt, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, do_sample=True, top_k=50, top_p=0.95)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Step 8: Interactive loop
print("Chatbot is ready! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = generate_response(user_input)
    print("Bot:", response)