import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from sentence_transformers import SentenceTransformer
print("Imported SentenceTransformer with parallelism disabled")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Loaded model")
