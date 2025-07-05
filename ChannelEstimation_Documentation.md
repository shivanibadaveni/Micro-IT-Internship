# Channel Estimation using Linear Regression - MMSE Bound Approach

## Project Overview
This project implements a **Linear Regression-based Channel Estimator** for wireless communication systems, designed to approach the **Minimum Mean Squared Error (MMSE) bound** for channel estimation using machine learning techniques.

## Module Description

### LinearRegression_ChannelEstimation Module

#### **Input Signals**

1. **System Control Inputs:**
   - `clk`: System clock for synchronous operation
   - `rst`: Active-high reset signal
   - `enable`: Global enable signal for the module

2. **Pilot Signal Inputs:**
   - `pilot_signals[NUM_PILOTS-1:0]`: Array of received pilot signals
     - **Purpose**: Known reference signals transmitted to estimate channel
     - **Width**: 16-bit signed values
     - **Format**: Q10 fixed-point format (1024 = 1.0)
     - **Example**: QPSK pilots (+1, -1 values)

3. **Weight Matrix Inputs:**
   - `weights[NUM_CHANNELS-1:0][NUM_PILOTS-1:0]`: 2D array of weight coefficients
     - **Purpose**: Trainable parameters for linear regression
     - **Width**: 18-bit signed values for higher precision
     - **Function**: Maps pilot signals to channel estimates

4. **Bias Inputs:**
   - `bias[NUM_CHANNELS-1:0]`: Bias terms for each channel
     - **Purpose**: Offset correction for each channel estimate
     - **Width**: 16-bit signed values

5. **Control Signals:**
   - `update_weights`: Signal to update weight coefficients
   - `estimation_enable`: Triggers channel estimation process
   - `training_mode`: Enables training mode for MMSE optimization

6. **Training Inputs:**
   - `true_channels[NUM_CHANNELS-1:0]`: Reference channel values
     - **Purpose**: Ground truth for training and error computation
     - **Used for**: MMSE optimization and performance evaluation

#### **Output Signals**

1. **Channel Estimates:**
   - `channel_estimates[NUM_CHANNELS-1:0]`: Estimated channel coefficients
     - **Purpose**: Primary output - estimated channel state information
     - **Width**: 16-bit signed values
     - **Format**: Complex channel coefficients in fixed-point

2. **Status Outputs:**
   - `estimation_valid`: Indicates when channel estimates are valid
   - `overflow_flag`: Detects arithmetic overflow conditions

3. **Training Outputs:**
   - `estimation_error[NUM_CHANNELS-1:0]`: Estimation errors for each channel
     - **Purpose**: Used for MMSE optimization and weight updates
     - **Computation**: `true_channels - channel_estimates`

## MMSE Channel Estimation Theory

### Mathematical Background

The **MMSE estimator** minimizes the mean squared error between true and estimated channel coefficients:

```
J = E[||h - h_est||²]
```

Where:
- `h`: True channel vector
- `h_est`: Estimated channel vector
- `E[]`: Expectation operator

### Linear Regression Approach

The module implements:
```
h_est = W * x + b
```

Where:
- `x`: Pilot signal vector
- `W`: Weight matrix (trainable)
- `b`: Bias vector
- `h_est`: Channel estimate vector

### Key Features for MMSE Optimization

1. **Multi-Channel Support**: Estimates multiple channel coefficients simultaneously
2. **Training Mode**: Computes estimation errors for weight optimization
3. **Overflow Protection**: Prevents arithmetic overflow in accumulations
4. **State Machine**: Ensures proper timing and data flow

## Implementation Details

### State Machine Operation

1. **IDLE**: Waits for estimation trigger
2. **COMPUTE**: Calculates weight × pilot products
3. **ACCUMULATE**: Sums products for each channel
4. **OUTPUT**: Generates final estimates with bias
5. **ERROR_COMPUTE**: Calculates training errors (if in training mode)

### Precision and Scaling

- **Input Precision**: 16-bit for signals, 18-bit for weights
- **Internal Precision**: 32-bit accumulator to prevent overflow
- **Output Scaling**: Right-shift by 8 bits for proper scaling

### Hardware Efficiency

- **Parallel Processing**: All channels processed simultaneously
- **Pipeline-friendly**: State machine enables pipelined operation
- **Memory Efficient**: Uses arrays for multi-dimensional data

## Application to Wireless Communication

### Channel Estimation Scenario

1. **Transmitter**: Sends known pilot signals
2. **Channel**: Wireless channel distorts signals
3. **Receiver**: Receives distorted pilots
4. **Estimator**: Uses this module to estimate channel coefficients
5. **Equalization**: Uses estimates to correct data symbols

### MMSE Bound Approach

The module approaches the MMSE bound by:

1. **Optimal Weight Learning**: Trains weights to minimize MSE
2. **Multi-Pilot Utilization**: Uses multiple pilots for better accuracy
3. **Bias Compensation**: Corrects for systematic errors
4. **Error Feedback**: Provides error signals for adaptive learning

## Usage Example

### Basic Channel Estimation
```systemverilog
// Configure pilot signals (QPSK)
pilot_signals[0] = 16'd1024;   // +1
pilot_signals[1] = -16'd1024;  // -1
// ... more pilots

// Set initial weights (can be trained)
weights[0][0] = 16'd512;  // Example weight
// ... more weights

// Enable estimation
estimation_enable = 1;
// Wait for estimation_valid
// Read channel_estimates[]
```

### Training Mode
```systemverilog
// Provide true channel values
true_channels[0] = 16'd2048;
// ... more true channels

// Enable training mode
training_mode = 1;
estimation_enable = 1;

// After estimation_valid, read estimation_error[]
// Use errors to update weights for MMSE optimization
```

## Performance Metrics

### Key Metrics for MMSE Evaluation

1. **Mean Squared Error (MSE)**: `E[||error||²]`
2. **Estimation Accuracy**: Correlation between true and estimated channels
3. **Convergence Rate**: Speed of weight adaptation
4. **Hardware Efficiency**: Clock cycles per estimation

## Integration with Communication Systems

This module can be integrated into:

1. **OFDM Receivers**: For subcarrier channel estimation
2. **MIMO Systems**: For multiple antenna channel estimation
3. **Adaptive Equalizers**: For real-time channel tracking
4. **Software-Defined Radios**: For flexible channel estimation

## Advantages of This Approach

1. **Hardware Efficient**: Optimized for FPGA implementation
2. **Scalable**: Configurable number of pilots and channels
3. **Trainable**: Supports online learning for MMSE optimization
4. **Robust**: Includes overflow detection and error handling
5. **Real-time**: Suitable for high-speed communication systems

## Future Enhancements

1. **Adaptive Weight Update**: Implement gradient descent in hardware
2. **Non-linear Estimation**: Support for neural network-based estimation
3. **Multi-path Channels**: Extended support for frequency-selective channels
4. **Noise Estimation**: Joint channel and noise variance estimation