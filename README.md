## Khmer OCR Evaluation Metrics (KHCWER)
These metrics are specifically designed to evaluate CER and WER in the context of the Khmer language. 
The key component of this method is the Khmer word normalization process and word segmentation, which applied the Khmer word segmentation of khmercut[^1] to split both the predicted and ground-truth texts and Khmer Syllable Reordering Search[^2] for Khmer text normalization; we adapted only the parts related to reordering each syllable while ensuring that the original structure of the text remains intact.

---

### References:
[^1]: KhmerCut: [https://github.com/seanghay/khmercut]
[^2]: Khmer Syllable Reordering Search: [https://github.com/seanghay/khmercut]
