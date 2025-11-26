# Use-case: generating synthetic data to improve named entity tagging

In these two notebooks we create an artificial scenario where we have very few data points (200 samples). So we want to augment our training set by creating another 200 synthetic data points and verify the impact on model performance.

The emphasis here lies on the methodology. We are not at all trying to create "the best ever NER" system! The notebooks touches on some fundamentals of LLMs, tokenization, synthetic data, and (crucially) evaluation and significance.

More information in the notebooks.

**Note**: unfortunately [Github is not great](https://github.com/orgs/community/discussions/155944) at displaying output of certain widgets (like `tqdm`) so chances are that the first notebook cannot be displayed in preview mode on the Github platform. It still just works though! So instead, try Google Colab.

1. Make sure you are signed into a Google account (so you can use Google Colab free tier and save your version of the notebook)
2. Open the notebooks. 
  - #1 https://colab.research.google.com/drive/1pqI5GU6UVQhUr9HOKehUrJCY8OBc6GV3
  - #2 https://colab.research.google.com/drive/17C1LTiw4OoQF0xdZMX2C_V1Xc1m2okdt
3. ⚠️ Save the notebook to your own drive before running: "File > Save a copy in Drive"

⚠️ Despite best efforts of making results reproducible, they seem to differ wildly between environments. Running the notebook locally for me repeatedly leads to the same results, but running the exact same code on Colab still leads to large differences that propagate and that **may impact the analyses**! So the descriptive cells that discuss the results may not hold true. That is not a problem, however, since the goal of the notebook was educational in nature. So perhaps the best approach to this notebook is to first read it with its current output cells in tact, so you should follow along with "the story" exactly as written. And as soon as you start running your own experiments, you can put the story aside and begin your own adventure.

---

I created these notebooks from-scratch in the context of the [SSHOC-NL project](https://sshoc.nl/), specifically [Task 3.1](https://enrichment.ivdnt.org/) on methodologically sound data enrichment and evaluation.