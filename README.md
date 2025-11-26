# Use-case: generating synthetic data to improve named entity tagging

In these two notebooks we create an artificial scenario where we have very few data points (200 samples). So we want to augment our training set by creating another 200 synthetic data points and verify the impact on model performance.

The emphasis here lies on the methodology. We are not at all trying to create "the best ever NER" system! The notebooks touches on some fundamentals of LLMs, tokenization, synthetic data, and (crucially) evaluation and significance.

More information in the notebooks.

**Note**: unfortunately [Github is not great](https://github.com/orgs/community/discussions/155944) at displaying output of certain widgets (like `tqdm`) so chances are that the first notebook cannot be displayed in preview mode on the Github platform. It still just works though! So instead, try Google Colab.

1. Make sure you are signed into a Google account (so we can use Google Colab)
2. Open the notebooks. When you click on the link it will look like a bunch of strange characters. But at the top center there should be an option to "Open in Google Colab". Click that.
  - #1 https://drive.google.com/file/d/1kQYZHsYJnvbB55zyLcxoi05YdTF6IXXg/view?usp=sharing
  - #2 https://drive.google.com/file/d/1bh83ouElIZZEU6stPfPb2acPIdsKTrJr/view?usp=sharing
3. Save the notebook to your own drive before running: "File > Save a copy in Drive"

---

I created these notebooks from-scratch in the context of the [SSHOC-NL project](https://sshoc.nl/), specifically [Task 3.1](https://enrichment.ivdnt.org/) on methodologically sound data enrichment and evaluation.