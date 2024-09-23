import wave
from tqdm import tqdm

# Parameters
input_file = 'chal.wav'
output_file = 'restored.wav'
sample_rate_scale = 4      # Factor by which the sample rate was scaled
out_width = 64             # Padded bit depth in bytes
original_width = 4         # Original bit depth in bytes (4 bytes = 32 bits)

# Function to extract the original sample by removing the padding
def extract_original_sample(padded_sample):
    return padded_sample[-original_width:]

# Open the input WAV file
with wave.open(input_file, 'rb') as src:
    num_channels = src.getnchannels()
    src_sample_rate = src.getframerate()
    src_sample_width = src.getsampwidth()
    total_frames = src.getnframes()
    original_sample_rate = src_sample_rate // sample_rate_scale

    # Open the output WAV file for writing
    with wave.open(output_file, 'wb') as out:
        out.setnchannels(num_channels)
        out.setsampwidth(original_width)
        out.setframerate(original_sample_rate)

        # Loop through the original frames and reverse the tampering
        for _ in tqdm(range(total_frames // sample_rate_scale), desc='Reversing tampering'):
            # Read the duplicated group of frames
            data = src.readframes(sample_rate_scale)
            frame = data[:num_channels * out_width]
            original_samples = bytearray()

            # Extract the original samples for each channel
            for ch in range(num_channels):
                start, end = ch * out_width, (ch + 1) * out_width
                original_sample = extract_original_sample(frame[start:end])
                original_samples.extend(original_sample)

            # Write the restored samples to the output file
            out.writeframes(original_samples)