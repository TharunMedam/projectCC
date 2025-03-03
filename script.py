import socket
import re
from collections import Counter

def main():
    doc1 = "IF-1.txt"
    doc2 = "AlwaysRememberUsThisWay-1.txt"
    with open(doc1, "r", encoding="utf-8") as f:
        content1 = f.read()
    with open(doc2, "r", encoding="utf-8") as f:
        content2 = f.read()
    words_doc1 = content1.split()
    words_doc2 = content2.split()
    count_doc1 = len(words_doc1)
    count_doc2 = len(words_doc2)
    total_words = count_doc1 + count_doc2
    processed_text1 = re.findall(r"[a-zA-Z']+", content1.lower())
    freq_doc1 = Counter(processed_text1)
    top_3_doc1 = freq_doc1.most_common(3)
    processed_text2 = re.findall(r"[a-zA-Z']+", content2.lower())
    expanded_terms = []
    for word in processed_text2:
        expanded_terms.extend(word.split("'"))
    expanded_terms = [word for word in expanded_terms if word != '']
    freq_doc2 = Counter(expanded_terms)
    top_3_doc2 = freq_doc2.most_common(3)
    system_ip = socket.gethostbyname(socket.gethostname())
    output_data = []
    output_data.append(f"Words in IF-1.txt: {count_doc1}")
    output_data.append(f"Words in AlwaysRememberUsThisWay-1.txt: {count_doc2}")
    output_data.append(f"Total words (both files): {total_words}")
    output_data.append("Top 3 most frequent words in IF-1.txt:")
    for word, cnt in top_3_doc1:
        output_data.append(f"{word}: {cnt}")
    output_data.append("Top 3 most frequent words in AlwaysRememberUsThisWay-1.txt (with contractions split):")
    for word, cnt in top_3_doc2:
        output_data.append(f"{word}: {cnt}")
    output_data.append(f"Container IP: {system_ip}")
    with open("output/result.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(output_data))
    print("\n".join(output_data))

if __name__ == "__main__":
    main()
