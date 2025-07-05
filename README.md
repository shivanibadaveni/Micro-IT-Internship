# MMSE Channel Estimation using Linear Regression

## Project Overview
This project implements a **hardware-efficient linear regression module** for **channel estimation in wireless communication systems**, designed to approach the **Minimum Mean Squared Error (MMSE) bound** using machine learning techniques.

## 🎯 Key Features
- **Multi-channel estimation** for MIMO/OFDM systems
- **Machine learning support** with trainable parameters
- **MMSE optimization** capabilities
- **Hardware-efficient** SystemVerilog implementation
- **Real-time processing** with state machine architecture
- **Overflow protection** and error handling
- **Comprehensive testbench** included

## 📁 Project Structure

```
├── LinearRegression_ChannelEstimation.sv  # Main module + testbench
├── ChannelEstimation_Documentation.md     # Detailed technical documentation
├── Code_Comparison.md                     # Original vs improved comparison
├── run_simulation.tcl                     # Simulation script
└── README.md                              # This file
```

## 🔧 Module Interface

### **Input Signals**
- `pilot_signals[7:0]` - Array of received pilot signals (16-bit signed)
- `weights[3:0][7:0]` - Weight matrix for linear regression (18-bit signed)
- `bias[3:0]` - Bias terms for each channel (16-bit signed)
- `true_channels[3:0]` - Reference channels for training
- Control signals: `clk`, `rst`, `enable`, `estimation_enable`, `training_mode`

### **Output Signals**
- `channel_estimates[3:0]` - Estimated channel coefficients (16-bit signed)
- `estimation_error[3:0]` - Training error signals
- Status signals: `estimation_valid`, `overflow_flag`

## 🚀 Quick Start

### 1. **Simulation (Vivado)**
```bash
# In Vivado TCL console
source run_simulation.tcl
```

### 2. **Simulation (ModelSim)**
```bash
# Compile
vlog LinearRegression_ChannelEstimation.sv

# Simulate
vsim tb_LinearRegression_ChannelEstimation
run 1000ns
```

### 3. **Manual Integration**
```systemverilog
// Instantiate the module
LinearRegression_ChannelEstimation #(
    .DATA_WIDTH(16),
    .NUM_PILOTS(8),
    .NUM_CHANNELS(4)
) channel_estimator (
    .clk(clk),
    .rst(rst),
    .enable(enable),
    .pilot_signals(pilot_signals),
    .weights(weights),
    .bias(bias),
    .channel_estimates(channel_estimates),
    .estimation_valid(estimation_valid)
);
```

## 📊 Performance Analysis

### **Original vs Improved Code**
| Feature | Original | Improved |
|---------|----------|----------|
| **Inputs** | 1 feature | 8 pilot signals |
| **Outputs** | 1 prediction | 4 channel estimates |
| **Parameters** | 2 fixed | 32+ trainable |
| **Training** | None | Full MMSE support |
| **Precision** | 16-bit | 18/32-bit |

### **Hardware Resources (Estimated)**
- **Multipliers**: 8 (for parallel processing)
- **Adders**: 32+ (accumulation tree)
- **Registers**: ~200
- **Memory**: Weight matrices + pilot buffers

## 🔬 Technical Details

### **Mathematical Model**
```
h_est = W * x + b
```
Where:
- `h_est`: Estimated channel vector (4×1)
- `W`: Weight matrix (4×8)
- `x`: Pilot signal vector (8×1)
- `b`: Bias vector (4×1)

### **MMSE Optimization**
The module minimizes:
```
J = E[||h_true - h_est||²]
```

### **State Machine**
1. **IDLE** → Wait for estimation trigger
2. **COMPUTE** → Calculate weight × pilot products
3. **ACCUMULATE** → Sum products for each channel
4. **OUTPUT** → Generate final estimates
5. **ERROR_COMPUTE** → Calculate training errors (if training mode)

## 🎯 Applications

### **Wireless Communication Systems**
- **5G/6G Networks**: Channel estimation for massive MIMO
- **WiFi 6/7**: Multi-user channel estimation
- **LTE/5G**: OFDM subcarrier channel estimation

### **Hardware Implementations**
- **FPGA**: Xilinx Zynq, Intel Stratix
- **ASIC**: Custom wireless baseband chips
- **SDR**: Software-defined radio platforms

## 📈 Usage Examples

### **Basic Channel Estimation**
```systemverilog
// Configure QPSK pilot signals
pilot_signals[0] = 16'd1024;   // +1 (Q10 format)
pilot_signals[1] = -16'd1024;  // -1 (Q10 format)
// ... configure remaining pilots

// Set initial weights
weights[0][0] = 18'd512;  // Example weight
// ... configure weight matrix

// Trigger estimation
estimation_enable = 1;
@(posedge clk) estimation_enable = 0;

// Wait for result
wait(estimation_valid);
// Read channel_estimates[] array
```

### **Training Mode**
```systemverilog
// Provide reference channels
true_channels[0] = 16'd2048;  // Known channel 0
// ... set true channels

// Enable training
training_mode = 1;
estimation_enable = 1;
@(posedge clk) estimation_enable = 0;

wait(estimation_valid);
// Read estimation_error[] for weight updates
```

## 🧪 Testing & Validation

### **Included Tests**
- **Functional**: Basic estimation with known pilots
- **Training**: Error computation and validation
- **Corner Cases**: Overflow detection
- **Performance**: Timing and resource usage

### **Validation Metrics**
- **MSE**: Mean squared error between true and estimated channels
- **Accuracy**: Correlation coefficient
- **Timing**: Clock cycles per estimation
- **Resources**: Hardware utilization

## 🔧 Customization

### **Parameters**
- `DATA_WIDTH`: Signal precision (default: 16)
- `NUM_PILOTS`: Number of pilot signals (default: 8)
- `NUM_CHANNELS`: Number of channels to estimate (default: 4)
- `WEIGHT_WIDTH`: Weight precision (default: 18)
- `ACCUMULATOR_WIDTH`: Internal precision (default: 32)

### **Scaling for Different Systems**
- **SISO**: Set `NUM_CHANNELS = 1`
- **2×2 MIMO**: Set `NUM_CHANNELS = 4`
- **4×4 MIMO**: Set `NUM_CHANNELS = 16`
- **More Pilots**: Increase `NUM_PILOTS` for better accuracy

## 🚧 Future Enhancements

### **Planned Features**
1. **Adaptive Weight Updates**: Hardware gradient descent
2. **Non-linear Estimation**: Neural network support
3. **Noise Estimation**: Joint channel/noise estimation
4. **Pipeline Optimization**: Higher throughput variants

### **Integration Opportunities**
- **Equalizer Integration**: Direct connection to adaptive equalizers
- **Decoder Integration**: Joint estimation/decoding
- **Beamforming**: Integration with MIMO beamforming

## 📚 Documentation

- **[ChannelEstimation_Documentation.md](ChannelEstimation_Documentation.md)**: Detailed technical documentation
- **[Code_Comparison.md](Code_Comparison.md)**: Original vs improved comparison
- **[run_simulation.tcl](run_simulation.tcl)**: Simulation automation script

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Create your feature branch
3. Add comprehensive tests
4. Submit a pull request

## 📄 License

This project is provided for educational and research purposes. Please cite appropriately if used in academic work.

## 🔗 References

- **MMSE Channel Estimation**: Optimal estimator theory
- **Linear Regression**: Machine learning fundamentals
- **Wireless Communications**: OFDM and MIMO systems
- **Hardware Design**: SystemVerilog and FPGA implementation

---

**Author**: AI Assistant  
**Project**: MMSE Channel Estimation using Linear Regression  
**Date**: 2024