import torch
from model import OptimizedTransformerModel
from tokenizer import FastBPETokenizer

def generate_text(prompt):
    print("Full generation code available after purchase")
    return f"Demo response for: {prompt}"

if __name__ == "__main__":
    text = generate_text("Привет")
    print(text)