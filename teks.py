from tqdm import tqdm

for char in tqdm(range(97, 123)):
    print(chr(char), end="", flush=True)
