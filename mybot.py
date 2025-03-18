import torch
from torch.utils.data import Dataset, DataLoader
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Step 1: Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # Set padding token to EOS token

# Step 2: Custom Dataset class for your text file
class TextDataset(Dataset):
    def __init__(self, file_path, tokenizer, block_size=128):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]  # Remove empty lines
        
        self.examples = []
        for line in lines:
            tokenized = tokenizer(line, truncation=True, max_length=block_size, padding="max_length", return_tensors="pt")
            self.examples.append(tokenized["input_ids"].squeeze(0))  # Remove batch dimension

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        return self.examples[idx]

# Load and prepare the dataset
data_file = "data2.txt"
dataset = TextDataset(data_file, tokenizer)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# Step 3: Set up training parameters
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
num_epochs = 4

# Step 4: Custom training loop
model.train()
for epoch in range(num_epochs):
    print(f"Epoch {epoch + 1}/{num_epochs}")
    total_loss = 0
    for batch in dataloader:
        inputs = batch.to(device)
        labels = inputs.clone()  # Labels are the same as inputs (shifted prediction)

        optimizer.zero_grad()
        outputs = model(input_ids=inputs, labels=labels)  # Model computes loss internally
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    avg_loss = total_loss / len(dataloader)
    print(f"Average loss: {avg_loss:.4f}")

# Step 5: Save the fine-tuned model and tokenizer
model.save_pretrained("./gpt2-finetuned")
tokenizer.save_pretrained("./gpt2-finetuned")

# Step 6: Chatbot interaction function
def generate_response(prompt, max_length=100):
    model.eval()
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to(device)
    outputs = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Step 7: Interactive loop
print("Chatbot is ready! Type 'exit' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = generate_response(user_input)
    print("Bot:", response)
