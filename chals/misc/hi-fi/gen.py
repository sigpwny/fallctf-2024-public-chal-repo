import wave
import struct

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None

input_file = 'source.wav'
output_file = 'chal.wav'
# sample width in bytes of output
out_width = 64
# out_width = 4
# how much to scale up the sample rate
sample_rate_scale = 4

# processing chunk size
chunk_size = 64

def p16(num):
    return struct.pack('<H', num)

def p32(num):
    return struct.pack('<I', num)

# see spec: http://soundfile.sapp.org/doc/WaveFormat/

with wave.open(input_file, 'rb') as src:
    new_sample_rate = src.getframerate() * sample_rate_scale
    with open(output_file, 'wb') as out:
        out.write(b'RIFF')
        out.write(p32(36 + src.getnframes() * sample_rate_scale * src.getnchannels() * out_width))
        out.write(b'WAVE')

        out.write(b'fmt ')
        out.write(p32(16)) # subchunk1size
        out.write(p16(1)) # audio format
        out.write(p16(src.getnchannels())) # num channels

        out.write(p32(new_sample_rate)) # sample rate
        out.write(p32(new_sample_rate * src.getnchannels() * out_width)) # byte rate
        out.write(p16(src.getnchannels() * out_width)) # block align
        out.write(p16(out_width * 8)) # bits per sample

        out.write(b'data')
        out.write(p32(src.getnframes() * sample_rate_scale * src.getnchannels() * out_width))

        if tqdm is None:
            iterator = range(0, src.getnframes(), chunk_size)
        else:
            iterator = tqdm(range(0, src.getnframes(), chunk_size))
        for _ in iterator:
            data = src.readframes(chunk_size)
            assert len(data) % (src.getnchannels() * src.getsampwidth()) == 0
            new_data = b''
            for i in range(0, len(data), src.getsampwidth()):
                new_data += (b'\x00' * (out_width - src.getsampwidth()) + data[i:i+src.getsampwidth()]) * sample_rate_scale
            out.write(new_data)
