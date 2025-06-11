import pandas as pd
import khmercut
import Levenshtein
from khmer_norm import clean_and_normalize  # Import Khmer normalization function

# Function to compute WER correctly (word-level comparison)
def calculate_wer(gt_words, ocr_words):
    gt_words = [clean_and_normalize(w) for w in gt_words]
    ocr_words = [clean_and_normalize(w) for w in ocr_words]

    if gt_words == ocr_words:
        return 0.0

    gt_str, ocr_str = " ".join(gt_words), " ".join(ocr_words)
    lev_distance = Levenshtein.distance(gt_str.split(), ocr_str.split())

    return lev_distance / max(len(gt_words), len(ocr_words))

# Function to compute CER correctly (character-level comparison)
def calculate_cer(gt_text, ocr_text):
    gt_text, ocr_text = clean_and_normalize(gt_text), clean_and_normalize(ocr_text)

    if gt_text == ocr_text:
        return 0.0

    lev_distance = Levenshtein.distance(gt_text, ocr_text)

    return lev_distance / max(len(gt_text), len(ocr_text))

# Load CSV file
csv_file = "input.csv"
data = pd.read_csv(csv_file, dtype=str).fillna('')

# Apply fixes to `gt` and `ocr`
data["gt_cleaned"] = data["gt"].apply(clean_and_normalize)
data["ocr_cleaned"] = data["ocr"].apply(clean_and_normalize)
data["gt_segmented"] = data["gt_cleaned"].apply(khmercut.tokenize)
data["ocr_segmented"] = data["ocr_cleaned"].apply(khmercut.tokenize)

# Compute WER & CER
data["WER"] = data.apply(lambda row: calculate_wer(row["gt_segmented"], row["ocr_segmented"]), axis=1)
data["CER"] = data.apply(lambda row: calculate_cer(row["gt_cleaned"], row["ocr_cleaned"]), axis=1)

# Keep only required columns
data = data[["name", "gt", "ocr", "gt_segmented", "ocr_segmented",  "CER", "WER"]]

# Save results
output_file = "output_wer_cer.csv"
data.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"✅ WER & CER calculation complete! Results saved to {output_file}")
