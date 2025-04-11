#!/bin/bash

# Deleting best .pth PyTorch model
if [ -f "best_resnet_car_classifier.pth" ]; then
    echo "Best model found"
    echo "Cleaning up the best resnet car classifier model"
    rm best_resnet_car_classifier.pth
else
    echo "Best resnet car classifier not found."
fi

# If using the basic training model
if [ -f "best_model.pth" ]; then
    echo "Basic best model found"
    echo "Deleting basic best model"
    rm best_model.pth
else
    echo "Basic training model not used"
fi

# Deleting the checkpoints
if [ -d "./checkpoints/" ]; then
    echo "Checkpoints found"
    echo "Cleaning up the checkpoints dir"
    rm -rf ./checkpoints/*
else
    echo "No checkpoints found."
fi

echo "Cleanup complete."
