# Hi-fi

## Guidance for admin/helpers giving hints

- this is not stego; no guess needed, just play the audio file
- try reducing the bit depth
- understand how the samples are stored in the audio file

## Generation code

The file `gen.py` creates the highly inflated audio file from an original file source.wav, which is me reading the flag aloud.

## Solution

The original audio had its sample rate and bit depth increased to absurd numbers. The only thing needed to make the audio file playable is to reduce the bit depth from 512 bits to something more reasonble, like 32 bits. To my knowledge, there are no publically available audio players that can play back the 512-bit PCM data in the WAVE file provided. The solution is to reduce the bit depth yourself, using an understanding of the [WAVE format](http://soundfile.sapp.org/doc/WaveFormat/) and reducing the number of bytes for each sample.
