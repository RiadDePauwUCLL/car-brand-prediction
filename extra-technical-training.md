# Technical Training Details for Car Brand Classification


---

# Progressive Unfreezing in Neural Network Training

## Stages Structure
The training process is divided into sequential stages, each defined by:
- **Number of epochs**: How long to train at this stage (20 epochs per stage)
- **Unfreeze level**: How many blocks of the model to make trainable

```python
stages = [
    {'epochs': 20, 'unfreeze': 1},   
    {'epochs': 20, 'unfreeze': 2},  
    {'epochs': 20, 'unfreeze': 3},
    {'epochs': 20, 'unfreeze': 4},
    {'epochs': 20, 'unfreeze': 5},
]
```

## Unfreezing Mechanism
The `unfreeze_layers` function gradually makes more of the network trainable:

1. **Stage 1 (unfreeze=1)**: Only the fully connected (FC) layer and `layer4` (final convolutional block) are trainable
2. **Stage 2 (unfreeze=2)**: FC + `layer4` + `layer3` are trainable
3. **Stage 3 (unfreeze=3)**: Adds `layer2` to trainable layers
4. **Stage 4 (unfreeze=4)**: Adds `layer1` to trainable layers
5. **Stage 5 (unfreeze=5)**: Makes all layers trainable

## Benefits of This Approach
- **Transfer learning optimization**: Adapts higher-level features first before fine-tuning lower-level features
- **Prevents catastrophic forgetting**: Gradual adaptation preserves useful pretrained weights
- **Learning rate efficiency**: Each stage uses a declining learning rate as more layers are unfrozen
- **Progressive complexity**: Model capacity increases gradually throughout training

This approach is especially effective when fine-tuning a pretrained model for a new domain like car brand classification.

---

# Understanding OneCycleLR and SGD Parameters

## OneCycleLR Parameters

### `pct_start=0.2`
- **Purpose**: Controls what percentage of training is spent in the "warm-up" phase
- **How it works**: 
  - First 20% of training: Learning rate gradually increases from initial_lr to max_lr
  - Remaining 80%: Learning rate decreases from max_lr to a very small value
- **Effect**: Creates a smoother start to training, helping stabilize early optimization

### `div_factor=20`
- **Purpose**: Determines how much smaller the initial learning rate is compared to max_lr
- **How it works**: `initial_lr = max_lr / div_factor`
- **Example**: If `max_lr=0.03`, then training starts at `0.0015`
- **Effect**: Ensures training begins conservatively before accelerating

### `final_div_factor=100`
- **Purpose**: Determines how small the final learning rate becomes
- **How it works**: `final_lr = initial_lr / final_div_factor = max_lr / (div_factor * final_div_factor)`
- **Example**: With these values, the final learning rate is `max_lr / 2000`
- **Effect**: Allows fine-grained optimization at the end of training

## SGD Optimizer Parameters

### `lr=stage_lr * 3`
- **What changed**: The learning rate is multiplied by 3 (as noted in the comment)
- **Purpose**: Increases the baseline learning rate to potentially accelerate training
- **Risk/reward**: Higher learning rates can speed up convergence but may also cause instability

### `momentum=0.9`
- **Purpose**: Adds a fraction of the previous update to the current update
- **Effect**: Helps overcome small obstacles in the loss landscape and speeds up convergence
- **Value**: 0.9 is standard - 90% of previous update is carried forward

### `weight_decay=5e-4`
- **Purpose**: L2 regularization that prevents weights from growing too large
- **Effect**: Reduces overfitting by penalizing complex models
- **Note**: The commented value (1e-3) would provide stronger regularization

### `nesterov=True`
- **Purpose**: Advanced form of momentum that "looks ahead" in the update direction
- **Effect**: Usually provides better convergence than standard momentum
- **How it works**: Calculates gradients after applying momentum, leading to more accurate updates

Together, these parameters create a dynamic learning schedule that starts slow, accelerates quickly, then gradually decreases to fine-tune the model's weights.