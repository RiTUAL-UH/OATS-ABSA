# OATS-ABSA
This repository contains the OATS (Opinion Aspect Target Sentiment) dataset for the Aspect Sentiment Quad Prediction (ASQP) or Aspect-Category-Opinion-Sentiment (ACOS) task.
In addition to the opinion quadruples, we provide review-level tuples with the dominating sentiment polarity of each aspect category that has an opinion in that review. 

We annotated 3 datasets from scratch from different domains, including Amazon FineFood reviews, Coursera course reviews, and TripAdvisor Hotel reviews. 

Each of these datasets can be found under their respective folders in the data/ directory:
- data/{domain}:
  - data/{domain}/quads  
    - XML (similar to the SemEval-2016 format, along with the opinion phrase annotations and their _from_index_ and _to_index_)
    - txt (similar to the ASQP dataset that has a list of lists for each review sentence, where each inner list corresponds to an opinion quadruple with the target, aspect category, sentiment, and opinion phrase in the order)
  - data/{domain}/tuples
    - XML (with aspect category and sentiment polarity for each mentioned category in the review)
    - txt (list of lists for each review, where each inner list corresponds to an opinion tuple with the aspect category and dominating sentiment polarity)

_{domain}_: \[amazon_ff, coursera, hotels\]

If you use this dataset in your research, please cite the following paper: 
[OATS: Opinion Aspect Target Sentiment Quadruple Extraction Dataset for Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2309.13297)
This paper is accepted at **LREC/COLING 2024** and the proceedings link will be updated soon!!
```
@misc{chebolu2023oats,
      title={OATS: Opinion Aspect Target Sentiment Quadruple Extraction Dataset for Aspect-Based Sentiment Analysis}, 
      author={Siva Uday Sampreeth Chebolu and Franck Dernoncourt and Nedim Lipka and Thamar Solorio},
      year={2023},
      eprint={2309.13297},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```
