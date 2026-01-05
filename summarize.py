import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

from transformers import pipeline

# ================================
# MODEL SELECTION
# ================================

# ✅ FINAL MODEL (default – stable, faithful summaries)
SUMMARIZATION_MODEL = "facebook/bart-large-cnn"

# 🔬 EXPERIMENTED MODEL (commented – caused hallucinations on narrative text)
# SUMMARIZATION_MODEL = "t5-base"


# ================================
# LOAD SUMMARIZER ONCE
# ================================
summarizer = pipeline(
    "summarization",
    model=SUMMARIZATION_MODEL
)


# ================================
# SUMMARIZATION FUNCTION
# ================================
def summarize_text(text):
    word_count = len(text.split())

    # ---- SHORT TEXT ----
    if word_count < 150:
        result = summarizer(
            text,
            max_length=80,
            min_length=30,
            do_sample=False
        )

    # ---- MEDIUM TEXT ----
    elif word_count < 400:
        result = summarizer(
            text,
            max_length=140,
            min_length=60,
            do_sample=False
        )

    # ---- LONG TEXT ----
    else:
        result = summarizer(
            text,
            max_length=200,
            min_length=90,
            do_sample=False
        )

    return result[0]["summary_text"]
