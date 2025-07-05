# TCL Script for Channel Estimation Simulation
# Compatible with Vivado, ModelSim, and other EDA tools

# Create simulation project
create_project -force channel_estimation_sim . -part xc7z020clg484-1

# Add source files
add_files -norecurse LinearRegression_ChannelEstimation.sv

# Set testbench as top module
set_property top tb_LinearRegression_ChannelEstimation [get_filesets sim_1]

# Run behavioral simulation
launch_simulation -mode behavioral

# Run simulation for adequate time
run 1000ns

# Add signals to waveform (if using GUI)
add_wave -group "Control Signals" /tb_LinearRegression_ChannelEstimation/clk
add_wave -group "Control Signals" /tb_LinearRegression_ChannelEstimation/rst
add_wave -group "Control Signals" /tb_LinearRegression_ChannelEstimation/enable
add_wave -group "Control Signals" /tb_LinearRegression_ChannelEstimation/estimation_enable
add_wave -group "Control Signals" /tb_LinearRegression_ChannelEstimation/training_mode

add_wave -group "Input Pilots" /tb_LinearRegression_ChannelEstimation/pilot_signals

add_wave -group "Channel Estimates" /tb_LinearRegression_ChannelEstimation/channel_estimates
add_wave -group "Channel Estimates" /tb_LinearRegression_ChannelEstimation/estimation_valid
add_wave -group "Channel Estimates" /tb_LinearRegression_ChannelEstimation/overflow_flag

add_wave -group "Training" /tb_LinearRegression_ChannelEstimation/true_channels
add_wave -group "Training" /tb_LinearRegression_ChannelEstimation/estimation_error

add_wave -group "Internal State" /tb_LinearRegression_ChannelEstimation/dut/state
add_wave -group "Internal State" /tb_LinearRegression_ChannelEstimation/dut/accumulator

# Configure waveform display
configure_wave -namecolwidth 200
configure_wave -valuecolwidth 100

# Print simulation results
puts "========================================="
puts "Channel Estimation Simulation Complete"
puts "========================================="
puts "Check waveform for detailed analysis"
puts "Key signals:"
puts "- estimation_valid: Indicates when estimates are ready"
puts "- overflow_flag: Monitors for arithmetic overflow"
puts "- channel_estimates: Primary output estimates"
puts "- estimation_error: Training error signals"
puts "========================================="