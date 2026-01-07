# 5-Gram Language Model — Edgar Allan Poe


This repository contains a **5-gram language model** implemented in Python, trained on the works of **Edgar Allan Poe** from Project Gutenberg. The model learns word sequences and generates text that mimics the author’s style.

## 📥 Dataset

The text data used for training is obtained from **Project Gutenberg**.

Download the plain text file here:
👉 https://www.gutenberg.org/ebooks/10031.txt.utf-8  
*(Save this file as `poe.txt` in the project folder.)*

---

## 📂 Repository Structure
n-gram-language-model/  
├─ poe.txt  
├─ 5-gramModel.py  
├─ README.md  
└─ 423181_output.pdf  



---

## 🧠 Model Description

We implement a **5-gram model** that predicts the next word based on the **previous 4 words**.

### What the model does:

1. **Cleans and tokenizes** the text
2. Builds **5-gram frequency counts**
3. Uses the model to **generate text** given a sample phrase
4. It only predicts the next word if the current 4 words context window is contigously present in the training data.

---

## 🧪 How to Run the Model

1. Download `poe.txt` (from Project Gutenberg) and put it in the project folder.
2. Run the Python code:
   ```bash
   python 5-gramModel.py

