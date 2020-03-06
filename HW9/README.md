# Homework 9
## Questions
### 1. How long does it take to complete the training run? (hint: this session is on distributed training, so it will take a while)
  - It took about 18 hours to train with 40,000 training steps with 2 nodes and four V-100 GPUs total.
### 2. Do you think your model is fully trained? How can you tell?
  - I think the model is almost fully trained if not all because all the graphs including the BLEU Score and the Train Loss graphs are stabilized as shown below; so, I wouldn't expect to see a big change between my model and a fully trained model.
  - Graphs

|            BLEU Score           |                 Train Loss                |
|:-------------------------------:|:-----------------------------------------:|
| <img src="Eval_BLEU_Score.png"> | <img src="./Extra_Images/train_loss.png"> |

### 3. Were you overfitting?
  - Looking the train and validation loss graphs, I do not see a sign of overfitting as both training and validation loss decrease to a point of stability with a minimal gap between the two final loss values.
  - Graphs

|                 Train Loss                | Evaluation(Validation) Loss |
|:-----------------------------------------:|:---------------------------:|
| <img src="./Extra_Images/train_loss.png"> |  <img src="eval_loss.png">  |

### 4. Were your GPUs fully utilized?
  - All of them were fully utilized for the most of the time as shown below. Even when the GPUs were not fully utilized, the utilization rate was quite high with a value of at least around 80%.
  - GPU Utilization of v100a and v100b

|                   v100a                  |                   v100b                  |
|:----------------------------------------:|:----------------------------------------:|
| <img src="./Extra_Images/v100a_gpu.png"> | <img src="./Extra_Images/v100b_gpu.png"> |

### 5. Did you monitor network traffic (hint: apt install nmon)? Was network the bottleneck?
  - Answer
  - Network Monitoring of v100a and v100b

|                   v100a                   |                   v100b                   |
|:-----------------------------------------:|:-----------------------------------------:|
| <img src="./Extra_Images/v100a_nmon.png"> | <img src="./Extra_Images/v100b_nmon.png"> |

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
