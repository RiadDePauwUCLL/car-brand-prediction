import scipy.io
import numpy as np
import os

def print_mat_info(filepath):
    """Load and print information from a MAT file using its actual variable names"""
    print(f"\n{'='*50}")
    print(f"Loading: {filepath}")
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None
    
    try:
        # Load the MAT file
        mat = scipy.io.loadmat(filepath)
        
        # Show all variables in the file (excluding system variables)
        variables = [k for k in mat.keys() if not k.startswith('__')]
        print(f"Variables in file: {variables}")
        
        if not variables:
            print("No valid variables found in file.")
            return None
            
        # Get the first non-system variable (most likely to be our annotations)
        var_name = variables[0] 
        print(f"Using variable: '{var_name}'")
        
        # Get the annotations array
        annotations = mat[var_name]
        
        # Count the number of entries
        num_entries = len(annotations)
        print(f"Number of entries: {num_entries}")
        
        # Display first 5 entries as a sample
        print("\nSample entries:")
        for i in range(min(5, num_entries)):
            try:
                # Handle different array structures
                if isinstance(annotations[i], np.ndarray) and annotations[i].size > 0:
                    if isinstance(annotations[i][0], np.ndarray):
                        print(f"  {i+1}. {annotations[i][0][0]}")
                    else:
                        print(f"  {i+1}. {annotations[i][0]}")
                else:
                    print(f"  {i+1}. {annotations[i]}")
            except:
                print(f"  {i+1}. [Complex structure - cannot display simply]")
        
        # Data type information
        print(f"\nData structure type: {type(annotations)}")
        print(f"Shape of annotations array: {annotations.shape}")
        
        return var_name, annotations
        
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

# Process both MAT files
result1 = print_mat_info('cars_annotations_v1.mat')
result2 = print_mat_info('cars_annotations_v2.mat')

# Compare the data between versions
if result1 and result2:
    var_name1, annotations1 = result1
    var_name2, annotations2 = result2
    
    print("\n== Comparison between v1 and v2 ==")
    print(f"v1 entries ({var_name1}): {len(annotations1)}")
    print(f"v2 entries ({var_name2}): {len(annotations2)}")
    print(f"Difference: {abs(len(annotations1) - len(annotations2))} entries")
    
    # Check for first entries
    print("\nSample comparison (first entry):")
    try:
        # Try to extract and display first entry from v1
        if isinstance(annotations1[0], np.ndarray) and annotations1[0].size > 0:
            if isinstance(annotations1[0][0], np.ndarray):
                print(f"v1: {annotations1[0][0][0]}")
            else:
                print(f"v1: {annotations1[0][0]}")
    except:
        print("v1: [Cannot display first entry]")
        
    try:
        # Try to extract and display first entry from v2
        if isinstance(annotations2[0], np.ndarray) and annotations2[0].size > 0:
            if isinstance(annotations2[0][0], np.ndarray):
                print(f"v2: {annotations2[0][0][0]}")
            else:
                print(f"v2: {annotations2[0][0]}")
    except:
        print("v2: [Cannot display first entry]")