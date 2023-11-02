---
tags:
- gpt2
- text-generation
- music-modeling
- music-generation
widget:
- text: PIECE_START
- text: PIECE_START PIECE_START TRACK_START INST=34 DENSITY=8
- text: PIECE_START TRACK_START INST=1
---


# GPT-2 for Music

Language Models such as GPT-2 can be used for Music Generation. The idea is to represent pieces of music as texts, effectively reducing the task to Language Generation.

This model is a rather small instance of GPT-2 trained the [Lakhclean dataset](https://colinraffel.com/projects/lmd/). The model generates 4 bars at a time at a 16th note resolution with 4/4 meter.

If you want to contribute, if you want to say hello, if you want to know more, find me here:

- https://www.linkedin.com/in/dr-tristan-behrens-734967a2/
- https://www.youtube.com/@drtristanbehrens 
- https://twitter.com/DrTBehrens
- https://github.com/AI-Guru
- https://huggingface.co/TristanBehrens
- https://huggingface.co/ai-guru

Run the model on Google Colab: https://colab.research.google.com/drive/1Mz-KJ8vX4Wylr4mzvgP-MclDwQJ06KSq?usp=sharing

## License

You are free to use this model in any open-source context without charge. If you do so, please credit me.

However, if you wish to use the model for commercial purposes, please contact me to discuss licensing terms. Depending on the specific use case, there may be fees associated with commercial use. I am open to negotiating the terms of the license to meet your needs and ensure that the model is used appropriately. Please feel free to reach out to me at your earliest convenience to discuss further.

## Model description

The model is GPT-2 with 6 decoders and 8 attention heads each. The context length is 2048. The embedding dimensions are 512.

## Model family

This model is part of a huge group of Transformers I have trained. Most of them are not publicly available.

If you are interested in using andor licensing one of the models, please get in touch. 

### Lakhclean

These models were trained on roundabout 15K MIDI files (the same as the model you are viewing now) from the Lakhclean dataset.

- lakhclean_mmmbar_4bars_d-2048: 4 bars resolution, bar inpainting, note density conditioning
- lakhclean_mmmbar_8bars_d-2048: 8 bars resolution, bar inpainting, note density conditioning
- lakhclean_mmmtrack_4bars_chords: 4 bars resolution, chord conditioning
- lakhclean_mmmtrack_4bars_d-2048: 4 bars resolution, note density conditioning (this model)
- lakhclean_mmmtrack_4bars_simple-2048: 4 bars resolution
- lakhclean_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning

### Lakhfull

These models were trained on roundabout 175K MIDI files from the Lakh dataset.

- lakhfull_mmmtrack_4bars_d-2048: 4 bars resolution, note density conditioning (the big brother of this model)
- lakhfull_mmmtrack_4bars_simple-2048: 4 bars resolution

### Metal

These models were trained on roundabout 7K MIDI files from my own collections. They contain genre conditioning.

- metal_mmmbar_4bars_d-2048: 4 bars resolution, bar inpainting, note density conditioning
- metal_mmmbar_8bars_d-2048: 8 bars resolution, bar inpainting, note density conditioning
- metal_mmmtrack_4bars_d-2048: 4 bars resolution, note density conditioning
- metal_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning

### MetaMIDI Dataset genres

These models were trained on genre-specific subsets of the MetaMIDI dataset.

- mmd-baroque_mmmtrack_4bars_d-2048: 4 bars resolution, note density conditioning
- mmd-baroque_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning
- mmd-classical_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning
- mmd-noncontemporary_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning
- mmd-pop_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning
- mmd-renaissance_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning

### MetaMIDI Dataset full

These models were trained on roundabout 400K MIDI files from the MetaMIDI dataset.

- mmd-full_mmmtrack_4bars_d-2048: 4 bars resolution, note density conditioning
- mmd-full_mmmtrack_8bars_d-2048: 8 bars resolution, note density conditioning
- mmd-full_mmmtrack_4bars_chords-d-2048: 4 bars resolution, note density conditioning, chord conditioning (most powerful model in the entire group)

## Intended uses & limitations

This model is just a proof of concept. It shows that HuggingFace can be used to compose music.

### How to use

There is a notebook in the repo that you can use to generate symbolic music and then render it.

### Limitations and bias

Since this model has been trained on a very small corpus of music, it is overfitting heavily. 

### Acknowledgements

This model has been created with support from NVIDIA. I am very grateful for the GPU compute they provided!