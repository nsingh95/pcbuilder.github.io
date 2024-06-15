import csv
import random

# Function to generate a random benchmark score
def generate_benchmark():
    return random.randint(1000, 5000)  # Assuming a benchmark score between 1000 and 5000

# Function to assess compatibility
def check_compatibility(cpu_model, gpu_model, motherboard_model, ram_model):
    # Perform compatibility checks here
    # For simplicity, assuming all combinations are compatible
    return True

# Function to write data to CSV file
def write_to_csv(data):
    with open('pc_configurations.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["CPU", "GPU", "Motherboard", "RAM", "Benchmark", "Compatibility"])
        for row in data:
            writer.writerow(row)

# Main function
def main():
    configurations = []
    cpu_models = ["AMD Ryzen 9 3950X", "Intel Core i9-10900K", "AMD Ryzen 7 5800X"]
    gpu_models = ["NVIDIA GeForce RTX 2080 Ti", "NVIDIA GeForce RTX 3080", "AMD Radeon RX 6800 XT"]
    motherboard_models = ["ASUSTeK COMPUTER INC. GA35DX", "MSI MAG X570 TOMAHAWK WIFI", "GIGABYTE Z490 AORUS ELITE"]
    ram_models = ["Corsair Vengeance LPX 16GB (2 x 8GB) DDR4-3600", "G.Skill Trident Z RGB 32GB (2 x 16GB) DDR4-3200", "Crucial Ballistix 16GB (2 x 8GB) DDR4-3200"]

    for _ in range(10):
        cpu_model = random.choice(cpu_models)
        gpu_model = random.choice(gpu_models)
        motherboard_model = random.choice(motherboard_models)
        ram_model = random.choice(ram_models)
        benchmark = generate_benchmark()
        compatibility = check_compatibility(cpu_model, gpu_model, motherboard_model, ram_model)
        configurations.append([cpu_model, gpu_model, motherboard_model, ram_model, benchmark, compatibility])

    write_to_csv(configurations)
    print("PC configurations generated and written to pc_configurations.csv")

if __name__ == "__main__":
    main()
