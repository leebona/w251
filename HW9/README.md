# Homework 9
## Questions
### 1. How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
  - It took about 18 hours to train with 40,000 training steps with 2 nodes and four V-100 GPUs total.
### 2. Do you think your model is fully trained? How can you tell?
  - I think the model is almost fully trained if not all because all the graphs including the BLEU Score and the Train Loss graphs are stabilized as shown below; so, I wouldn't expect to see a big change between my model and a fully trained model.

  ![BLEU Score](Eval_BLEU_Score.png)

  ![Train Loss](https://github.com/leebona/w251/tree/master/HW9/Extra_Images/train_loss.png)

### 3. Were you overfitting?
  - Answer
### 4. Were your GPUs fully utilized?
  - All of them were fully utilized for the most of the time as shown below. Even when the GPUs were not fully utilized, the utilization rate was quite high with a value of at least around 80%.
### 5. Did you monitor network traffic (hint: apt install nmon)? Was network the bottleneck?
  - Answer
### 6. Take a look at the plot of the learning rate and then check the config file. Can you explain this setting?
  - Answer
### 7. How big was your training set (mb)? How many training lines did it contain?
  - Answer
### 8. What are the files that a TF checkpoint is comprised of?
  - Answer
### 9. How big is your resulting model checkpoint (mb)?
  - Answer
### 10. Remember the definition of a "step". How long did an average step take?
  - Average time per step was 1.625s.
### 11. How does that correlate with the observed network utilization between nodes?
  - Answer

* Validation loss: 1.6316
* Eval BLUE score: 0.3644
* Avg time per step: 1.625s
* Avg objects per second: 38391.122
