import os
os.system("vllm serve 'vikhyatk/moondream2' --host 0.0.0.0 --port 8000 --device cpu")
