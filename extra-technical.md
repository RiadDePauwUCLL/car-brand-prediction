# Enhanced Challenges Section for Technical Report

## Data Preparation & Model Training Challenges

### Data Collection & Quality Issues

Your project faced significant data challenges that required sophisticated solutions:

- **Data Scraping & Image Collection**: You implemented multiple custom scraping solutions to build a comprehensive dataset:
  
  - A Pexels API wrapper (`scraper.py`) that authenticates with the API, performs parametrized searches for car brands, and systematically saves images to brand-specific directories
  
  - A Google Images crawler (`google_images_scraper.py`) that leverages the icrawler library to collect additional images with custom search terms like "MG car back" to ensure diverse viewing angles
  
  - Image consolidation utilities (`combine.py`) that process and unify scraped images from multiple sources, generating randomized filenames to prevent bias from naming patterns
  
  - Filename normalization scripts (`rename.py`) to handle special characters in car model names (e.g., replacing "Mégane" with "Megane") for consistent labeling

- **Inconsistent Image Sources**: The dataset combined images from multiple repositories with varying quality standards. Many images contained watermarks, unusual angles, or partial car views that complicated recognition.

- **Filename Parsing Complexity**: As seen in your `analyze_image_filenames` function, extracting accurate brand information required complex pattern matching. You implemented an extensive `brand_mapping` dictionary with over 100 entries to standardize inconsistent naming conventions:

  ```python
  brand_mapping = {
      'bmw': 'BMW',
      'vw': 'VOLKSWAGEN',
      'merc': 'MERCEDES-BENZ',
      'benz': 'MERCEDES-BENZ',
      # Over 100 more mappings
  }
  ```

- **CSV Data Preparation**: You created a dedicated `csv-prep.ipynb` notebook that intelligently processes multiple car datasets, handling different delimiters, extracting car information from complex descriptions, and standardizing fuel types and transmission values. The notebook combines data from various sources while prioritizing rows with price information and exports a clean, unified dataset.

- **Handling Rare Brands**: You faced the challenge of maintaining representation for rare car manufacturers like "IRAN KHODRO" or "LONDON TAXI" while preventing them from being filtered out due to insufficient samples.

### Memory Management Constraints

Your implementation showed careful handling of memory limitations:

- **GPU Memory Bottlenecks**: Working with AMD GPUs through PyTorch DirectML required custom memory management. You implemented specialized functions like `aggressive_memory_cleanup()` and `memory_efficient_forward()` to prevent out-of-memory errors.

- **Batch Processing Adaptations**: When standard approaches failed, you dynamically split batches:
  
  ```python
  # From your memory_efficient_forward function
  if batch_size <= 1:
      print("Cannot split batch further, minimum batch size reached")
      raise e
  half = batch_size // 2
  out1 = model(inputs[:half])
  out2 = model(inputs[half:])
  ```

- **Caching Mechanism**: You implemented an intelligent caching system for preprocessed data to avoid redundant computations:

  ```python
  # Cache loading optimization
  if cache_valid:
      print("Loading datasets from cache...")
      with open(cache_path, 'rb') as f:
          cached_data = pickle.load(f)
  ```

- **Project Cleanup Automation**: You developed a `cleanup.sh` bash script to automate the removal of temporary files, models, and checkpoints, ensuring clean project state between training runs and preventing disk space issues when experimenting with different model configurations.

### Training Stability Issues

The progressive training approach encountered several challenges:

- **Gradient Explosions**: Early training attempts showed unstable loss values, requiring implementation of gradient clipping:

  ```python
  torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
  ```

- **Layer Freezing Balance**: Finding the optimal progression for unfreezing layers proved challenging - unfreezing too quickly led to catastrophic forgetting, while too slowly resulted in underfitting. Your final solution was a staged approach:

  ```python
  stages = [
      {'epochs': 20, 'unfreeze': 1},
      {'epochs': 20, 'unfreeze': 2},
      {'epochs': 20, 'unfreeze': 3},
      {'epochs': 20, 'unfreeze': 4},
      {'epochs': 20, 'unfreeze': 5},
  ]
  ```

- **Interrupted Training Recovery**: As evidenced in your progress file, training was interrupted at ~70% accuracy. You implemented a robust checkpoint system to resume from interruptions:

  ```python
  # From your progressV3 file
  checkpoint = torch.load(interrupt_checkpoint_path)
  Resuming from epoch 1 with best accuracy: 0.6611 (stage 1)
  ```

### Class Imbalance Management

Class imbalance was a persistent challenge throughout the project:

- **Extreme Distribution Skew**: Some popular brands like Toyota and BMW had thousands of samples while rare manufacturers had fewer than 30 images, creating significant bias.

- **Weighted Loss Implementation**: You addressed this with a sophisticated square-root-based weighting system:

  ```python
  class_weights = {cls: math.sqrt(total_samples / class_counts.get(cls, 1)) for cls in range(num_classes)}
  ```

- **Strategic Sampling**: Your implementation of `WeightedRandomSampler` ensured proper representation of minority classes:

  ```python
  sampler = WeightedRandomSampler(weights=sample_weights, 
                                  num_samples=len(sample_weights), 
                                  replacement=True)
  ```

### Cross-Brand Confusion

Visual similarity between related brands created persistent classification challenges:

- **Corporate Family Confusion**: Brands within the same corporate group (e.g., Volkswagen Group's Audi, VW, Seat, Škoda) share design languages, creating classification ambiguity.

- **Luxury/Economy Brand Pairs**: Your confusion matrices revealed systematic misclassification between luxury brands and their mainstream counterparts (Lexus/Toyota, Infiniti/Nissan, Acura/Honda).

- **Visual Feature Overlap**: Many vehicle designs, particularly in similar market segments (compact SUVs, midsize sedans), share silhouettes and proportions that complicated classification.